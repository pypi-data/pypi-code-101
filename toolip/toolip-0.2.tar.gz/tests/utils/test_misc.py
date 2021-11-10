from toolip.utils.misc import get_unique_id


def test_get_unique_id():
    length = 8
    unique_id = get_unique_id(length)
    assert len(unique_id) == length
