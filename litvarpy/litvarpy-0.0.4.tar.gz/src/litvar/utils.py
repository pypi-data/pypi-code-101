from . import core


def publications_from_query(query):
	var_models = core.variation_search(query)
	var_rsids = map(lambda x: x.rsid, var_models)
	pmids = core.pmids_by_rsids(list(var_rsids))
	return pmids

