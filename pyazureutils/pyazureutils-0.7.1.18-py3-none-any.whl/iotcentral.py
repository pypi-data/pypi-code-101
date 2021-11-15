"""
Azure IoT Central functions
"""
import subprocess
import json
import shutil
from logging import getLogger
from datetime import datetime
from requests import Session
from requests import codes


class AzureIotCentralSession:
    """
    Session handling for Azure IoT Central
    """
    def __init__(self, subscription=None):
        self.logger = getLogger(__name__)
        self.management_headers = None
        self.apps_headers = None
        self.management_session = None
        self.apps_session = None
        self.params = None
        self.management_token = None
        self.iotcentral_app_token = None
        self.subscription = subscription
        self.az_cmd = shutil.which("az")
        if not self.az_cmd:
            raise Exception("Azure CLI (az) not found.")
        else:
            self.logger.debug("Found Azure CLI in %s", )

    def connect(self):
        """Connect to Azure services by creating access tokens.

        :raises Exception: If no access tokens could be created.
        """
        if not self.management_token or not self._is_token_valid(self.management_token):
            self._az_login()
        self.management_token = self._az_get_resource_management_token(self.subscription)
        self.iotcentral_app_token = self._az_get_iotcentral_app_access_token()

        if not self.iotcentral_app_token or not self.management_token:
            raise Exception("Apps token could not be retrieved")

        self.apps_session = Session()
        self.params = {"api-version":"1.0"}
        self.management_headers = {"Authorization": "Bearer {}".format(self.management_token['accessToken'])}
        self.apps_headers = {"Authorization": "Bearer {}".format(self.iotcentral_app_token['accessToken'])}

    def _is_token_valid(self, auth_token):
        """ Check if a local token is valid """
        if datetime.utcnow() > datetime.strptime(auth_token['expiresOn'], '%Y-%m-%d %H:%M:%S.%f'):
            return False
        return True

    def _az_get_resource_management_token(self, subscription=None):
        """ Retrieve access tokens from Azure account using CLI """
        cmd = [self.az_cmd, "account", "get-access-token"]
        if subscription:
            cmd += ["--subscription", f"{subscription}"]
        process = subprocess.run(cmd, shell=False, stdout=subprocess.PIPE, universal_newlines=True, check=True)
        if process.returncode:
            self.logger.error("Unable to run Azure CLI")
            self.logger.debug("Stdout returned: %s", process.stdout)
            raise Exception("AZ CLI not installed, or inaccessible!")
        token = json.loads(process.stdout)
        self.logger.debug("Azure resource management token collected:")
        self.logger.debug("Type: %s", token['tokenType'])
        self.logger.debug("Tenant: %s", token['tenant'])
        self.logger.debug("Subscription: %s", token['subscription'])
        self.logger.debug("Expires: %s", token['expiresOn'])
        return token

    def _az_get_iotcentral_app_access_token(self):
        """ Retrieve iotcentral app access token from Azure account using CLI """
        process = subprocess.run([self.az_cmd, "account", "get-access-token", "--resource",
                                  "https://apps.azureiotcentral.com"],
                                 shell=False, stdout=subprocess.PIPE, universal_newlines=True, check=True)
        if process.returncode:
            self.logger.error("Unable to run Azure CLI")
            self.logger.debug("Stdout returned: %s", process.stdout)
            raise Exception("AZ CLI not installed, or inaccessible!")

        token = json.loads(process.stdout)
        self.logger.debug("Apps token collected:")
        self.logger.debug("Type: %s", token['tokenType'])
        self.logger.debug("Tenant: %s", token['tenant'])
        self.logger.debug("Subscription: %s", token['subscription'])
        self.logger.debug("Expires: %s", token['expiresOn'])
        return token

    def _check_all_token_validity(self, tokens):
        """ Filter tokens by validity """
        valid_tokens = []
        for token in tokens:
            if self._is_token_valid(token):
                valid_tokens.append(token)
            else:
                self.logger.debug("Expired token")

        return valid_tokens

    def _az_login(self):
        """ Login to Azure using CLI """
        self.logger.info("Logging in using 'az login'")
        process = subprocess.run([self.az_cmd, "login"], shell=False, check=True)
        if process.returncode:
            self.logger.error("Unable to run Azure CLI")
            raise Exception("AZ CLI not installed, or inaccessible!")

    def az_cli_command(self, command):
        """ Execute an Azure CLI command """
        cmd = command.split(' ')
        # add absolute path for az command instead
        cmd[0] = self.az_cmd
        process = subprocess.run(cmd, shell=False, stdout=subprocess.PIPE,
                                 universal_newlines=True, check=True)
        if process.returncode:
            self.logger.error("Unable to run Azure CLI")
            raise Exception("AZ CLI not installed, or inaccessible!")
        return process.stdout

    def az_rest_get(self, url):
        """ Make a rest-api GET call to Azure IoTCentral"""
        if "api-version" in url:
            params = {}
        else:
            params = self.params

        if "management.azure" in url:
            return self.management_session.get(url=url, headers=self.management_headers, params=params).json()
        return self.apps_session.get(url=url, headers=self.apps_headers, params=params).json()

    def az_rest_put(self, url, json_content=None):
        """ Make a rest-api PUT call to Azure IoTCentral"""
        if "api-version" in url:
            params = {}
        else:
            params = self.params

        if "management.azure" in url:
            response = self.management_session.put(url=url, headers=self.management_headers,
                                                   params=params, json=json_content)
        else:
            response = self.apps_session.put(url=url, headers=self.apps_headers, params=params, json=json_content)

        if response.status_code != codes['ok']:
            self.logger.debug(response.content)
            raise Exception("Invalid response from IoTCentral")

        return response


class AzureIotCentral:
    """
    Wrapper for interaction with Azure IoT Central
    """
    def __init__(self, session, app_name):
        self.logger = getLogger(__name__)
        self.session = session
        self.app_name = app_name

    def set_app_name(self, app_name):
        """ Set the app name """
        self.app_name = app_name

    # az commands using subprocess
    def list_applications(self):
        """ List applications using AZ CLI """
        self.logger.info("Retrieving application list")
        cmd = 'az iot central app list'
        apps = self.session.az_cli_command(cmd)
        return json.loads(apps)

    def get_admin_role_id(self):
        """ Retrieve admin role from AZ CLI """
        self.logger.info("Retrieving admin role ID")
        cmd = f"az rest -m get -u https://{self.app_name}.azureiotcentral.com/api/roles "\
        "--url-parameters api-version=1.0 "\
        " --resource https://apps.azureiotcentral.com --query value[?displayName=='Administrator'].id -o tsv"
        role_id = self.session.az_cli_command(cmd)
        return role_id.strip()

    def get_operator_role_id(self):
        """ Retrieve operator role from AZ CLI """
        self.logger.info("Retrieving operator role ID")
        cmd = f"az rest -m get -u https://{self.app_name}.azureiotcentral.com/api/roles "\
        "--url-parameters api-version=1.0 "\
        " --resource https://apps.azureiotcentral.com --query value[?displayName=='Operator'].id -o tsv"
        role_id = self.session.az_cli_command(cmd)
        return role_id.strip()

    # Rest-API calls
    def get_subscriptions(self):
        """ Retrieve subscriptions via REST API call """
        return self.session.az_rest_get("https://management.azure.com/subscriptions?api-version=2021-04-01")

    def get_roles(self):
        """ Retrieve roles via REST API call """
        url = "https://{}.azureiotcentral.com/api/roles".format(self.app_name)
        return self.session.az_rest_get(url)

    def get_device_templates(self):
        """ Retrieve device templates via REST API call """
        url = "https://{}.azureiotcentral.com/api/deviceTemplates".format(self.app_name)
        result = self.session.az_rest_get(url)
        return result

    def get_device_template(self, template_id):
        """Get a device template by ID via REST API call.

        :param template_id: Template ID as defined by the DTDL e.g. dtmi:com:Microchip:PIC_IoT_WM;1 for the
        PIC-IoT Wx. More info here
        https://github.com/Azure/opendigitaltwins-dtdl/blob/master/DTDL/v2/dtdlv2.md#digital-twin-model-identifier
        :type template_id: str
        :return: result of the REST request
        :rtype: str
        """
        url = f"https://{self.app_name}.azureiotcentral.com/api/deviceTemplates/{template_id}"
        result = self.session.az_rest_get(url)
        return result

    def get_users(self):
        """ Retrieve users via REST API call """
        url = "https://{}.azureiotcentral.com/api/users?api-version=1.0".format(self.app_name)
        return self.session.az_rest_get(url)

    def create_device(self, device_id, template, display_name=None):
        """ Creaste device via REST API call """
        url = "https://{}.azureiotcentral.com/api/devices/{}".format(self.app_name, device_id)
        if not display_name:
            display_name = device_id
        device = {
            'displayName': display_name,
            'simulated': False,
            'template': template
        }
        return self.session.az_rest_put(url, json_content=device)

    def get_device(self, device_id):
        """ Retrieve device info via REST API call """
        url = "https://{}.azureiotcentral.com/api/devices/{}?".format(self.app_name, device_id)
        return self.session.az_rest_get(url)

    def get_device_attestation(self, device_id):
        """ Retrieve device attestation via REST API call """
        url = "https://{}.azureiotcentral.com/api/devices/{}/attestation".format(self.app_name, device_id)
        return self.session.az_rest_get(url)

    def create_device_attestation(self, device_id, certificate):
        """ Create device attestation via REST API call """
        url = "https://{}.azureiotcentral.com/api/devices/{}/attestation".format(self.app_name, device_id)
        attestation = {
            "type": "x509",
            "x509": {
                "clientCertificates": {
                    "primary": {
                        "certificate": certificate
                    }
                }
            }
        }
        return  self.session.az_rest_put(url, json_content=attestation)
