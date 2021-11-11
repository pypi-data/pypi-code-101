from . import core
import copy


def publications_from_query(query:str):
	complete_var_dict = {}
	var_models = core.variation_search(query)
	for model in var_models:
		complete_var_dict[model.rsid] = complete_var_dict.get(model.rsid, {"hgvs": None, "pmids": set()})
		complete_var_dict[model.rsid]["hgvs"] = model.hgvs

	var_rsids = map(lambda x: x.rsid, var_models)
	pmid_models = core.pmids_by_rsids(list(var_rsids))

	for pmid_list in pmid_models:
		for pmid in pmid_list.pmids:
			complete_var_dict[pmid_list.rsid]["pmids"].add(pmid)

	return complete_var_dict

