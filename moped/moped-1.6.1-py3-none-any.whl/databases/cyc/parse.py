"""Parse and repair metacyc or biocyc PGDB databases."""
from __future__ import annotations

import re
import warnings
from collections import defaultdict
from functools import partial
from pathlib import Path
from typing import Any, Callable, Dict, Iterable, List, Set, Tuple

from ...core.reaction import Monomer
from .data import ParseCompound, ParseEnzyme, ParseGene, ParseReaction

# Often lines starting with these identifiers are malformed
MALFORMED_LINE_STARTS = {
    "/",
    "COMMENT",
    "CITATIONS",
    "^CITATIONS",
    "SYNONYMS",
    "#",
}


def _check_for_monomer(
    enzrxn: str,
    protein: str,
    monomers: Iterable[str],
    complexes: Dict[str, Set[str]],
    enzrxn_to_monomer: Dict[str, Set[str]],
) -> None:
    """Check complex tree until you arrive at monomers."""
    try:
        for subcomplex in complexes[protein]:
            if subcomplex in monomers:
                enzrxn_to_monomer.setdefault(enzrxn, set()).add(subcomplex)
            else:
                _check_for_monomer(enzrxn, subcomplex, monomers, complexes, enzrxn_to_monomer)
    except KeyError:
        pass


def _get_enzrnx_to_monomer_mapping(
    enzrxns: Dict[str, ParseEnzyme],
    monomers: Iterable[str],
    complexes: Dict[str, Set[str]],
) -> Dict[str, Set[str]]:
    """Get mapping of enzyme reactions to monomers."""
    enzrxn_to_monomer: Dict[str, Set[str]] = {}
    for enzrxn, enzrxn_dict in enzrxns.items():
        protein = enzrxn_dict.enzyme
        if protein is not None:
            if protein in monomers:
                enzrxn_to_monomer.setdefault(enzrxn, set()).add(protein)
            else:
                _check_for_monomer(enzrxn, protein, monomers, complexes, enzrxn_to_monomer)
    return enzrxn_to_monomer


def _get_enzrnx_to_sequence_mapping(
    enzrxn_to_monomer: Dict[str, Set[str]], sequences: Dict[str, str]
) -> Dict[str, Dict[str, str]]:
    """Get mapping of enzyme reactions to sequences."""
    enzrxn_to_sequence: Dict[str, Dict[str, str]] = {}
    for enzrxn, monomers in enzrxn_to_monomer.items():
        for monomer in monomers:
            try:
                sequence = sequences[monomer]
                enzrxn_to_sequence.setdefault(enzrxn, dict())[monomer] = sequence
            except KeyError:
                pass
    return enzrxn_to_sequence


def _map_reactions_to_sequences(
    reactions: Dict[str, ParseReaction],
    enzrxn_to_monomer: Dict[str, Set[str]],
    enzrxn_to_seq: Dict[str, Dict[str, str]],
) -> None:
    """Get mapping of enzyme reactions to sequences."""
    for reaction in reactions.values():
        try:
            for enzrxn in reaction.enzymes:
                try:
                    reaction.sequences.update(enzrxn_to_seq[enzrxn])
                except KeyError:
                    pass
                try:
                    reaction.monomers.setdefault(enzrxn, set()).update(enzrxn_to_monomer[enzrxn])
                except KeyError:
                    pass
        except KeyError:
            pass


def _map_reactions_to_kinetic_parameters(
    reactions: Dict[str, ParseReaction],
    enzrxns: Dict[str, ParseEnzyme],
) -> None:
    """Get mapping of enzyme reactions to kinetic parameters."""
    for reaction in reactions.values():
        try:
            for enzrxn in reaction.enzymes:
                try:
                    enzyme = enzrxns[enzrxn]
                except KeyError:
                    pass
                else:
                    if bool(enzyme.kcat):
                        reaction.enzrxns.setdefault(enzyme.id, {}).setdefault("kcat", enzyme.kcat)
                    if bool(enzyme.km):
                        reaction.enzrxns.setdefault(enzyme.id, {}).setdefault("km", enzyme.km)
                    if bool(enzyme.vmax):
                        reaction.enzrxns.setdefault(enzyme.id, {}).setdefault("vmax", enzyme.vmax)
        except KeyError:
            pass


class Parser:
    """Base class for all metacyc/biocyc related databases."""

    def __init__(
        self,
        pgdb_path: Path,
        compartment_map: Dict[str, str],
        type_map: Dict[str, str],
        parse_sequences: bool = True,
    ) -> None:
        """Parse a *cyc pgdb into a moped.Model.

        Parameters
        ----------
        pgdb_path : Path
            Path to the pgdb
        parse_enzymes : bool
        parse_sequences : bool
        name : str, optional

        Returns
        -------
        moped.Model
        """
        self.path = Path(pgdb_path)
        self.parse_sequences = parse_sequences
        self.compartment_map = compartment_map
        self.type_map = type_map

    def parse(
        self,
    ) -> Tuple[Dict[str, ParseCompound], Dict[str, List[str]], Dict[str, ParseReaction], Dict[str, Monomer]]:
        """Parse the database."""
        path = self.path
        parse_compounds, compound_types = CompoundParser(
            path / "compounds.dat", type_map=self.type_map
        ).parse()
        parse_reactions = ReactionParser(path / "reactions.dat", type_map=self.type_map).parse()
        genes = GeneParser(path / "genes.dat").parse()

        if self.parse_sequences:
            try:
                enzrxns = EnzymeParser(path / "enzrxns.dat").parse()
                monomers, complexes = ProteinParser(path / "proteins.dat").parse()
                sequences = SequenceParser(path / "protseq.fsa").parse()
            except FileNotFoundError:
                pass
            else:
                enzrxn_to_monomer = _get_enzrnx_to_monomer_mapping(enzrxns, monomers, complexes)
                enzrxn_to_seq = _get_enzrnx_to_sequence_mapping(enzrxn_to_monomer, sequences)
                enzrxn_to_monomer = _get_enzrnx_to_monomer_mapping(enzrxns, monomers, complexes)
                enzrxn_to_seq = _get_enzrnx_to_sequence_mapping(enzrxn_to_monomer, sequences)
                _map_reactions_to_sequences(parse_reactions, enzrxn_to_monomer, enzrxn_to_seq)
                _map_reactions_to_kinetic_parameters(parse_reactions, enzrxns)
        return parse_compounds, compound_types, parse_reactions, genes


###############################################################################
# Universal functions
###############################################################################


def _remove_top_comments(file: List[str]) -> Tuple[List[str], int]:
    """Remove the metainformation from a pgdb file."""
    for i, line in enumerate(file):
        if line.startswith("UNIQUE-ID"):
            break
    return file[i:], i


def _open_file_and_remove_comments(path: Path) -> Tuple[List[str], int]:
    """Read the file and remove metainformation."""
    with open(path, encoding="ISO-8859-14") as f:
        file = f.readlines()
    return _remove_top_comments(file)


def _rename(content: str) -> str:
    """Remove garbage from compound and reaction ids."""
    return (
        content.replace("<i>", "")
        .replace("</i>", "")
        .replace("<SUP>", "")
        .replace("</SUP>", "")
        .replace("<sup>", "")
        .replace("</sup>", "")
        .replace("<sub>", "")
        .replace("</sub>", "")
        .replace("<SUB>", "")
        .replace("</SUB>", "")
        .replace("&", "")
        .replace(";", "")
        .replace("|", "")
    )


def _do_nothing(*args: Any) -> None:
    """Chill. The archetype of a useful function."""
    pass


def _set_gibbs0(dictionary: Dict[str, ParseReaction | ParseCompound], id_: str, gibbs0: str) -> None:
    dictionary[id_].gibbs0 = float(gibbs0)


def _set_name(dictionary: Dict[str, ParseReaction | ParseCompound], id_: str, name: str) -> None:
    dictionary[id_].name = _rename(name)


def _add_database_link(dictionary: Dict[str, ParseReaction | ParseCompound], id_: str, content: str) -> None:
    """Short description.

    Database links are of form DBLINKS - (REFMET "Tryptophan" NIL |midford| 3697479617 NIL NIL)
    so content will be (REFMET "Tryptophan" NIL |midford| 3697479617 NIL NIL)
    """
    database, database_id, *_ = content[1:-1].split(" ")
    dictionary[id_].database_links.setdefault(database, set()).add(database_id[1:-1])


def _add_type(
    dictionary: Dict[str, ParseReaction | ParseCompound],
    id_: str,
    type_: str,
    type_map: Dict[str, str],
) -> None:
    """Short description."""
    dictionary[id_].types.append(type_map.get(type_, type_))


###############################################################################
# Compound function
###############################################################################


def _set_atom_charges(compounds: Dict[str, ParseCompound], id_: str, content: str) -> None:
    """Short description.

    Parameters
    ----------
    Compounds : dict
    id_ : str
    content : str(int int)
        Are of form "(8 -1)", we only need the second part
    """
    compounds[id_].charge += int(content[1:-1].split()[-1])


def _set_chemical_formula(compounds: Dict[str, ParseCompound], id_: str, content: str) -> None:
    """Short description.

    Parameters
    ----------
    Compounds : dict
    id_ : str
    content : str(int int)
        Are of form (C 11)
    """
    atom, count = content[1:-1].split(" ")
    compounds[id_].formula[atom] = int(count)


def _set_smiles(compounds: Dict[str, ParseCompound], id_: str, content: str) -> None:
    """Short description.

    Parameters
    ----------
    Compounds : dict
    id_ : str
    content : str
    """
    compounds[id_].smiles = content


class CompoundParser:
    """Class to parse compounds."""

    def __init__(self, path: Path, type_map: Dict[str, str]) -> None:
        """Parser compound information."""
        file, start_idx = _open_file_and_remove_comments(path)
        self.file = file
        self.start_idx = start_idx
        self.type_map = type_map

        self.actions: Dict[str, Callable[[Any, Any, Any], None]] = {
            "TYPES": partial(_add_type, type_map=self.type_map),
            "COMMON-NAME": _set_name,
            "ABBREV-NAME": _do_nothing,
            "ACCESSION-1": _do_nothing,
            "ANTICODON": _do_nothing,
            "ATOM-CHARGES": _set_atom_charges,
            "ATOM-ISOTOPES": _do_nothing,
            "CATALYZES": _do_nothing,
            "CFG-ICON-COLOR": _do_nothing,
            "CHEMICAL-FORMULA": _set_chemical_formula,
            "CITATIONS": _do_nothing,
            "CODING-SEGMENTS": _do_nothing,
            "CODONS": _do_nothing,
            "COFACTORS-OF": _do_nothing,
            "COMMENT": _do_nothing,
            "COMPONENT-COEFFICIENTS": _do_nothing,
            "COMPONENT-OF": _do_nothing,
            "COMPONENTS": _do_nothing,
            "CONSENSUS-SEQUENCE": _do_nothing,
            "COPY-NUMBER": _do_nothing,
            "CREDITS": _do_nothing,
            "DATA-SOURCE": _do_nothing,
            "DBLINKS": _add_database_link,
            "DNA-FOOTPRINT-SIZE": _do_nothing,
            "DOCUMENTATION": _do_nothing,
            "ENZYME-NOT-USED-IN": _do_nothing,
            "EXPRESSION-MECHANISM": _do_nothing,
            "FAST-EQUILIBRATING-INSTANCES?": _do_nothing,
            "FEATURES": _do_nothing,
            "FUNCTIONAL-ASSIGNMENT-COMMENT": _do_nothing,
            "FUNCTIONAL-ASSIGNMENT-STATUS": _do_nothing,
            "GENE": _do_nothing,
            "GIBBS-0": _set_gibbs0,
            "GO-TERMS": _do_nothing,
            "GROUP-COORDS-2D": _do_nothing,
            "GROUP-INTERNALS": _do_nothing,
            "HAS-NO-STRUCTURE?": _do_nothing,
            "HIDE-SLOT?": _do_nothing,
            "IN-MIXTURE": _do_nothing,
            "INCHI": _do_nothing,
            "INCHI-KEY": _do_nothing,
            "INSTANCE-NAME-TEMPLATE": _do_nothing,
            "INTERNALS-OF-GROUP": _do_nothing,
            "ISOZYME-SEQUENCE-SIMILARITY": _do_nothing,
            "LEFT-END-POSITION": _do_nothing,
            "LOCATIONS": _do_nothing,
            "MEMBER-SORT-FN": _do_nothing,
            "MODIFIED-FORM": _do_nothing,
            "MOLECULAR-WEIGHT": _do_nothing,
            "MOLECULAR-WEIGHT-EXP": _do_nothing,
            "MOLECULAR-WEIGHT-KD": _do_nothing,
            "MOLECULAR-WEIGHT-SEQ": _do_nothing,
            "MONOISOTOPIC-MW": _do_nothing,
            "N+1-NAME": _do_nothing,
            "N-1-NAME": _do_nothing,
            "N-NAME": _do_nothing,
            "NEIDHARDT-SPOT-NUMBER": _do_nothing,
            "NON-STANDARD-INCHI": _do_nothing,
            "PATHOLOGIC-NAME-MATCHER-EVIDENCE": _do_nothing,
            "PATHOLOGIC-PWY-EVIDENCE": _do_nothing,
            "PI": _do_nothing,
            "PKA1": _do_nothing,
            "PKA2": _do_nothing,
            "PKA3": _do_nothing,
            "RADICAL-ATOMS": _do_nothing,
            "REGULATED-BY": _do_nothing,
            "REGULATES": _do_nothing,
            "RIGHT-END-POSITION": _do_nothing,
            "SMILES": _set_smiles,
            "SPECIES": _do_nothing,
            "SPLICE-FORM-INTRONS": _do_nothing,
            "STRUCTURE-GROUPS": _do_nothing,
            "STRUCTURE-LINKS": _do_nothing,
            "SUPERATOMS": _do_nothing,
            "SYMMETRY": _do_nothing,
            "SYNONYMS": _do_nothing,
            "SYSTEMATIC-NAME": _do_nothing,
            "TAUTOMERS": _do_nothing,
            "UNMODIFIED-FORM": _do_nothing,
            "LOGP": _do_nothing,
            "POLAR-SURFACE-AREA": _do_nothing,
        }

    @staticmethod
    def gather_compound_types(compounds: Dict[str, ParseCompound]) -> Dict[str, List[str]]:
        """Return (type: list(cpds)) dictionary.

        Only uses the highest-level type
        """
        types = defaultdict(list)
        for id_, cpd in compounds.items():
            if bool(cpd.types):
                # Only use highest level
                types[cpd.types[-1] + "_c"].append(id_)
        return dict(types)

    def parse(self) -> Tuple[Dict[str, ParseCompound], Dict[str, List[str]]]:
        """Parse."""
        compounds: Dict[str, ParseCompound] = {}
        for line in self.file:
            if any(line.startswith(i) for i in MALFORMED_LINE_STARTS):
                continue
            else:
                identifier, content = line.rstrip().split(" - ", maxsplit=1)
                if identifier == "UNIQUE-ID":
                    base_id = content
                    id_ = content + "_c"
                    compounds[id_] = ParseCompound(
                        id=id_,
                        base_id=base_id,
                        compartment="CYTOSOL",
                    )
                else:
                    try:
                        self.actions[identifier](compounds, id_, content)
                    except KeyError:
                        warnings.warn(f"Unknown identifier {identifier} for compound {id_}")
        compound_types = self.gather_compound_types(compounds)
        return compounds, compound_types


###############################################################################
# Reaction functions
###############################################################################
def _set_ec_number(reactions: Dict[str, ParseReaction], id_: str, ec_number: str) -> None:
    reactions[id_].ec = ec_number


def _add_reaction_pathway(reactions: Dict[str, ParseReaction], id_: str, pathway: str) -> None:
    reactions[id_].pathways.add(pathway)


def _add_reaction_enzyme(reactions: Dict[str, ParseReaction], id_: str, enzyme: str) -> None:
    reactions[id_].enzymes.add(enzyme)


def _set_reaction_direction(reactions: Dict[str, ParseReaction], id_: str, direction: str) -> None:
    reactions[id_].direction = direction
    if direction == "REVERSIBLE":
        reactions[id_].reversible = True
    else:
        reactions[id_].reversible = False


def _add_reaction_location(reactions: Dict[str, ParseReaction], id_: str, location: str) -> None:
    location = location.replace("CCI-", "CCO-")
    if location.startswith("CCO-"):
        reactions[id_].locations.append(location)


def _set_substrate(
    reactions: Dict[str, ParseReaction],
    id_: str,
    substrate: str,
    type_map: Dict[str, str],
) -> None:
    substrate = _rename(type_map.get(substrate, substrate)) + "_c"
    reactions[id_].substrates[substrate] = -1
    reactions[id_].substrate_compartments[substrate] = "CCO-IN"


def _set_product(
    reactions: Dict[str, ParseReaction],
    id_: str,
    product: str,
    type_map: Dict[str, str],
) -> None:
    product = _rename(type_map.get(product, product)) + "_c"
    reactions[id_].products[product] = 1
    reactions[id_].product_compartments[product] = "CCO-IN"


def _set_substrate_coefficient(
    reactions: Dict[str, ParseReaction],
    id_: str,
    coefficient: str,
    substrate: str,
    type_map: Dict[str, str],
) -> None:
    try:
        reactions[id_].substrates[_rename(type_map.get(substrate, substrate)) + "_c"] = -float(coefficient)
    except ValueError:
        pass


def _set_product_coefficient(
    reactions: Dict[str, ParseReaction],
    id_: str,
    coefficient: str,
    product: str,
    type_map: Dict[str, str],
) -> None:
    try:
        reactions[id_].products[_rename(type_map.get(product, product)) + "_c"] = float(coefficient)
    except ValueError:
        pass


def _set_substrate_compartment(
    reactions: Dict[str, ParseReaction],
    id_: str,
    compartment: str,
    substrate: str,
    type_map: Dict[str, str],
) -> None:
    if compartment == "CCO-OUT":
        reactions[id_].substrate_compartments[
            _rename(type_map.get(substrate, substrate)) + "_c"
        ] = compartment
    elif compartment == "CCO-MIDDLE":
        reactions[id_].substrate_compartments[_rename(type_map.get(substrate, substrate)) + "_c"] = "CCO-OUT"


def _set_product_compartment(
    reactions: Dict[str, ParseReaction],
    id_: str,
    compartment: str,
    product: str,
    type_map: Dict[str, str],
) -> None:
    if compartment == "CCO-OUT":
        reactions[id_].product_compartments[_rename(type_map.get(product, product)) + "_c"] = compartment
    elif compartment == "CCO-MIDDLE":
        reactions[id_].product_compartments[_rename(type_map.get(product, product)) + "_c"] = "CCO-OUT"


class ReactionParser:
    """Reaction Parser."""

    def __init__(self, path: Path, type_map: Dict[str, str]) -> None:
        """Parse reactions and pathways."""
        file, start_idx = _open_file_and_remove_comments(path)
        self.file = file
        self.start_idx = start_idx
        self.type_map = type_map

        self.actions: Dict[str, Callable[[Any, Any, Any], None]] = {
            "TYPES": partial(_add_type, type_map=self.type_map),
            "COMMON-NAME": _set_name,
            "ATOM-MAPPINGS": _do_nothing,
            "CANNOT-BALANCE?": _do_nothing,
            "CITATIONS": _do_nothing,
            "COMMENT": _do_nothing,
            "CREDITS": _do_nothing,
            "DATA-SOURCE": _do_nothing,
            "DBLINKS": _add_database_link,
            "DOCUMENTATION": _do_nothing,
            "EC-NUMBER": _set_ec_number,
            "ENZYMATIC-REACTION": _add_reaction_enzyme,
            "ENZYMES-NOT-USED": _do_nothing,
            "EQUILIBRIUM-CONSTANT": _do_nothing,
            "GIBBS-0": _set_gibbs0,
            "HIDE-SLOT?": _do_nothing,
            "IN-PATHWAY": _add_reaction_pathway,
            "INSTANCE-NAME-TEMPLATE": _do_nothing,
            "LEFT": partial(_set_substrate, type_map=self.type_map),
            "MEMBER-SORT-FN": _do_nothing,
            "ORPHAN?": _do_nothing,
            "PATHOLOGIC-NAME-MATCHER-EVIDENCE": _do_nothing,
            "PATHOLOGIC-PWY-EVIDENCE": _do_nothing,
            "PHYSIOLOGICALLY-RELEVANT?": _do_nothing,
            "PREDECESSORS": _do_nothing,
            "PRIMARIES": _do_nothing,
            "REACTION-BALANCE-STATUS": _do_nothing,
            "REACTION-DIRECTION": _set_reaction_direction,
            "REACTION-LIST": _do_nothing,
            "REGULATED-BY": _do_nothing,
            "REQUIREMENTS": _do_nothing,
            "RIGHT": partial(_set_product, type_map=self.type_map),
            "RXN-LOCATIONS": _add_reaction_location,
            "SIGNAL": _do_nothing,
            "SPECIES": _do_nothing,
            "SPONTANEOUS?": _do_nothing,
            "STD-REDUCTION-POTENTIAL": _do_nothing,
            "SYNONYMS": _do_nothing,
            "SYSTEMATIC-NAME": _do_nothing,
            "TAXONOMIC-RANGE": _do_nothing,
        }

        self.sub_actions: Dict[str, Dict[str, Callable[[Any, Any, Any, Any], None]]] = {
            "^COMPARTMENT": {
                "LEFT": partial(_set_substrate_compartment, type_map=self.type_map),
                "RIGHT": lambda a, b, c, d: _set_product_compartment(a, b, c, d, type_map=self.type_map),
            },
            "^OFFICIAL?": {
                "EC-NUMBER": _do_nothing,
            },
            "^COEFFICIENT": {
                "LEFT": lambda a, b, c, d: _set_substrate_coefficient(a, b, c, d, type_map=self.type_map),
                "RIGHT": lambda a, b, c, d: _set_product_coefficient(a, b, c, d, type_map=self.type_map),
            },
        }  # type: ignore

    def parse(self) -> Dict[str, ParseReaction]:
        """Parse."""
        id_ = ""
        reactions = {}
        for line in self.file:
            if any(line.startswith(i) for i in MALFORMED_LINE_STARTS):
                continue
            else:
                identifier, content = line.rstrip().split(" - ", maxsplit=1)
                if identifier == "UNIQUE-ID":
                    id_ = content
                    reactions[id_] = ParseReaction(id=id_, base_id=id_)

                elif not identifier.startswith("^"):
                    try:
                        self.actions[identifier](reactions, id_, content)
                        last_identifier = identifier
                        last_content = content
                    except KeyError:
                        warnings.warn(f"Unknown identifier {identifier} for reaction {id_}")
                else:
                    self.sub_actions[identifier][last_identifier](reactions, id_, content, last_content)
        return reactions


###############################################################################
# Enzyme functions
###############################################################################


def _set_enzyme(enzrxns: Dict[str, ParseEnzyme], id_: str, enzyme: str) -> None:
    enzrxns[id_].enzyme = enzyme


def _add_kcat(enzrxns: Dict[str, ParseEnzyme], id_: str, substrate: str, kcat: str) -> None:
    enzrxns[id_].kcat.setdefault(substrate, float(kcat))


def _add_km(enzrxns: Dict[str, ParseEnzyme], id_: str, substrate: str, km: str) -> None:
    enzrxns[id_].km.setdefault(substrate, float(km))


def _add_vmax(enzrxns: Dict[str, ParseEnzyme], id_: str, substrate: str, vmax: str) -> None:
    enzrxns[id_].vmax.setdefault(substrate, float(vmax))


class EnzymeParser:
    """Enzyme Parser."""

    def __init__(self, path: Path) -> None:
        file, start_idx = _open_file_and_remove_comments(path)
        self.file = file
        self.start_idx = start_idx
        self.actions: Dict[str, Callable[[Any, Any, Any], None]] = {
            "UNIQUE-ID": _do_nothing,
            "TYPES": _do_nothing,
            "COMMON-NAME": _do_nothing,
            "ALTERNATIVE-COFACTORS": _do_nothing,
            "ALTERNATIVE-SUBSTRATES": _do_nothing,
            "BASIS-FOR-ASSIGNMENT": _do_nothing,
            "CITATIONS": _do_nothing,
            "COFACTOR-BINDING-COMMENT": _do_nothing,
            "COFACTORS": _do_nothing,
            "COMMENT": _do_nothing,
            "CREDITS": _do_nothing,
            "DATA-SOURCE": _do_nothing,
            "DBLINKS": _do_nothing,
            "DOCUMENTATION": _do_nothing,
            "ENZRXN-IN-PATHWAY": _do_nothing,
            "ENZYME": _set_enzyme,
            "HIDE-SLOT?": _do_nothing,
            "INSTANCE-NAME-TEMPLATE": _do_nothing,
            "KCAT": _do_nothing,
            "KM": _do_nothing,
            "MEMBER-SORT-FN": _do_nothing,
            "PATHOLOGIC-NAME-MATCHER-EVIDENCE": _do_nothing,
            "PATHOLOGIC-PWY-EVIDENCE": _do_nothing,
            "PH-OPT": _do_nothing,
            "PHYSIOLOGICALLY-RELEVANT?": _do_nothing,
            "REACTION": _do_nothing,
            "REACTION-DIRECTION": _do_nothing,
            "REGULATED-BY": _do_nothing,
            "REQUIRED-PROTEIN-COMPLEX": _do_nothing,
            "SPECIFIC-ACTIVITY": _do_nothing,
            "SYNONYMS": _do_nothing,
            "TEMPERATURE-OPT": _do_nothing,
            "VMAX": _do_nothing,
            "ENZRXN-EC-NUMBER": _do_nothing,
        }
        self.sub_actions: Dict[str, Dict[str, Callable[[Any, Any, Any, Any], None]]] = {
            "^SUBSTRATE": {"KM": _add_km, "VMAX": _add_vmax, "KCAT": _add_kcat},
            "^CITATIONS": {
                "KM": _do_nothing,
                "VMAX": _do_nothing,
                "KCAT": _do_nothing,
            },
        }

    def parse(self) -> Dict[str, ParseEnzyme]:
        """Parse."""
        id_ = ""
        enzrxns = {}
        for line in self.file:
            if any(line.startswith(i) for i in MALFORMED_LINE_STARTS):
                continue
            else:
                identifier, content = line.rstrip().split(" - ", maxsplit=1)
                if identifier == "UNIQUE-ID":
                    id_ = content
                    enzrxns[id_] = ParseEnzyme(id=id_)
                elif not identifier.startswith("^"):
                    try:
                        self.actions[identifier](enzrxns, id_, content)
                        last_identifier = identifier
                        last_content = content
                    except KeyError:
                        warnings.warn(f"Unknown identifier {identifier} for enzyme {id_}")
                else:
                    self.sub_actions[identifier][last_identifier](enzrxns, id_, content, last_content)
        return enzrxns


###############################################################################
# Protein functions
###############################################################################


def _add_component(complexes: Dict[str, Set[str]], complex_id: str, component: str) -> None:
    complexes[complex_id].add(component)


class ProteinParser:
    """Protein parser."""

    def __init__(self, path: Path) -> None:
        file, start_idx = _open_file_and_remove_comments(path)
        self.file = file
        self.start_idx = start_idx
        self.actions: Dict[str, Callable[[Any, Any, Any], None]] = {
            # "UNIQUE-ID": _do_nothing,
            "TYPES": _do_nothing,
            "COMMON-NAME": _do_nothing,
            "ABBREV-NAME": _do_nothing,
            "ACCESSION-1": _do_nothing,
            "AROMATIC-RINGS": _do_nothing,
            "ATOM-CHARGES": _do_nothing,
            "ATOM-ISOTOPES": _do_nothing,
            "CATALYZES": _do_nothing,
            "CHEMICAL-FORMULA": _do_nothing,
            "CITATIONS": _do_nothing,
            "CODING-SEGMENTS": _do_nothing,
            "COFACTORS-OF": _do_nothing,
            "COMMENT": _do_nothing,
            "COMPONENT-COEFFICIENTS": _do_nothing,
            "COMPONENT-OF": _do_nothing,
            "COMPONENTS": _add_component,
            "CONSENSUS-SEQUENCE": _do_nothing,
            "COPY-NUMBER": _do_nothing,
            "CREDITS": _do_nothing,
            "DATA-SOURCE": _do_nothing,
            "DBLINKS": _do_nothing,
            "DNA-FOOTPRINT-SIZE": _do_nothing,
            "DOCUMENTATION": _do_nothing,
            "ENZYME-NOT-USED-IN": _do_nothing,
            "EXPRESSION-MECHANISM": _do_nothing,
            "FAST-EQUILIBRATING-INSTANCES?": _do_nothing,
            "FEATURES": _do_nothing,
            "FUNCTIONAL-ASSIGNMENT-COMMENT": _do_nothing,
            "FUNCTIONAL-ASSIGNMENT-STATUS": _do_nothing,
            "GENE": _do_nothing,
            "GIBBS-0": _do_nothing,
            "GO-TERMS": _do_nothing,
            "GROUP-COORDS-2D": _do_nothing,
            "HAS-NO-STRUCTURE?": _do_nothing,
            "HIDE-SLOT?": _do_nothing,
            "IN-MIXTURE": _do_nothing,
            "INCHI": _do_nothing,
            "INCHI-KEY": _do_nothing,
            "INSTANCE-NAME-TEMPLATE": _do_nothing,
            "INTERNALS-OF-GROUP": _do_nothing,
            "ISOZYME-SEQUENCE-SIMILARITY": _do_nothing,
            "LOCATIONS": _do_nothing,
            "MEMBER-SORT-FN": _do_nothing,
            "MODIFIED-FORM": _do_nothing,
            "MOLECULAR-WEIGHT": _do_nothing,
            "MOLECULAR-WEIGHT-EXP": _do_nothing,
            "MOLECULAR-WEIGHT-KD": _do_nothing,
            "MOLECULAR-WEIGHT-SEQ": _do_nothing,
            "MONOISOTOPIC-MW": _do_nothing,
            "N+1-NAME": _do_nothing,
            "N-1-NAME": _do_nothing,
            "N-NAME": _do_nothing,
            "NEIDHARDT-SPOT-NUMBER": _do_nothing,
            "NON-STANDARD-INCHI": _do_nothing,
            "PATHOLOGIC-NAME-MATCHER-EVIDENCE": _do_nothing,
            "PATHOLOGIC-PWY-EVIDENCE": _do_nothing,
            "PI": _do_nothing,
            "PKA1": _do_nothing,
            "PKA2": _do_nothing,
            "PKA3": _do_nothing,
            "PROMOTER-BOX-NAME-1": _do_nothing,
            "PROMOTER-BOX-NAME-2": _do_nothing,
            "RADICAL-ATOMS": _do_nothing,
            "RECOGNIZED-PROMOTERS": _do_nothing,
            "REGULATED-BY": _do_nothing,
            "REGULATES": _do_nothing,
            "SMILES": _do_nothing,
            "SPECIES": _do_nothing,
            "SPLICE-FORM-INTRONS": _do_nothing,
            "STRUCTURE-BONDS": _do_nothing,
            "STRUCTURE-GROUPS": _do_nothing,
            "STRUCTURE-LINKS": _do_nothing,
            "SUPERATOMS": _do_nothing,
            "SYMMETRY": _do_nothing,
            "SYNONYMS": _do_nothing,
            "SYSTEMATIC-NAME": _do_nothing,
            "TAUTOMERS": _do_nothing,
            "UNMODIFIED-FORM": _do_nothing,
        }

    def parse(self) -> Tuple[Set[str], Dict[str, Set[str]]]:
        """Parse."""
        id_ = ""
        proteins: Dict[str, Set[str]] = {}
        monomers: Set[str] = set()
        complexes: Dict[str, Set[str]] = dict()
        for i, line in enumerate(self.file, self.start_idx):
            if any(line.startswith(i) for i in MALFORMED_LINE_STARTS):
                continue
            else:
                try:
                    identifier, content = line.rstrip().split(" - ", maxsplit=1)
                    if identifier == "UNIQUE-ID":
                        id_ = content
                        proteins[id_] = set()
                    elif not identifier.startswith("^"):
                        try:
                            self.actions[identifier](proteins, id_, content)
                        except KeyError:
                            warnings.warn(f"Unknown identifier {identifier} for protein {id_}")
                except ValueError:
                    warnings.warn(f"Malformed line {i} in proteins.dat")
        for k, v in proteins.items():
            if bool(v):
                complexes[k] = v
            else:
                monomers.add(k)
        return monomers, complexes


###############################################################################
# Sequence functions
###############################################################################


class SequenceParser:
    """SequenceParser."""

    def __init__(self, path: Path) -> None:
        with open(path, encoding="ISO-8859-14") as f:
            self.file = f.readlines()

    def parse(self) -> Dict[str, str]:
        """Parse."""
        RE_PAT = re.compile(r"^>gnl\|.*?\|")
        sequences: Dict[str, str] = {}
        for id_, sequence in zip(self.file[::2], self.file[1::2]):
            id_ = re.sub(RE_PAT, "", id_).split(" ", maxsplit=1)[0]
            sequences[id_] = sequence.strip()
        return sequences


###############################################################################
# Sequence functions
###############################################################################


def _set_gene_product(genes: Dict[str, ParseGene], id_: str, product: str) -> None:
    genes[id_].product = product


class GeneParser:
    def __init__(self, path: Path) -> None:
        file, start_idx = _open_file_and_remove_comments(path)
        self.file = file
        self.start_idx = start_idx

        self.actions: Dict[str, Callable[[Any, Any, Any], None]] = {
            "DBLINKS": _add_database_link,
            "PRODUCT": _set_gene_product,
        }

    def parse(self) -> Dict[str, Monomer]:
        genes: Dict[str, ParseGene] = {}
        for line in self.file:
            if any(line.startswith(i) for i in MALFORMED_LINE_STARTS):
                continue
            identifier, content = line.rstrip().split(" - ", maxsplit=1)
            if identifier == "UNIQUE-ID":
                id_ = content
                genes[content] = ParseGene(id=content)
            else:
                self.actions.get(identifier, _do_nothing)(genes, id_, content)
        return {
            product: Monomer(id=product, gene=i.id, database_links=i.database_links)
            for i in genes.values()
            if (product := i.product) is not None
        }
