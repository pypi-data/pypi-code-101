from spacy.language import Language 
from spacy.tokens import Doc

_d2c = {
  "nsubj": "主语",
  "advmod": "状语",
  "prep": "状语",
  "attr": "表语",
  "dobj": "直接宾语",
  "dative": "间接宾语",
  "advcl": "状语从句",
  "intj": "感叹语",
  "nsubjpass": "主语", 
  "aux": "助动词",
  "neg": "否定词",
  "auxpass": "谓语助词",
  "cc": "连词",
  "preconj": "前置连接",
  #"ccomp": "宾语从句",
  "xcomp": "宾语",
  "acomp": "表语",
}

def _get_root_explanation(doc, r, structure):
  ele = doc[r["element"]]
  deps = [doc[s["element"]].dep_ for s in structure]
  explanation = None
  if ele.pos_ not in ["VERB", "AUX"]:
    explanation = None
  elif any([e in ["attr", "oprd", "acomp"] for e in deps]):  
    explanation = "系动词"
  else:
    explanation = "谓语"
  return explanation

def _get_conj_explanation(doc, c, structure):
  explanation = None
  if c["end"] - c["start"] == 1 and doc[c["element"]].pos_ in ["VERB", "AUX"]:
    explanation = "谓语"
  else:
    explanation = "并列连句"
  return explanation

def _get_oprd_explanation(doc, o, structure):
  ele = doc[o["element"]]
  deps = [doc[s["element"]].dep_ for s in structure]
  explanation = None
  if any([e in ["dobj"] for e in deps]):  
    explanation = "补语"
  else:
    explanation = "表语"
  return explanation

def _get_npadvmod_explanation(doc, t, structure):
  explanation = None
  if t["end"] - t["start"] == 1 and doc[t["element"]].pos_ == "PROPN":
    explanation = "插入语"
  else:
    explanation = "状语"
  return explanation
  
def _analyze(doc, t, structure):
  dep = doc[t["element"]].dep_
  explanation = None
  if dep == "ROOT":
    explanation = _get_root_explanation(doc, t, structure)  
  elif dep == "conj":
    explanation = _get_conj_explanation(doc, t, structure)
  elif dep == "oprd":
    explanation = _get_oprd_explanation(doc, t, structure)
  elif dep == "punct":
    explanation = None
  elif dep == "npadvmod":
    explanation = _get_npadvmod_explanation(doc, t, structure)
  elif dep in _d2c.keys():
    explanation = _d2c[dep]
  else:
    explanation = dep
  t["explanation"] = explanation
  return t

def en_trs(doc, structure):
  structure_with_explanation = []
  for t in structure:
    _t = _analyze(doc, t, structure)
    structure_with_explanation.append(_t)
  return structure_with_explanation
