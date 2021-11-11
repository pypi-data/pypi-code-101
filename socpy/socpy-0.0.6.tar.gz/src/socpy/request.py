from requests import get
from urllib.parse import quote

def quote_str_int(val):
    if not (isinstance(val, str) or isinstance(val, int) or isinstance(val, None)):
        raise TypeError
    if isinstance(val, str):
        return quote(val)
    return val

def soccer_req(job_title, job_desc, industry, n_results):
    req = get(
        url = url_query(
            "https://sitf-raft3imjaq-uc.a.run.app/soccer/code",
            title = job_title,
            task = job_desc,
            industry = industry,
            n = n_results
        )
    )
    return req

def url_query(url, **kwargs):
    if not isinstance(url, str):
        raise ValueError("Argument 'url' must be a string")
    url = url.strip("\/")
    if not kwargs:
        return url
    else:
        query_ls = [f"{x}={quote_str_int(kwargs[x])}" for x in kwargs if kwargs[x]]
        url = f"{url}?{'&'.join(query_ls)}"
        return url