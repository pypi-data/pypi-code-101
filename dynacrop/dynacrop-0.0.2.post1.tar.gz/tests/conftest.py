import json
import pytest

from dynacrop import Polygon
# from .test_utils import supply_polygon


def get_mocked_data(path):
    with open(path) as md:
        return json.load(md)


@pytest.fixture(autouse=True)
def refresh_mocker(mocker):
    mocker.patch(
        'dynacrop.api_handles.APIObject.refresh',
        return_value=None
    )


@pytest.fixture(autouse=True)
def get_mocker(mocker, path):
    mocker.patch(
        'dynacrop.api_handles.RequestsHelper.get',
        return_value=get_mocked_data(path)
    )


@pytest.fixture(autouse=True)
def patch_mocker(mocker):
    mocker.patch(
        'dynacrop.api_handles.RequestsHelper.patch',
        return_value=None
    )


@pytest.fixture()
def example_apiobject(apiobject_type):
    return apiobject_type.get(1)


# @pytest.fixture
# def example_polygon(mocker):
#     mocker.patch(
#         'dynacrop.api_handles.RequestsHelper.get',
#         return_value=get_mocked_data('mocked_polygon_data.json')
#     )
#     mocker.patch(
#         'dynacrop.api_handles.RequestsHelper.patch',
#         return_value=None
#     )
#     return Polygon.get(1)


# @pytest.fixture
# def polygons_list(mocker):
#     mocker.patch(
#         'dynacrop.api_handles.RequestsHelper.get',
#         return_value=get_mocked_data('mocked_list_polygons.json')
#     )
#     mocker.patch(
#         'dynacrop.api_handles.APIObject.refresh',
#         return_value=None
#     )
#     return Polygon.list()

# @pytest.fixture
# def deleted_polygon(mocker):
