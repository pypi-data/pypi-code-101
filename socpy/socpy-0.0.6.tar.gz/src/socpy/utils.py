def map_dict(fun, **kwargs):
    lens = [len(kwargs[x]) for x in kwargs]
    if not all(x == lens[0] for x in lens):
        raise ValueError("All arguments must be lists of equal lengths")
    out_list = []
    for i in range(lens[0]):
        arg_dict = {x[0]: x[1][i] for x in kwargs.items()}
        out_list.append(fun(**arg_dict))
    return out_list

def recycle_args(**kwargs):
    kwargs = wrap_args(**kwargs)
    lens = [len(kwargs[x]) for x in kwargs]
    max_len = max(lens)
    if not all([x in [1, max_len] for x in lens]):
        raise ValueError(f"All arguments must be either length 1 or {max_len}")
    out_dict = dict()
    for i in kwargs:
        if len(kwargs[i]) == max_len:
            out_dict[i] = kwargs[i]
        else:
            out_dict[i] = kwargs[i] * max_len
    return out_dict

def wrap_args(**kwargs):
    out_dict = dict()
    for i in kwargs:
        if isinstance(kwargs[i], list):
            out_dict[i] = kwargs[i]
        else:
            out_dict[i] = [kwargs[i]]
    return out_dict