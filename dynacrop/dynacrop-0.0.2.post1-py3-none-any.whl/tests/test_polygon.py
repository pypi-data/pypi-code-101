from typing import Iterator
import pytest

from dynacrop import Polygon


@pytest.mark.parametrize(
    'path, apiobject_type', [
        ('mocked_polygon_data.json', Polygon)
    ],
)
def test_correct_instance(example_apiobject, apiobject_type):
    assert isinstance(example_apiobject, apiobject_type)


@pytest.mark.parametrize(
    'path, apiobject_type',
    [
        ('mocked_polygon_data.json', Polygon)
    ]
)
def test_apiobject_has_id(example_apiobject):
    assert example_apiobject.id


@pytest.mark.parametrize('path, apiobject_type', [
    ('mocked_polygon_data.json', Polygon)]
)
@pytest.mark.parametrize('noneditable_attr', [
    'id',
    'geometry',
    'area',
    'last_valid_observation',
    'valid_observations',
    'cloud_cover_percent',
    'last_updated']
)
def test_polygon_noneditable_attrs(
    example_apiobject,
    noneditable_attr
):
    with pytest.raises(AttributeError):
        setattr(example_apiobject, noneditable_attr, 'nonsense')


# @pytest.mark.parametrize(
#     'polygon_attr, attr_value',
#     zip(
#         Polygon._editable_attrs,
#         [True, 0.8, '[CHANGED LABEL] DynaCrop SDK Polygon for tests']
#     )
# )
# def test_polygon_editable_attrs(example_polygon, polygon_attr, attr_value):
#     setattr(example_polygon, polygon_attr, attr_value)


# def test_list_polygons(polygons_list):
#     assert isinstance(polygons_list, Iterator)


# def test_list_polygons_correct_results(polygons_list):
#     assert all([isinstance(p, Polygon) for p in polygons_list])
