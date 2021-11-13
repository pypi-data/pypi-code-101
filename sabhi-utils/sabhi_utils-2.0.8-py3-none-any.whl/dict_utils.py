
def merge_list_of_dicts(
    list_of_dicts=None
):

    return {
        k: v for x in list_of_dicts for k, v in x.items()
    }


def sum_list_of_dicts(
    list_of_dicts=None,
    keys=None
):
    result = dict.fromkeys(keys, None)
    for key in keys:
        result[key] = sum(
            item.get(key, 0) for item in list_of_dicts
        )

    return result

def average_list_of_dicts(
    list_of_dicts=None,
    keys=None
):
    result = dict.fromkeys(keys, None)
    no_samples = len(list_of_dicts)
    for key in keys:
        result[key] = sum(
            item.get(key, 0) for item in list_of_dicts
        )/no_samples

    return result



if __name__ == "__main__":
    l = [
        {'a': 0, 'f': 10}, {'a': 1}, {'a': 3}, {'e': 4, 'a': 4}]

    print(merge_list_of_dicts(l))

    print(
        average_list_of_dicts(
            l,
            keys = ['a','f']
        )
    )
