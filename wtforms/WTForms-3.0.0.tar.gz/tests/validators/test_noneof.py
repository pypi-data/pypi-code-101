import pytest

from wtforms.validators import NoneOf


def test_none_of_passes(dummy_form, dummy_field):
    """
    it should pass if the value is not present in list
    """
    dummy_field.data = "d"
    validator = NoneOf(["a", "b", "c"])
    validator(dummy_form, dummy_field)


def test_none_of_raises(dummy_form, dummy_field):
    """
    it should raise ValueError if the value is present in list
    """
    dummy_field.data = "a"
    validator = NoneOf(["a", "b", "c"])
    with pytest.raises(ValueError):
        validator(dummy_form, dummy_field)
