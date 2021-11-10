import json
import sys
from pprint import pprint

import pytest

from superwise import Superwise
from superwise.controller.exceptions import *
from superwise.models.task import Task
from superwise.resources.superwise_enums import TaskTypes
from tests import config
from tests import get_sw
from tests import print_results

task_id = None


@pytest.mark.vcr()
def test_create_task_inline():
    sw = get_sw()
    inline_model_test = sw.task.create(
        Task(
            task_type=TaskTypes.BINARY_CLASSIFICATION,
            title="inline title",
            task_description="inline tesk description",
            monitor_delay=1,
        )
    )

    print_results("created task object 1", inline_model_test.get_properties())
    assert inline_model_test.title == "inline title"


@pytest.mark.vcr()
def test_create_task():
    sw = get_sw()
    model = Task()
    global task_id
    model.task_type = TaskTypes.BINARY_CLASSIFICATION.value
    model.title = "this is test title"
    model.task_description = "description"
    model.monitor_delay = 0
    model.ongoing_label = 12
    model.title = "this is test title"
    new_task_model = sw.task.create(model)
    print_results("created task object 2", new_task_model.get_properties())
    assert new_task_model.title == "this is test title"
    assert new_task_model.task_description == "description"
    task_id = new_task_model.id


@pytest.mark.vcr()
def test_get_task():
    sw = get_sw()
    global task_id
    print(task_id)
    model = sw.task.get_by_id(task_id)
    assert int(model.id) == task_id


@pytest.mark.vcr()
def test_create_incomplete_input():
    sw = get_sw()
    model = Task()
    ok = False
    try:
        ok = True
        model = sw.task.create(model)
    except SuperwiseValidationException as e:
        assert ok == True
        pprint(e)
    print(model.get_properties())
    ok2 = False
    try:
        new_inline = sw.task.create(
            Task(title="inline title", task_description="inline tesk description", monitor_delay=1)
        )
    except SuperwiseValidationException as e:
        pprint(e)
        ok2 = True
    assert ok2 == True
