import click
import os
import re
from shuvel.rule import Severity
from shuvel.result import Result
import shuvel.utils as utils


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    utils.print_version()
    ctx.exit()


def set_verbose(ctx, param, value):
    utils.set_verbose()


@click.group()
@click.option("-v", "--version", is_flag=True, callback=print_version, expose_value=False, is_eager=True)
@click.option("-d", "--debug", is_flag=True, callback=set_verbose, expose_value=False, is_eager=True)
def shuvel_cli():
    pass


@click.command()
@click.option("-r", "--rules",
              help="Comma-seperated list of rule names and categories to run, wildcards accepted [*]",
              required=False,
              default="*",
              type=str)
@click.option("-s", "--sev",
              help="Only show results of this severity or higher [Info]",
              required=False,
              default="Info",
              type=click.Choice(["High", "Low", "Info"], case_sensitive=False))
@click.option("-t", "--target",
              help="Path to the directory with the source code to run against [.]",
              required=False,
              default=os.getcwd(),
              type=str)
@click.option("-R", "--rules-dir",
              help=f"Path to the rules directory [{utils.get_rules_dir()}]",
              required=False,
              default=utils.get_rules_dir(),
              type=str)
def run(rules, sev, target, rules_dir):
    """Run a set of rules against the target folder"""
    all_rules = utils.load_all_rules([""], rules_dir)

    severity = Severity(sev.lower())

    user_sel_rules = [x.strip() for x in rules.split(",")]

    target_files = []
    target_fq_dir = os.path.abspath(target)
    dirlist = [target_fq_dir]
    results = []

    utils.print_info(f"Running against the target directory `{target_fq_dir}`.")

    while len(dirlist) > 0:
        for (dirpath, dirnames, filenames) in os.walk(dirlist.pop()):
            dirlist.extend(dirnames)
            target_files.extend(map(lambda n: os.path.join(*n), zip([dirpath] * len(filenames), filenames)))

    for rule in all_rules:
        # First see if the rule we have loaded is supposed to run now
        if utils.should_rule_run(user_sel_rules, severity, rule):
            # Run this rule against the entire codebase. In the future we can make it smarter so that
            # specific rules run only against specific files based on extentions, but for now deal with it.
            p = re.compile(rule.pattern)

            for target_file in target_files:
                with open(target_file, "r") as fd:
                    lines = fd.readlines()
                    i = 0
                    for line in lines:
                        i += 1
                        m = p.search(line)
                        if m is not None:
                            tmp_result = Result(target_file, i, line.strip(), rule)
                            results.append(tmp_result)

    utils.print_info("Results:")
    for result in results:
        utils.print_info(f"{result.fq_file_path}:{result.line_num}")
        utils.print_info(f"    Match:    {result.line_str}")
        utils.print_info(f"    Rule:     {result.rule.name}")
        utils.print_info(f"    Severity: {result.rule.severity}")
        utils.print_info(f"    Desc:     {result.rule.description}")
        if result.rule.references:
            utils.print_info("    Refs:")
            for ref in result.rule.references:
                utils.print_info(f"        - {ref}")


shuvel_cli.add_command(run)


@click.command()
@click.option("-R", "--rules-dir",
              help="Path to the rules directory",
              required=False,
              default=utils.get_rules_dir(),
              type=str)
def test(rules_dir):
    """Load a set of rules, useful for testing"""
    utils.print_info(f"Loading all rules and validating correctness from `{rules_dir}`.")
    utils.load_all_rules([""], rules_dir)
    utils.print_info("All rules loaded successfully.")


shuvel_cli.add_command(test)


@click.command()
@click.option("-R", "--rules-dir",
              help="Path to the rules directory",
              required=False,
              default=utils.get_rules_dir(),
              type=str)
def rules(rules_dir):
    """Show all loaded rules"""
    utils.print_info(f"Showing all rules from `{rules_dir}`.")
    all_rules = utils.load_all_rules([""], rules_dir)
    all_rules = sorted(all_rules, key=lambda x: x.name)

    for rule_obj in all_rules:
        utils.print_info(rule_obj.name)


shuvel_cli.add_command(rules)

if __name__ == "__main__":
    shuvel_cli()
