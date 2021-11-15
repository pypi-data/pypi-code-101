from random import randint

import numpy as np
import pytest
from astropy.io import fits
from dkist_header_validator import spec214_validator
from dkist_processing_common.models.constants import BudName
from dkist_processing_common.models.tags import Tag
from dkist_processing_common.tests.conftest import FakeGQLClient

from dkist_processing_visp.models.constants import VispBudName
from dkist_processing_visp.tasks.write_l1 import VispWriteL1Frame


@pytest.fixture(scope="function", params=[1, 4])
def write_l1_task(visp_dataset, request):
    with VispWriteL1Frame(
        recipe_run_id=randint(0, 99999),
        workflow_name="workflow_name",
        workflow_version="workflow_version",
    ) as task:
        num_of_stokes_params = request.param
        stokes_params = ["I", "Q", "U", "V"]
        used_stokes_params = []
        hdu = fits.PrimaryHDU(data=np.ones(shape=(128, 128, 1)), header=visp_dataset)
        hdul = fits.HDUList([hdu])
        for i in range(num_of_stokes_params):
            task.fits_data_write(
                hdu_list=hdul,
                tags=[Tag.calibrated(), Tag.frame(), Tag.stokes(stokes_params[i])],
            )
            used_stokes_params.append(stokes_params[i])
        task.constants[BudName.average_cadence.value] = 10
        task.constants[BudName.minimum_cadence.value] = 10
        task.constants[BudName.maximum_cadence.value] = 10
        task.constants[BudName.variance_cadence.value] = 0
        task.constants[BudName.num_dsps_repeats.value] = 1
        task.constants[VispBudName.num_raster_steps.value] = 2
        task.constants[BudName.spectral_line.value] = "VISP Ca II H"
        yield task, used_stokes_params
        task.constants.purge()
        task.scratch.purge()


def test_write_l1_frame(write_l1_task, mocker):
    """
    :Given: a write L1 task
    :When: running the task
    :Then: no errors are raised
    """
    mocker.patch(
        "dkist_processing_common.tasks.mixin.metadata_store.GraphQLClient", new=FakeGQLClient
    )
    task, stokes_params = write_l1_task
    task()
    for stokes_param in stokes_params:
        files = list(task.read(tags=[Tag.frame(), Tag.output(), Tag.stokes(stokes_param)]))
        assert len(files) == 1
        for file in files:
            assert file.exists
            # TODO uncomment this line once the spec catches up
            #  spec214_validator.validate(file, extra=False)
