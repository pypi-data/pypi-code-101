from urllib import request, parse
import certifi
import json
import io


def make_request(href, post_body):
    return_data = None
    href = parse.quote(href, safe="/:?=%")

    req = request.Request(href)
    jsondataasbytes = None
    if post_body is not None:
        req.add_header('Content-Type', 'application/json; charset=utf-8')
        jsondata = json.dumps(post_body)
        jsondataasbytes = jsondata.encode('utf-8')  # needs to be bytes
        req.add_header('Content-Length', str(len(jsondataasbytes)))

    with request.urlopen(req, data=jsondataasbytes, cafile=certifi.where()) as response:
        in_buffer = io.BytesIO()
        in_buffer.write(response.read())
        in_buffer.seek(0)
        text_buffer = io.TextIOWrapper(in_buffer, encoding='utf-8')
        return_data = text_buffer.read()
    return return_data


class Model:
    def __init__(self, **kwargs):
        model_attributes = {'_id', 'name', 'concept', 'id', 'db', 'weight', 'rsid', 'hgvs', 'data', 'links', 'pmids', 'relations'}
        self.__dict__.update((k, v) for k, v in kwargs.items() if k in model_attributes)


# Disambiguation
SEARCH_URL = "https://www.ncbi.nlm.nih.gov/research/bionlp/litvar/api/v1/entity/search/"
INFO_URL = "https://www.ncbi.nlm.nih.gov/research/bionlp/litvar/api/v1/entity/litvar/"


def variation_search(query):
    '''
    Search for all LitVar variants by query search of related concepts
    :param query:  search term. can be gene or variant
    :return:
    '''
    results = json.loads(make_request(SEARCH_URL + query, None))
    models = []
    for result in results:
        new_model = Model(**result)
        models.append(new_model)
    return models


def variation_information(var_id):
    '''
    Return variation information given its VarId
    :param var_id: VarId of the variant
    :return: 
    '''
    results = json.loads(make_request(INFO_URL + var_id, None))
    models = []
    if not isinstance(results, list):
        results = [results]
    for result in results:
        new_model = Model(**result)
        models.append(new_model)
    return models


# Publications
OCCURANCE_URL = "https://www.ncbi.nlm.nih.gov/research/bionlp/litvar/api/v1/public/pmids?"
PMIDS_URL = "https://www.ncbi.nlm.nih.gov/research/bionlp/litvar/api/v1/public/rsids2pmids"


def pmids_by_cooccur_varids(var_ids):
    var_ids_str = str(var_ids).replace("\'", "\"").replace(" ", "")
    var_ids_param = parse.urlencode({"query": var_ids_str})
    csv = make_request(OCCURANCE_URL + var_ids_param, None)
    models = []
    for line in csv.splitlines():
        new_model = Model(pmids=line)
        models.append(new_model)
    return models


def pmids_by_rsids(rs_ids, method="GET"):
    models = []
    if method == "GET":
        rs_id_string = ",".join(rs_ids)
        param = parse.urlencode({'rsids': rs_id_string})
        href = f"{PMIDS_URL}?{param}"
        results = json.loads(make_request(href, None))
        for result in results:
            new_model = Model(**result)
            models.append(new_model)

    elif method == "POST":
        rsid_dict = {"rsids": rs_ids}
        href = PMIDS_URL
        results = json.loads(make_request(href, rsid_dict))
        for result in results:
            new_model = Model(**result)
            models.append(new_model)

    return models


# Relations
RELATIONS_URL = "https://www.ncbi.nlm.nih.gov/research/bionlp/litvar/api/v1/public/relations"


def publications_by_varids(var_ids, unlimited):
    models = []
    var_dict = {"accessions": var_ids, "unlimited": unlimited}
    href = RELATIONS_URL
    results = json.loads(make_request(href, var_dict))
    for result in results:
        new_model = Model(**result)
        models.append(new_model)
    return models