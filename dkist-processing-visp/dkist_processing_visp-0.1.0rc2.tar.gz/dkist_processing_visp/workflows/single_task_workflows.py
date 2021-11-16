from dkist_processing_core import Workflow

from dkist_processing_visp.tasks.dark import DarkCalibration
from dkist_processing_visp.tasks.instrument_polarization import InstrumentPolarizationCalibration
from dkist_processing_visp.tasks.lamp import LampCalibration
from dkist_processing_visp.tasks.parse import ParseL0VispInputData
from dkist_processing_visp.tasks.science import ScienceCalibration

dark_workflow = Workflow(process_category="visp", process_name="dark", workflow_package=__package__)
dark_workflow.add_node(task=DarkCalibration, upstreams=None)

lamp_gain_workflow = Workflow(
    process_category="visp", process_name="lamp_gain", workflow_package=__package__
)
lamp_gain_workflow.add_node(task=LampCalibration, upstreams=None)

inst_polcal_workflow = Workflow(
    process_category="visp", process_name="inst_polcal", workflow_package=__package__
)
inst_polcal_workflow.add_node(task=InstrumentPolarizationCalibration, upstreams=None)

inst_polcal_workflow = Workflow(
    process_category="visp", process_name="science", workflow_package=__package__
)
inst_polcal_workflow.add_node(task=ScienceCalibration, upstreams=None)

parse_workflow = Workflow(
    process_category="visp", process_name="parse_inputs", workflow_package=__package__
)
parse_workflow.add_node(task=ParseL0VispInputData, upstreams=None)
