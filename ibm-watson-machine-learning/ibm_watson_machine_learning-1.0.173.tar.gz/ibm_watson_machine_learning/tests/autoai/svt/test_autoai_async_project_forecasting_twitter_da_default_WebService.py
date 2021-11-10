#  (C) Copyright IBM Corp. 2021.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import unittest

import ibm_boto3
from ibm_watson_machine_learning.experiment import AutoAI
from ibm_watson_machine_learning.helpers.connections import DataConnection, S3Location
from ibm_watson_machine_learning.utils.autoai.errors import WMLClientError
from ibm_watson_machine_learning.tests.utils import bucket_exists, create_bucket, is_cp4d
from ibm_watson_machine_learning.tests.autoai.abstract_tests_classes import AbstractTestTSAsync, \
    AbstractTestWebservice

from ibm_watson_machine_learning.utils.autoai.enums import PredictionType, Metrics


class TestAutoAIRemote(AbstractTestTSAsync, unittest.TestCase):
    """
    The test can be run on Cloud only
    """

    cos_resource = None
    data_location = './autoai/data/Twitter_volume_AMZN.csv'

    data_cos_path = 'Twitter_volume_AMZN.csv'

    batch_payload_location = data_location
    batch_payload_cos_location = data_cos_path

    SPACE_ONLY = False
    BATCH_DEPLOYMENT = False

    OPTIMIZER_NAME = "Twitter_volume_AMZN test sdk"
    DEPLOYMENT_NAME = OPTIMIZER_NAME + "Deployment"

    target_space_id = None

    experiment_info = dict(
        name=OPTIMIZER_NAME,
        prediction_type=PredictionType.FORECASTING,
        prediction_columns=['value'],
        timestamp_column_name='timestamp',
        backtest_num=4,
        lookback_window=5,
        forecast_window=2,
        holdout_size=0.05,
        max_number_of_estimators=1
    )

    def test_00d_prepare_data_asset(self):
        asset_details = self.wml_client.data_assets.create(
            name=self.data_location.split('/')[-1],
            file_path=self.data_location)

        TestAutoAIRemote.asset_id = self.wml_client.data_assets.get_id(asset_details)
        self.assertIsInstance(self.asset_id, str)

    def test_02_data_reference_setup(self):
        TestAutoAIRemote.data_connection = DataConnection(data_asset_id=self.asset_id)
        TestAutoAIRemote.results_connection = None

        self.assertIsNotNone(obj=TestAutoAIRemote.data_connection)
        self.assertIsNone(obj=TestAutoAIRemote.results_connection)

    def test_99_delete_data_asset(self):
        if not self.SPACE_ONLY:
            self.wml_client.set.default_project(self.project_id)

        self.wml_client.data_assets.delete(self.asset_id)

        with self.assertRaises(WMLClientError):
            self.wml_client.data_assets.get_details(self.asset_id)


if __name__ == '__main__':
    unittest.main()
