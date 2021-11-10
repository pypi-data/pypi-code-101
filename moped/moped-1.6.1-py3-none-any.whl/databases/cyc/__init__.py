from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Set, Tuple

from ...core.compound import Compound
from ...core.reaction import Monomer, Reaction
from .data import ParseCompound, ParseEnzyme, ParseGene, ParseReaction
from .fix_add_important_cpds import fix_add_important_compounds
from .fix_compartments import fix_create_compartment_variants
from .fix_filter_garbage import fix_filter_garbage_reactions
from .fix_kinetic_data import fix_kinetic_data
from .fix_monomer_annotations import fix_annotate_monomers
from .fix_reaction_variants import fix_create_reaction_variants
from .fix_stoichiometry import fix_set_reaction_stoichiometry
from .fix_unify_reaction_direction import fix_unify_reaction_direction
from .parse import (
    CompoundParser,
    EnzymeParser,
    GeneParser,
    Parser,
    ProteinParser,
    ReactionParser,
    SequenceParser,
)

COMPARTMENT_MAP = {
    "CYTOSOL": "CYTOSOL",
    "IN": "CYTOSOL",
    "UNKNOWN-SPACE": "CYTOSOL",
    "SIDE-1": "CYTOSOL",
    "SIDE-2": "EXTRACELLULAR",
    "EXTRACELLULAR": "EXTRACELLULAR",
    "CHL-THY-MEM": "PERIPLASM",
    "CHLOR-STR": "CYTOSOL",
    "CHROM-STR": "CYTOSOL",
    "GOLGI-LUM": "CYTOSOL",
    "LYS-LUM": "CYTOSOL",
    "MIT-IM-SPC": "CYTOSOL",
    "MIT-IMEM": "PERIPLASM",
    "MIT-LUM": "CYTOSOL",
    "OUTER-MEM": "PERIPLASM",
    "PERI-BAC": "PERIPLASM",
    "PERI-BAC-GN": "PERIPLASM",
    "PERIPLASM": "PERIPLASM",
    "PEROX-LUM": "CYTOSOL",
    "PLASMA-MEM": "PERIPLASM",
    "PLAST-IMEM": "PERIPLASM",
    "PLASTID-STR": "PERIPLASM",
    "PM-ANIMAL": "PERIPLASM",
    "PM-BAC-ACT": "PERIPLASM",
    "PM-BAC-NEG": "PERIPLASM",
    "PM-BAC-POS": "PERIPLASM",
    "RGH-ER-LUM": "CYTOSOL",
    "PM-FUNGI": "PERIPLASM",
    "RGH-ER-MEM": "PERIPLASM",
    "THY-LUM-CYA": "CYTOSOL",
    "VAC-LUM": "CYTOSOL",
    "VAC-MEM": "PERIPLASM",
    "VESICLE": "PERIPLASM",
    "OUT": "PERIPLASM",
    "THY-MEM-CYA": "PERIPLASM",
    "VESICLE-MEM": "PERIPLASM",
}

TYPE_MAP = {
    "ETR-Quinones": "Ubiquinones",
    "ETR-Quinols": "Ubiquinols",
}

COMPARTMENT_SUFFIXES = {
    # Common to all
    "CYTOSOL": "c",
    "EXTRACELLULAR": "e",
    "PERIPLASM": "p",
    "MITOCHONDRIA": "m",
    "PEROXISOME": "x",
    "ER": "r",
    "VACUOLE": "v",
    "NUCLEUS": "n",
    "GOLGI": "g",
    "THYLAKOID": "u",
    "LYSOSOME": "l",
    "CHLOROPLAST": "h",
    "FLAGELLUM": "f",
    "EYESPOT": "s",
    "INTERMEMBRANE": "im",
    "CARBOXYSOME": "cx",
    "THYLAKOID-MEMBRANE": "um",
    "CYTOSOLIC-MEMBRANE": "cm",
    "INNER-MITOCHONDRIA": "i",
    "MITOCHONDRIA-INNER-MEMBRANE": "mm",
    "WILDTYPE": "w",
    "CYTOCHROME-COMPLEX": "y",
}

MANUAL_ADDITIONS = {
    "Acceptor_c": ParseCompound(
        base_id="Acceptor",
        id="Acceptor_c",
        compartment="CYTOSOL",
        charge=0,
        formula={"Unknown": 1},
    ),
    "Donor-H2_c": ParseCompound(
        base_id="Donor-H2",
        id="Donor-H2_c",
        compartment="CYTOSOL",
        charge=0,
        formula={"Unknown": 1, "H": 2},
    ),
    "Oxidized-ferredoxins_c": ParseCompound(
        base_id="Oxidized-ferredoxins",
        id="Oxidized-ferredoxins_c",
        compartment="CYTOSOL",
        charge=1,
        formula={"Unknown": 1},
    ),
    "Reduced-ferredoxins_c": ParseCompound(
        base_id="Reduced-ferredoxins",
        id="Reduced-ferredoxins_c",
        compartment="CYTOSOL",
        charge=0,
        formula={"Unknown": 1},
    ),
    "Red-NADPH-Hemoprotein-Reductases_c": ParseCompound(
        base_id="Red-NADPH-Hemoprotein-Reductases",
        id="Red-NADPH-Hemoprotein-Reductases_c",
        compartment="CYTOSOL",
        charge=0,
        formula={"Unknown": 1, "H": 2},
    ),
    "Ox-NADPH-Hemoprotein-Reductases_c": ParseCompound(
        base_id="Ox-NADPH-Hemoprotein-Reductases",
        id="Ox-NADPH-Hemoprotein-Reductases_c",
        compartment="CYTOSOL",
        charge=0,
        formula={"Unknown": 1},
    ),
    "Cytochromes-C-Oxidized_c": ParseCompound(
        base_id="Cytochromes-C-Oxidized",
        id="Cytochromes-C-Oxidized_c",
        compartment="CYTOSOL",
        charge=1,
        formula={"Unknown": 1},
    ),
    "Cytochromes-C-Reduced_c": ParseCompound(
        base_id="Cytochromes-C-Reduced",
        id="Cytochromes-C-Reduced_c",
        compartment="CYTOSOL",
        charge=0,
        formula={"Unknown": 1},
    ),
    "Oxidized-Plastocyanins_c": ParseCompound(
        base_id="Oxidized-Plastocyanins",
        id="Oxidized-Plastocyanins_c",
        compartment="CYTOSOL",
        charge=1,
        formula={"Unknown": 1},
    ),
    "Plastocyanin-Reduced_c": ParseCompound(
        base_id="Plastocyanin-Reduced",
        id="Plastocyanin-Reduced_c",
        compartment="CYTOSOL",
        charge=0,
        formula={"Unknown": 1},
    ),
    "ETF-Oxidized_c": ParseCompound(
        base_id="ETF-Oxidized",
        id="ETF-Oxidized_c",
        compartment="CYTOSOL",
        charge=1,
        formula={"Unknown": 1},
    ),
    "ETF-Reduced_c": ParseCompound(
        base_id="ETF-Reduced",
        id="ETF-Reduced_c",
        compartment="CYTOSOL",
        charge=2,
        formula={"Unknown": 1, "H": 3},
    ),
    "Ox-Glutaredoxins_c": ParseCompound(
        base_id="Ox-Glutaredoxins",
        id="Ox-Glutaredoxins_c",
        compartment="CYTOSOL",
        charge=1,
        formula={"Unknown": 1},
    ),
    "Red-Glutaredoxins_c": ParseCompound(
        base_id="Red-Glutaredoxins",
        id="Red-Glutaredoxins_c",
        compartment="CYTOSOL",
        charge=0,
        formula={"Unknown": 1},
    ),
    "Ox-Thioredoxin_c": ParseCompound(
        base_id="Ox-Thioredoxin",
        id="Ox-Thioredoxin_c",
        compartment="CYTOSOL",
        charge=0,
        formula={"Unknown": 1},
    ),
    "Red-Thioredoxin_c": ParseCompound(
        base_id="Red-Thioredoxin",
        id="Red-Thioredoxin_c",
        compartment="CYTOSOL",
        charge=0,
        formula={"Unknown": 1, "H": 2},
    ),
    "Ox-FMN-Flavoproteins_c": ParseCompound(
        base_id="Ox-FMN-Flavoproteins",
        id="Ox-FMN-Flavoproteins_c",
        compartment="CYTOSOL",
        charge=1,
        formula={"Unknown": 1},
    ),
    "Red-FMNH2-Flavoproteins_c": ParseCompound(
        base_id="Red-FMNH2-Flavoproteins",
        id="Red-FMNH2-Flavoproteins_c",
        compartment="CYTOSOL",
        charge=0,
        formula={"Unknown": 1, "H": 2},
    ),
    "Ox-FAD-Flavoproteins_c": ParseCompound(
        base_id="Ox-FAD-Flavoproteins",
        id="Ox-FAD-Flavoproteins_c",
        compartment="CYTOSOL",
        charge=1,
        formula={"Unknown": 1},
    ),
    "Red-FADH2-Flavoproteins_c": ParseCompound(
        base_id="Red-FADH2-Flavoproteins",
        id="Red-FADH2-Flavoproteins_c",
        compartment="CYTOSOL",
        charge=0,
        formula={"Unknown": 1, "H": 2},
    ),
    "Light_c": ParseCompound(
        base_id="Light",
        id="Light_c",
        compartment="CYTOSOL",
        charge=0,
        formula={"Unknown": 0},
    ),
    "Oxidized-flavodoxins_c": ParseCompound(
        base_id="Oxidized-flavodoxins",
        id="Oxidized-flavodoxins_c",
        compartment="CYTOSOL",
        charge=0,
        formula={"Unknown": 1},
    ),
    "Reduced-flavodoxins_c": ParseCompound(
        base_id="Reduced-flavodoxins",
        id="Reduced-flavodoxins_c",
        compartment="CYTOSOL",
        charge=0,
        formula={"Unknown": 1, "H": 2},
    ),
}


def _repair(
    parse_compounds: Dict[str, ParseCompound],
    parse_reactions: Dict[str, ParseReaction],
    monomers: Dict[str, Monomer],
    compound_types: Dict[str, List[str]],
    compartment_map: Dict[str, str],
    manual_additions: Dict[str, ParseCompound],
    compartment_suffixes: Dict[str, str],
) -> Tuple[Dict[str, ParseCompound], Dict[str, ParseReaction]]:

    parse_compounds = fix_add_important_compounds(parse_compounds, manual_additions)
    parse_reactions = fix_unify_reaction_direction(parse_reactions)
    parse_reactions = fix_kinetic_data(parse_reactions)
    parse_reactions = fix_annotate_monomers(parse_reactions, monomers)

    # Larger changes
    parse_reactions = fix_create_reaction_variants(parse_reactions, parse_compounds, compound_types)
    parse_reactions = fix_filter_garbage_reactions(parse_reactions, parse_compounds)
    parse_reactions = fix_create_compartment_variants(
        parse_reactions,
        parse_compounds,
        compartment_map,
        compartment_suffixes,
    )
    parse_reactions = fix_set_reaction_stoichiometry(parse_reactions)
    return parse_compounds, parse_reactions


class Cyc:
    def __init__(
        self,
        pgdb_path: Path,
        compartment_map: Dict[str, str] | None,
        type_map: Dict[str, str] | None,
        manual_additions: Dict[str, ParseCompound] | None,
        compartment_suffixes: Dict[str, str] | None,
        parse_sequences: bool = True,
    ) -> None:
        if compartment_map is None:
            compartment_map = COMPARTMENT_MAP
        if type_map is None:
            type_map = TYPE_MAP
        if manual_additions is None:
            manual_additions = MANUAL_ADDITIONS
        if compartment_suffixes is None:
            compartment_suffixes = COMPARTMENT_SUFFIXES

        self.pgdb_path = Path(pgdb_path)
        self.compartment_map = compartment_map
        self.type_map = type_map
        self.parse_sequences = parse_sequences
        self.manual_additions = manual_additions
        self.compartment_suffixes = compartment_suffixes

    def _to_moped(
        self,
        parse_compounds: Dict[str, ParseCompound],
        parse_reactions: Dict[str, ParseReaction],
    ) -> Tuple[list[Compound], list[Reaction], Dict[str, str]]:
        compounds = [
            Compound(
                base_id=v.base_id,
                compartment=v.compartment,
                formula=v.formula,
                charge=v.charge,
                name=v.name,
                gibbs0=v.gibbs0,
                smiles=v.smiles,
                database_links=v.database_links,
                types=v.types,
                id=v.id,
            )
            for v in parse_compounds.values()
        ]
        reactions = [
            Reaction(
                base_id=v.base_id,
                id=v.id,
                stoichiometries=v.stoichiometries,
                compartment=v.compartment,
                name=v.name,
                bounds=v.bounds,
                gibbs0=v.gibbs0,
                ec=v.ec,
                types=v.types,
                pathways=v.pathways,
                sequences=v.sequences,
                monomers=v.monomers_annotated,
                kinetic_data=v.kinetic_data,
                database_links=v.database_links,
                transmembrane=v.transmembrane,
                _var=v._var,
            )
            for v in parse_reactions.values()
        ]
        used_compartments: Set[str] = {i.compartment for i in compounds if i.compartment is not None}
        compartments: Dict[str, str] = {i: self.compartment_suffixes[i] for i in used_compartments}
        return compounds, reactions, compartments

    def _parse(
        self,
    ) -> Tuple[Dict[str, ParseCompound], Dict[str, List[str]], Dict[str, ParseReaction], Dict[str, Monomer]]:
        return Parser(
            pgdb_path=self.pgdb_path,
            compartment_map=self.compartment_map,
            type_map=self.type_map,
            parse_sequences=self.parse_sequences,
        ).parse()

    def parse(self) -> Tuple[list[Compound], list[Reaction], Dict[str, str]]:
        (
            parse_compounds,
            compound_types,
            parse_reactions,
            monomers,
        ) = self._parse()
        parse_compounds, parse_reactions = _repair(
            parse_compounds=parse_compounds,
            parse_reactions=parse_reactions,
            compound_types=compound_types,
            monomers=monomers,
            compartment_map=self.compartment_map,
            manual_additions=self.manual_additions,
            compartment_suffixes=self.compartment_suffixes,
        )
        return self._to_moped(parse_compounds, parse_reactions)
