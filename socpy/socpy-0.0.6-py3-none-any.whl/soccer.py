from .request import soccer_req
from .response import coalesce_results, soccer_enrich, soccer_resp
from .utils import map_dict, recycle_args

class SOCcer:
    """
    A class for handling SOCcer API results
    """
    def __init__(self, problems, valid):
        if problems.empty:
            self.problems = None
        else:
            self.problems = problems
        if valid.empty:
            self.valid = None
        else:
            self.valid = valid

def soccer_engine(job_title, job_desc = None, industry = None, n_results = 10, **kwargs):
    request = soccer_req(
        job_title = job_title,
        job_desc = job_desc,
        industry = industry,
        n_results = n_results
    )
    response = soccer_resp(request)
    enriched = soccer_enrich(
        resp = response,
        **kwargs
    )
    return enriched

def soccer(job_title, job_desc = None, industry = None, n_results = 10, **kwargs):
    fun_args = recycle_args(
        job_title = job_title, 
        job_desc = job_desc,
        industry = industry,
        n_results = n_results,
        **kwargs
    )
    tst = map_dict(fun = soccer_engine, **fun_args)
    tst_coalesce = coalesce_results(tst)
    return SOCcer(tst_coalesce['problems'], tst_coalesce['valid'])
