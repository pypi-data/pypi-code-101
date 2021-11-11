import os
import logging
import unittest

from clamnotif import config, messenger


class MessengerTestCase(unittest.TestCase):

    @unittest.skip("Only test this case if needed")
    def testSendHeartbeat(self):
        mail_content = "Hello, This is a simple mail for Heartbeat Testing"
        messenger.send_heartbeat(mail_content, config.home_config())
        logging.info("Heatbeat Notification Sent!")

    @unittest.skip("Only test this case if needed")
    def testSendAlert(self):
        mail_content = "Hello, This is a simple mail for Alert Testing"
        messenger.send_alert(mail_content, config.home_config())
        logging.info("Alert Notification Sent!")
