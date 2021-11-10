from quinella.dimensions import to_flat_exacta,from_flat_exacta,to_flat_quinella, from_flat_quinella
from quinella.normalization import to_normalized_dividends, to_normalized_probabilities


def to_normalized_quinella_probabilities(q,scr=-1):
    """
    :param q: 2-d representation
    :param scr:
    :return: 2-d representation
    """
    fq = to_normalized_probabilities( to_flat_quinella(q), scr=scr )
    return from_flat_quinella(fq, diag_val=0)


def to_normalized_quinella_dividends(q,scr=-1):
    """ Convert 2-d representation of probabilities to dividends
    :param q:
    :param scr:
    :return:
    """
    fd = to_normalized_dividends( to_flat_quinella(q), scr=scr )
    return from_flat_quinella(fd, diag_val=-1)


def to_normalized_exacta_probabilities(x,scr=-1):
    """
    :param x: 2-d representation
    :param scr:
    :return: 2-d representation
    """
    fx = to_normalized_probabilities( to_flat_exacta(x), scr=scr )
    return from_flat_exacta(fx, diag_value=0)


def to_normalized_exacta_dividends(x,scr=-1):
    """ Convert 2-d representation of probabilities to dividends
    :param x:
    :param scr:
    :return:
    """
    fx = to_normalized_dividends( to_flat_exacta(x), scr=scr )
    return from_flat_exacta(fx, diag_value=scr)





