# -*- encoding: utf-8 -*-

import click
import os
"""git quick tools"""

_help = """
    GIT command quick tools: 

    push: Only commit changes to remote branches

    pushall: Add * and commit changes to remote branches

    pushtag: Add tag and commit changes to remote branches
    
"""


@click.option('--repo',
              '-r',
              default="origin",
              help='repository, default is origin')
@click.option('--branch',
              '-b',
              default="master",
              help='branch, default is master')
@click.option('--msg', '-m', default=":heart:update", help='commit message')
@click.option('--tagv', '-v', default="1.0.0", help='tag version')
@click.command(context_settings=dict(
    allow_extra_args=True,
    ignore_unknown_options=True,
),
               help=_help)
@click.argument('command', required=False)
def git(command, repo, branch, msg, tagv):
    click.secho("Pull from git repository, default is origin master",
                fg='green')
    os.system("git pull {} {}".format(repo, branch))
    if 'push' == command:
        click.secho("Commit with message: {}".format(msg), fg='green')
        os.system("git commit -a -m \"{}\"".format(msg))
        os.system("git push")
    if 'pushall' == command:
        click.secho("Add * and commit with message: {}".format(msg), fg='green')
        os.system("git add *")
        os.system("git commit -a -m \"{}\"".format(msg))
        os.system("git push")

    if 'pushtag' == command:
        click.secho("Add tag and commit with message: {}".format(msg), fg='green')
        os.system("git add .")
        os.system("git commit -a -m \"publish on version %s\"" % tagv)
        os.system("git tag -a v{} -m \"add tag on {}\"".format(tagv, tagv))
        os.system("git push")
        os.system("git push origin --tags")

    if command == 'emoji':
        click.secho("{} {}".format(':tada:', "first commit"), fg='green')
        click.secho("{} {}".format(':new:', "new function"), fg='green')
        click.secho("{} {}".format(':bookmark:', "add tags"), fg='green')
        click.secho("{} {}".format(':bug:', "bug fixed"), fg='green')
        click.secho("{} {}".format(':ambulance:', "essential bug fixed"), fg='green')
        click.secho("{} {}".format(':wrench:', "configure file fixed"), fg='green')
        click.secho("{} {}".format(':rocket:', "function of deplay"), fg='green')
        click.secho("{} {}".format(':memo:', "document updated"), fg='green')
        click.secho("{} {}".format(':fire:', "huge modification"), fg='green')
        click.secho("{} {}".format(':heart:', "green_heart building relations"), fg='green')
