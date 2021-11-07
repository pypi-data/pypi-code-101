# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['pytest_zebrunner', 'pytest_zebrunner.api']

package_data = \
{'': ['*']}

install_requires = \
['PyYAML>=5.3.1,<6.0.0',
 'httpx>=0.15.0,<0.16.0',
 'pydantic>=1.0',
 'pytest>=4.5.0',
 'python-dotenv>=0.10']

entry_points = \
{'pytest11': ['pytest-zebrunner = pytest_zebrunner.plugin']}

setup_kwargs = {
    'name': 'pytest-zebrunner',
    'version': '1.3.2',
    'description': 'Pytest connector for Zebrunner reporting',
    'long_description': '# Zebrunner PyTest agent\n\n\nThe official Zebrunner PyTest agent provides the reporting functionality. It can automatically track Selenium sessions\nand send the info about session details to Zebrunner backend. It can be easily integrated into a project by just installing the library\nand adding the configuration file.\n\nIncluding reporting into your project is easy - just install the agent and provide minimal valid configuration for reporting.\n\n\n## Installation\n\n    pip install pytest-zebrunner\n\n\n## Configuration\nAfter the installation, reporting is disabled by default. It won\'t send any data to the Zebrunner service without a valid configuration.\n\nIt is currently possible to provide the configuration via:\n1. Environment variables\n2. YAML file\n\n`pyproject.toml`, `command arguments` are in plans for future releases.\n\n\n\n<!-- groups:start -->\n### Environment variables\nThe following configuration parameters are recognized by the agent:\n\n- `REPORTING_ENABLED` - enables or disables reporting. The default value is `true`.\n- `REPORTING_SERVER_HOSTNAME` - mandatory if reporting is enabled. It is Zebrunner server hostname. It can be obtained in Zebrunner on the \'Account & profile\' page under the \'Service URL\' section;\n- `REPORTING_SERVER_ACCESS_TOKEN` - mandatory if reporting is enabled. Access token must be used to perform API calls. It can be obtained in Zebrunner on the \'Account & profile\' page under the \'Token\' section;\n- `REPORTING_PROJECT_KEY` - optional value. It is the project that the test run belongs to. The default value is `DEF`. You can manage projects in Zebrunner in the appropriate section;\n- `REPORTING_RUN_DISPLAY_NAME` - optional value. It is the display name of the test run. The default value is `Default Suite`;\n- `REPORTING_RUN_BUILD` - optional value. It is the build number that is associated with the test run. It can depict either the test build number or the application build number;\n- `REPORTING_RUN_ENVIRONMENT` - optional value. It is the environment where the tests will run;\n- `REPORTING_SEND_LOGS` - Sends test logs to Zebrunner. Default: `true`;\n\nAgent also recognizes `.env` file in the resources root folder.\n<!-- groups:end -->\n\n<!-- groups:start -->\n### Yaml file\nAgent recognizes agent.yaml or agent.yml file in the resources root folder. It is currently not possible to configure an alternative file location.\n\nBelow is a sample configuration file:\n```yaml\nreporting:\n  enabled: true\n  project-key: DEF\n  send-logs: true\n  server:\n    hostname: localhost:8080\n    access-token: <token>\n  run:\n    display-name: Nightly Regression Suite\n    build: 1.12.1.96-SNAPSHOT\n    environment: TEST-1\n```\n<!-- groups:end -->\n\n- `reporting.enabled` - enables or disables reporting. The default value is `true`;\n- `reporting.server.hostname` - mandatory if reporting is enabled. Zebrunner server hostname. Can be obtained in Zebrunner on the \'Account & profile\' page under the \'Service URL\' section;\n- `reporting.server.access-token` - mandatory if reporting is enabled. Access token must be used to perform API calls. Can be obtained in Zebrunner on the \'Account & profile\' page under the \'Token\' section;\n- `reporting.project-key` - optional value. The project that the test run belongs to. The default value is `DEF`. You can manage projects in Zebrunner in the appropriate section;\n- `reporting.send-logs` - Sends test logs to Zebrunner. Default: `true`\n- `reporting.run.display-name` - optional value. The display name of the test run. The default value is Default Suite;\n- `reporting.run.build` - optional value. The build number that is associated with the test run. It can depict either the test build number or the application build number;\n- `reporting.run.environment` - optional value. The environment in which the tests will run.\n\nIf the required configurations are not provided, there is a warning displayed in logs with the problem description and the names of options\nwhich need to be specified. Parameter names are case insensitive and can be written in upper and lower registers.\n\n### Advanced configuration example\nSometimes there is need to change configuration from run to run. This can be done with changing environment variables\nbefore each run.\n```python\nimport os\nfrom datetime import datetime\nimport random\n\nimport dotenv\nimport pytest\n\n\n# Generate your run name here\ndef get_run_name():\n    return f"Regression [{datetime.now()}] [Other helpull stuff]"\n\n# Generate your build number here\ndef get_build_number():\n    return f"{random.randint(1, 10)}.{random.randint(1, 10)}.{random.randint(1, 10)}"\n\ndef load_access_token():\n    return dotenv.dotenv_values("secrets/secrets.txt")["REPORTING_SERVER_ACCESS_TOKEN"]\n\n\ndef run_tests():\n    os.environ["REPORTING_RUN_DISPLAY_NAME"] = get_run_name()\n    os.environ["REPORTING_RUN_BUILD"] = get_build_number()\n\n    # If you store your secrets seperately you can load it here\n    dotenv.load_dotenv("secrets/secrets.env")\n    # or you can set directly\n    os.environ["REPORTING_SERVER_ACCESS_TOKEN"] = load_access_token()\n\n    # Here you can pass arguments to pytest\n    pytest.main(["-n", "-2"])\n\n\nif __name__ == "__main__":\n    run_tests()\n```\n\n## Collecting logs\nFor sending logs to zebrunner you need to add ZebrunnerHandler to yours logger.\nExample:\n```python\nimport logging\n\nfrom pytest_zebrunner.zebrunner_logging import ZebrunnerHandler\n\nlogger = logging.getLogger(__name__)\nlogger.addHandler(ZebrunnerHandler())\n```\n\nTo send all logs to zebrunner you can add `ZebrunnerHandler` to root logger.\n```python\nimport logging\n\nfrom pytest_zebrunner.zebrunner_logging import ZebrunnerHandler\n\nlogging.root.addHandler(ZebrunnerHandler())\n```\n\n\n## Additional functionality\n\n**IMPORTANT**: All attachments to tests can only be done while some test is running.\nAll attachments to a test run can only be done while a pytest test session is active.\n---------------------------\n\n### Collecting captured screenshot\nSometimes it may be useful to have the ability to track captured screenshots in scope of Zebrunner Reporting. The agent comes\nwith the API allowing you to send your screenshots to Zebrunner, so that they could be attached to the test.\n\n```python\nfrom pytest_zebrunner import attach_test_screenshot\n\n\ndef test_something():\n    ...\n    driver.save_screenshot("path_to_screenshot.png) # Capture screenshot with selenium driver\n    attach_test_screenshot("path_to_screenshot.png")\n    ...\n```\n\n### Collecting additional artifacts\nIn case your tests or an entire test run produce some artifacts, it may be useful to track them in Zebrunner.\nThe agent comes with a few convenient methods for uploading artifacts in Zebrunner and linking them to the currently running test or test run.\nArtifacts and artifact references can be attached using functions from `attachments` module. Together with an artifact\nor artifact reference, you must provide the display name. For the file, this name must contain the file extension that\nreflects the actual content of the file. If the file extension does not match the file content, this file will not be\nsaved in Zebrunner. Artifact reference can have an arbitrary name.\n\n#### Attaching artifact to test\n```python\nfrom pytest_zebrunner import attach_test_artifact\n\n\ndef test_something():\n    ...\n    attach_test_artifact("path_to_artifact")\n    ...\n```\n\n### Attaching artifact reference to test\n```python\nfrom pytest_zebrunner import attach_test_artifact_reference\n\n\ndef test_something():\n    ...\n    attach_test_artifact_reference("name", "reference")\n    ...\n```\n\n### Attaching artifact to test run\n```python\nfrom pytest_zebrunner import attach_test_run_artifact\n\n\nattach_test_run_artifact("path_to_artifact")\n```\n\n### Attaching artifact reference to test run\n```python\nfrom pytest_zebrunner import attach_test_run_artifact_reference\n\n\nattach_test_run_artifact_reference("name", "reference")\n```\n\nArtifact uploading process is performed in the foreground now, so it will block the execution thread while sending.\nThe background uploading will be available in upcoming releases.\n\n\n### Attaching test labels\nIn some cases, it may be useful to attach some meta information related to a test. The agent comes with a concept of a label.\nLabel is a key-value pair associated with a test. The key and value are represented by a `str`. Labels can be attached to\ntests and test runs.\n\n```python\n@pytest.mark.label("name", "value")\ndef test_something():\n    ...\n```\nor\n```python\nfrom pytest_zebrunner import attach_test_label\n\n\ndef test_something():\n    ...\n    attach_test_label("name", "value")\n    ...\n```\n**Note:** These two methods can be combined.\n\nFor test run:\n```python\nfrom pytest_zebrunner import attach_test_run_label\n\nattach_test_run_label("name", "value")\n```\n\n\n### Tracking of test maintainer\nYou may want to add transparency to the process of automation maintenance by having an engineer responsible for\nevolution of specific tests or test classes. Zebrunner comes with a concept of a maintainer - a person that can be\nassigned to maintain tests. In order to keep track of those, the agent comes with the `@pytest.mark.maintainer` annotation.\n\nSee a sample test bellow:\n\n```python\n@pytest.mark.maintainer("username_of_maintainer")\ndef test_something():\n    ...\n```\n\n### Tracking web driver sessions\nThe Zebrunner test agent has a great ability to track tests along with remote driver sessions. You don\'t have to do anything.\nThe agent automatically injects the tracking functionality to the Selenium driver if the Selenium library is installed. The agent sends\ndriver capabilities to Zebrunner when the driver starts and the finish time when the driver stops.\n\nZebrunner can automatically collect your test artifacts like videos or selenium session logs if you are using\ntest running providers like ZebrunnerHub, BrowserStack, Lambdatest, etc. To enable this you need to enable integration in your project in Zebrunner\nand also specify the `provider` capability.\n\n#### Zebrunner\nExample:\n```python\ndef test_something():\n    hub_url = \'https://username:password@engine.zebrunner.com/wd/hub\'\n    capabilities = {\n        \'browserName\': \'firefox\',\n        \'enableVideo\': True,\n        \'enableLog\': True,\n        \'enableVNC\': True,\n        \'provider\': \'zebrunner\',\n        ...\n    }\n    driver = Remote(command_executor=hub_url, desired_capabilities=capabilities)\n    ...\n```\n\n### BrowserStack\nBrowserStack saves video and logs by default so you need just to specify capability.\nExample:\n```python\ndef test_something():\n    hub_url = \'https://username:password@hub-cloud.browserstack.com/wd/hub\'\n    capabilities = {\n        \'browser\': \'firefox\',\n        \'provider\': \'BROWSERSTACK\',\n        ...\n    }\n    driver = Remote(command_executor=hub_url, desired_capabilities=capabilities)\n    ...\n```\n',
    'author': 'Anatoliy Platonov',
    'author_email': 'p4m.dev@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': 'https://zebrunner.com/documentation/agents/pytest',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.7,<4.0',
}


setup(**setup_kwargs)
