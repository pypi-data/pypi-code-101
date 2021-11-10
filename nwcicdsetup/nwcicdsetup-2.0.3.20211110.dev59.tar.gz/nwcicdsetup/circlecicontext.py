import os
from dataclasses import dataclass, field


@dataclass
class CircleCIContext:
    branch: str
    build_num: int
    job_name: str
    project_reponame: str
    project_username: str
    stage: str
    username: str
    workflow_id: str
    workflow_job_id: str
    working_directory: str
    circle_token: str
    github_token: str
    vcs_type: str = "gh"
    current_vcs_revision: str = field(default="", init=False)
    last_successful_vcs_revision: str = field(default="", init=False)

    @staticmethod
    def create_from_environ() -> "CircleCIContext":
        return CircleCIContext(
            branch=os.environ["CIRCLE_BRANCH"],
            build_num=int(os.environ["CIRCLE_BUILD_NUM"]),
            job_name=os.environ["CIRCLE_JOB"],
            project_reponame=os.environ["CIRCLE_PROJECT_REPONAME"],
            project_username=os.environ["CIRCLE_PROJECT_USERNAME"],
            stage=os.environ["CIRCLE_STAGE"],
            username=os.environ["CIRCLE_USERNAME"],
            workflow_id=os.environ["CIRCLE_WORKFLOW_ID"],
            workflow_job_id=os.environ["CIRCLE_WORKFLOW_JOB_ID"],
            working_directory=os.environ["CIRCLE_WORKING_DIRECTORY"],
            circle_token=os.environ["CIRCLE_TOKEN"],
            github_token=os.environ["GITHUB_TOKEN"])

    @staticmethod
    def create_dummy_env() -> "CircleCIContext":
        circle_token = os.environ.get("CIRCLE_TOKEN", "")
        github_token = os.environ.get("GITHUB_TOKEN", "")
        return CircleCIContext(
            branch="develop",
            build_num=1,
            job_name="cicd/setup-and-run",
            project_reponame="nw-platform",
            project_username="nativewaves",
            stage="cicd/setup-and-run",
            username="vindor",
            workflow_id="29902ed6-5f07-4db9-a496-8bb122938e78",
            workflow_job_id="2239e3f4-dbd4-4879-b614-298584b884c2",
            working_directory=".",
            circle_token=circle_token,
            github_token=github_token)

    def get_changed_dir_path(self) -> str:
        return os.path.expanduser("~/.circleci/changed")

    def get_change_flag_path(self) -> str:
        return "{}/{}".format(self.get_changed_dir_path(), self.workflow_job_id)

    def set_change_flag(self) -> None:
        os.makedirs(self.get_changed_dir_path(), exist_ok=True)
        with open(self.get_change_flag_path(), "w") as file:
            file.write(self.workflow_job_id)

    def get_change_flag(self) -> bool:
        return os.path.exists(self.get_change_flag_path())
