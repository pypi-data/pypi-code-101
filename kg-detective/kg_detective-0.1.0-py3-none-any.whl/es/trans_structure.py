from spacy.language import Language 
from spacy.tokens import Doc

def _analyze(doc, t, structure):
  dep = doc[t["element"]].dep_
  explanation = dep
  t["explanation"] = explanation
  return t

def es_trs(doc, structure):
  structure_with_explanation = []
  for t in structure:
    _t = _analyze(doc, t, structure)
    structure_with_explanation.append(_t)
  return structure_with_explanation
