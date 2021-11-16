from spacy.language import Language 
from spacy.tokens import Doc

def _is_verb_like(e):
  return e.pos_ in ["VERB", "AUX"]

def _has_no_subject(e):
  children_deps = [x.dep_ for x in e.children]
  return all([subj not in children_deps for subj in ["csubj"]])

def _get_predicate_range(p):
  start = p.i
  end  = p.i+1
  return (start, end)

def _get_predicate(doc: Doc, nlp: Language):
  root = [r for r in doc if r.dep_=="ROOT"][0]
  p_conj = [e for e in root.children if e.dep_ == "conj" and _is_verb_like(e) and _has_no_subject(e)]
  predicates = sum([p_conj], [root])

  predicate_info = []
  predicate_related = []

  for p in predicates:
    start, end = _get_predicate_range(p)
    predicate_related.extend(range(start, end))
    _info = {
      "start": start,
      "end": end,
      "text": doc[start:end].text,
      "element": p.i,
      "is_root": True if p.dep_=="ROOT" else False,
    }
    predicate_info.append(_info)
  return (predicate_info, predicate_related)

def get_tree(doc: Doc, nlp: Language):
  store = []

  p_info, p_related = _get_predicate(doc, nlp)
  store.extend(p_info)

  roots = [doc[e["element"]] for e in p_info]
  children = [t for t in sum([list(r.children) for r in roots], []) if t.i not in p_related]

  for dc in children:
    dc_ranges = [e.i for e in dc.subtree]
    start, end = min(dc_ranges), max(dc_ranges)+1
    _info = {
      "start": start,
      "end": end,
      "text": doc[start:end].text,
      "element": dc.i, 
      "is_root": False,
    }
    store.append(_info)

  ordered_store = sorted(store, key=lambda d: d["start"]) 
  return ordered_store 


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
  "aux": "谓语助词",
  "neg": "谓语否定词",
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
