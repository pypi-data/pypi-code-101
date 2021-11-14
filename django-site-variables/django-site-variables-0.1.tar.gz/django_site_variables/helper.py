import typing
from typing import Union, Optional

from django_site_variables.models import SiteVariable


def __get_first(list_: list, default):
    return list_[0] if len(list_) else default


def _cast_value(value: str) -> Union[str, int, bool]:
    if value.isnumeric():
        return int(value)
    elif value.lower() == 'true':
        return value.lower() == 'true'
    else:
        return value


def get_site_variable(name: str, default=None) -> Optional[Union[str, int, bool]]:
    try:
        value = SiteVariable.objects.values_list('content', flat=True).get(name=name)
        return _cast_value(value)
    except SiteVariable.DoesNotExist:
        return default


def set_site_variable(name: str, value: Union[str, int, bool]):
    value_type = __get_first([v for tp, v in {
        str: SiteVariable.TYPE_TEXT,
        int: SiteVariable.TYPE_NUMBER,
        bool: SiteVariable.TYPE_BOOLEAN,
    } if isinstance(value, tp)], SiteVariable.TYPE_TEXT)

    return SiteVariable.objects.create(name=name, value=str(value), value_type=value_type)


def get_many_site_variables(*names) -> dict:
    values = SiteVariable.objects.values_list('name', 'content').filter(name__in=names)
    return {k: _cast_value(v) for k, v in dict(values).items()}