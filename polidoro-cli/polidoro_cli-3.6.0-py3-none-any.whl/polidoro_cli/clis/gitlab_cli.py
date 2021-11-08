import os
from datetime import datetime, timedelta

import gitlab
from polidoro_argument import Command
from polidoro_cli import CLI
from time import sleep
from polidoro_table import Table, Property
from polidoro_table.string_utils import Color, Format


class GitLab:
    @staticmethod
    @Command
    def monitor(*args):
        pipeline = GitLab.get_pipeline()
        properties = [
            Property(format=Format.DIM, condition=f'C("status") in ["skipped", "manual"]'),
            Property(format=Color.GREEN, condition=f'C("status") == "success"'),
            Property(format=Color.RED, condition=f'C("status") == "failed"'),
            Property(format=Color.YELLOW, condition=f'C("status") == "pending"'),
            Property(format=Color.CYAN, condition=f'C("status") == "running"'),
            Property(format=Format.BOLD, condition=f'C("status") == "running"'),
        ]
        stop = False
        while not stop:
            t = Table(f'{pipeline.ref} (#{pipeline.id}) - {pipeline.status}')
            t.add_columns(['name', 'status', 'queue', 'time', 'url'])
            jobs = list(filter(lambda _j: _j.status == 'pending', GitLab.get_project().jobs.list()))

            stop = True
            for j in pipeline.jobs.list():
                pos = 0
                if j in jobs:
                    pos = len(jobs) - jobs.index(j)

                row = [j.name, j.status, pos]
                if j.duration:
                    row.append(timedelta(seconds=int(j.duration)))
                else:
                    row.append('-')
                row.append(j.web_url)
                if j.status in ['running', 'pending']:
                    stop = False
                t.add_row(row, properties=properties)
            if stop:
                stop = pipeline.status not in ['running', 'pending']
                pipeline = GitLab.get_pipeline()
            print('-' * 50, datetime.now())
            print(t)
            sleep(0.5)
        # print(GitLab.get_pipeline().status)

    @staticmethod
    def get_pipeline():
        project = GitLab.get_project()
        branch, _ = CLI.execute('git rev-parse --abbrev-ref HEAD', capture_output=True, show_cmd=False)
        last_commit = project.commits.list(ref_name=branch.strip())[0]
        return GitLab.rest().projects.get(project.id).pipelines.list(sha=last_commit.id)[0]

    @staticmethod
    def rest():
        if not hasattr(GitLab, '__rest'):
            gl = gitlab.Gitlab('https://gitlab.buser.com.br/', private_token=os.environ.get('PRIVATE_TOKEN', 'NkaSwYViY8bmVz9RcJnp'))
            gl.auth()
            setattr(GitLab, '__rest', gl)
        return getattr(GitLab, '__rest')

    @staticmethod
    def get_project(project_name=None):
        if not hasattr(GitLab, '__project'):
            if project_name is None:
                out, _ = CLI.execute('git config --get remote.origin.url', capture_output=True, show_cmd=False)
                project_name = out.split('/')[-1].replace('.git', '').strip()
            projects = GitLab.rest().projects.list(search=project_name)
            for p in projects:
                if p.name == project_name:
                    setattr(GitLab, '__project', p)
        return getattr(GitLab, '__project')

    # @staticmethod
    # def get_last_commit(branch=None):
    #     if branch is None:
    #         branch = get_current_branch()
    #
    #     # Replacing any '/' into '%2F'
    #     branch = branch.replace('/', '%2F')
    #
    #     try:
    #         content = Gitlab.get_project().commits.list(ref_name=branch)
    #         if content:
    #             return content[0].id
    #     except HTTPError as e:
    #         if e.response.status_code == 404:
    #             pass
    #         else:
    #             raise
    #
    #
