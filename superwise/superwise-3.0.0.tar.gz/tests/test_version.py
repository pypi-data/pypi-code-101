import json
import os
import sys
from datetime import datetime
from pprint import pprint

import pandas as pd
import pytest
import requests

from superwise import Superwise
from superwise.controller.exceptions import *
from superwise.controller.summary.entities_validator import EntitiesValidationError
from superwise.models.data_entity import DataEntity
from superwise.models.data_entity import DataEntityCollection
from superwise.models.task import Task
from superwise.models.version import Version
from superwise.resources.superwise_enums import DataTypesRoles
from superwise.resources.superwise_enums import FeatureType
from superwise.resources.superwise_enums import TaskTypes
from tests import config
from tests import get_entities_fixture
from tests import get_sw


def get_entities_fixture(path="tests/resources/basic_schema.json"):
    with open(path, "r") as fh:
        schema = json.loads(fh.read())

    entities = [
        DataEntity(
            dimension_start_ts=m.get("dimension_start_ts", None),
            name=m["name"],
            type=m["type"],
            role=m["role"],
            feature_importance=None,
        )
        for m in schema
    ]
    return entities


@pytest.mark.vcr()
def test_dataentity_creation_unit():
    entities = DataEntity(
        dimension_start_ts=None,
        name="barak",
        type=FeatureType.CATEGORICAL,
        role=DataTypesRoles.LABEL,
        feature_importance=None,
    )

    assert entities.type == FeatureType.CATEGORICAL.value
    assert entities.role == DataTypesRoles.LABEL.value

    entities = DataEntity(
        dimension_start_ts=None,
        name="barak",
        type=FeatureType.CATEGORICAL.value,
        role=DataTypesRoles.LABEL.value,
        feature_importance=None,
    )
    assert entities.type == FeatureType.CATEGORICAL.value
    assert entities.role == DataTypesRoles.LABEL.value


@pytest.mark.vcr()
def test_create_version():
    entities = get_entities_fixture()

    sw = get_sw()
    for e in entities:
        print(e.get_properties())
    versionExternal = Version(
        task_id=1,
        version_name="test version",
        external_id=None,
        baseline_files=["gs://superwise-tools/integration_tests/basic/baseline_meta.parquet"],
        data_entities=entities,
    )
    model = sw.version.create(versionExternal)


@pytest.mark.vcr()
def test_get_unknown_version():
    sw = get_sw()
    ok = False
    print("before")
    try:
        model = sw.version.get_by_id(0)
    except requests.exceptions.HTTPError:
        ok = True
    print("after")
    assert ok is True


@pytest.mark.vcr()
def test_get_version():
    sw = get_sw()
    model = sw.version.get_by_id(1)
    assert model.id == 1


@pytest.mark.vcr()
def test_get_version_activate():
    sw = get_sw()
    sw.version.activate(1)


@pytest.mark.vcr()
def test_get_version_dataentities():
    sw = get_sw()
    model = sw.version.get_data_entities(3)
    # assert model.type == "a"


@pytest.mark.vcr()
def test_create_from_df_bool_test():
    sw = get_sw()
    entites = get_entities_fixture("tests/resources/internal_sdk/basic_schema.json")
    entities_collection = DataEntityCollection(entites)

    task_id = 1
    df = pd.read_json("tests/resources/internal_sdk/data_bool.json")

    version_model = Version(
        task_id=task_id, version_name="test version", external_id=None, baseline_files=[], data_entities=entites
    )
    task = sw.task.get_by_id(1)
    # FIXME - move data_df to version object
    versionExternal = Version(
        task_id=1,
        baseline_df=df,
        version_name="test version 1",
        external_id=None,
        baseline_files=[],
        data_entities=entites,
    )
    model = sw.version.create(versionExternal, wait_until_complete=True)


@pytest.mark.vcr()
def test_create_from_df():
    sw = get_sw()
    entites = get_entities_fixture("tests/resources/internal_sdk/basic_schema.json")
    entities_collection = DataEntityCollection(entites)

    task_id = 1
    df = pd.read_json("tests/resources/internal_sdk/data.json")
    print(df)
    version_model = Version(
        task_id=task_id, version_name="test version", external_id=None, baseline_files=[], data_entities=entites
    )
    task = sw.task.get_by_id(1)

    ## fixme example of load
    base_version = Version(id=1, status="SUMMARIZED")
    entites[0].name = "est_country_name_change"
    df = df.rename(columns={"est_country": "est_country_name_change"})
    # FIXME - move data_df to version object
    versionExternal = Version(
        task_id=1,
        baseline_df=df,
        version_name="test version 1",
        external_id=None,
        baseline_files=[],
        data_entities=entites,
    )
    sw.version.create(versionExternal, base_version=base_version, wait_until_complete=True)


@pytest.mark.vcr()
def test_create_from_df_to_much_dimension():
    sw = get_sw()
    os.environ["MAX_DIMENSIONS"] = "5"

    entites = get_entities_fixture("tests/resources/internal_sdk/basic_schema_too_much_dimension.json")
    entities_collection = DataEntityCollection(entites)

    task_id = 1
    df = pd.read_json("tests/resources/internal_sdk/data.json")
    print(df)
    version_model = Version(
        task_id=task_id, version_name="test version", external_id=None, baseline_files=[], data_entities=entites
    )
    task = sw.task.get_by_id(1)

    ## fixme example of load
    base_version = Version(id=2, status="SUMMARIZED")

    ok = False
    versionExternal = Version(
        task_id=1,
        baseline_df=df,
        version_name="test version 1",
        external_id=None,
        baseline_files=[],
        data_entities=entites,
    )
    try:
        model = sw.version.create(versionExternal, base_version=base_version, wait_until_complete=True)
    except EntitiesValidationError:
        ok = True
    assert ok == True


@pytest.mark.vcr()
def test_base_version_not_summarized_version():
    return
    # fixme - not ussing gcp storage for CICD
    client = get_sw()

    task = client.task.create(
        Task(title="test", task_description="test", task_type=TaskTypes.BINARY_CLASSIFICATION, monitor_delay=1)
    )

    print(task.id)

    baseline_data = pd.read_parquet("gs://superwise-tools/integration_tests/basic/baseline_meta.parquet")
    schema = pd.read_json("/Users/barakbloch/dev/note/or/basic.json").to_dict(orient="records")

    entities = [
        DataEntity(
            name=m["name"],
            type=m["type"],
            dimension_start_ts=m["dimension_start_ts"],
            role=m["role"],
            feature_importance=None,
        )
        for m in schema
    ]

    first_version = Version(
        task_id=task.id,
        baseline_df=baseline_data,
        version_name="v1",
        external_id=None,
        baseline_files=[],
        data_entities=entities,
    )
    first_version = client.version.create(first_version)

    client.version.activate(first_version.id)

    ## Create second version
    baseline_data = pd.read_parquet("gs://superwise-tools/integration_tests/basic/baseline_meta.parquet")
    baseline_data = baseline_data.rename(columns={"f34": "f_new"})
    schema = pd.read_json("/Users/barakbloch/dev/note/or/basic.json")
    schema.loc[schema["name"] == "f34", "name"] = "f_new"
    schema = schema.to_dict(orient="records")
    entities = [
        DataEntity(
            name=m["name"],
            type=m["type"],
            dimension_start_ts=m["dimension_start_ts"],
            role=m["role"],
            feature_importance=None,
        )
        for m in schema
    ]

    second_version = Version(
        task_id=task.id,
        baseline_df=baseline_data,
        version_name="v2",
        external_id=None,
        baseline_files=[],
        data_entities=entities,
    )
    ok = False
    try:
        model = client.version.create(second_version, base_version=first_version)
    except SuperwiseValidationException:
        ok = True
    assert ok == True
