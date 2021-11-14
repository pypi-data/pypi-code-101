# flake8: noqa
import configparser
import os
import re


def read_configs(config_paths, config_dict):
    """Read a config file from filesystem.

    Args:
        config_paths (): A list of config file paths.
        config_dict (): A Config dictionary profile.

    Returns: Config profile dictionary

    """
    # We return all these values
    config = config_dict
    profile = config["profile"]

    # grab values from config files
    cp = configparser.ConfigParser()
    try:
        cp.read(config_paths)
    except Exception as e:
        raise Exception("%s: configuration file error" % profile)

    if len(cp.sections()) > 0:
        # we have a configuration file - lets use it
        try:
            # grab the section - as we will use it for all values
            section = cp[profile]
        except Exception as e:
            # however section name is missing - this is an error
            raise Exception("%s: configuration section missing" % profile)

        for option in list(config.keys()):
            if option not in config or config[option] is None:
                try:
                    config[option] = re.sub(r"\s+", "", section.get(option))
                    if config[option] == "":
                        config.pop(option)
                except (configparser.NoOptionError, configparser.NoSectionError):
                    pass
                except BaseException:
                    pass

    # remove blank entries
    for x in sorted(config.keys()):
        if config[x] is None or config[x] == "":
            try:
                config.pop(x)
            except BaseException:
                pass

    return config


config_paths = [
    ".gitjirabot.cfg",
    os.path.expanduser("~/.gitjirabot.cfg"),
    os.path.expanduser("~/.gitjirabot/gitjirabot.cfg"),
]

config_dict = {
    "jira_url": os.getenv("JIRA_URL"),
    "jira_token": os.getenv("JIRA_TOKEN"),
    "jira_user_name": os.getenv("JIRA_USERNAME"),
    "git_url": os.getenv("JIRA_URL"),
    "git_private_token": os.getenv("GIT_TOKEN"),
    "git_api_version": os.getenv("GIT_API_VERSION"),
    "profile": "GITJIRA",
}

"""
To setup config securely:
nano ~/.gitjirabot.cfg
"""
# Then enter the desired below with your details
# For jira ones https://atlassian-python-api.readthedocs.io/index.html#other-authentication-methods
# Obtain an API token from: https://id.atlassian.com/manage-profile/security/api-tokens
# You cannot log-in with your regular password to these services.
# For git/gitlab ones https://python-gitlab.readthedocs.io/en/stable/cli-usage.html#configuration
"""
[GITJIRA]
jira_url =
jira_token =
jira_user_name =
git_url =
git_private_token =
git_api_version = 4
"""

# Read config file if it exists and override the above
profile = read_configs(config_paths, config_dict)

jira_url = None
jira_token = None
jira_user_name = None
git_url = None
git_private_token = None
git_api_version = "4"

if "jira_url" in profile:
    jira_url = profile["jira_url"]

if "jira_token" in profile:
    jira_token = profile["jira_token"]

if "jira_user_name" in profile:
    jira_user_name = profile["jira_user_name"]

if "git_url" in profile:
    git_url = profile["git_url"]

if "git_private_token" in profile:
    git_private_token = profile["git_private_token"]

if "git_api_version" in profile:
    git_api_version = profile["git_api_version"]
