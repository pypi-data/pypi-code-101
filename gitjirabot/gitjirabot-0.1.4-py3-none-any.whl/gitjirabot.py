# This really should not be here but for now to prevent failing.
# flake8: noqa
import re
from pprint import pprint
import gitlab
from atlassian import Confluence, Jira
from settings import git_api_version, git_private_token, git_url, jira_token, jira_url, jira_user_name

# Debugging Auth only
# print('jira_url: ', jira_url, 'jira_token: ', jira_token, 'jira_user_name: ', jira_user_name, 'git_url: ', git_url,
#       'git_private_token: ', git_private_token, 'git_api_version: ', git_api_version)

link_regex = re.compile(r"((https?):((//)|(\\\\))+([\w\d:#@%/;$()~_?\+-=\\\.&](#!)?)*)", re.DOTALL)

jira = Jira(url=jira_url, username=jira_user_name, password=jira_token, cloud=True)

confluence = Confluence(url=jira_url, username=jira_user_name, password=jira_token, cloud=True)

# private token or personal token authentication
gl = gitlab.Gitlab(git_url, private_token=git_private_token, api_version=git_api_version)

# https://python-gitlab.readthedocs.io/en/stable/gl_objects/mrs.html
# List the merge requests for a group 'wizardassistantscripts'
group = gl.groups.get("wizardassistantscripts")
mrs = group.mergerequests.list(state="merged")

# List the merge requests created by the user of the token on the GitLab server:
# mrs = gl.mergerequests.list()

pprint("=================================")
pprint(group)
pprint("=================================")
pprint(mrs)
