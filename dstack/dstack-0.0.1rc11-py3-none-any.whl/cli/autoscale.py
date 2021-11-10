import sys
from argparse import Namespace

import colorama
from tabulate import tabulate

from dstack.cli.common import do_post, do_get, sensitive
from dstack.config import ConfigurationError


def unpause_func(_: Namespace):
    try:
        data = {
            "paused": False
        }
        response = do_post("autoscale/config", data)
        if response.status_code == 200:
            print("Succeeded")
        else:
            response.raise_for_status()
    except ConfigurationError:
        sys.exit(f"Call 'dstack login' or 'dstack register' first")


def pause_rules_func(_: Namespace):
    try:
        data = {
            "paused": True
        }
        response = do_post("autoscale/config", data)
        if response.status_code == 200:
            print("Succeeded")
        else:
            response.raise_for_status()
    except ConfigurationError:
        sys.exit(f"Call 'dstack login' or 'dstack register' first")


def set_rule_func(args: Namespace):
    try:
        data = {
            "instance_type": args.instance_type,
            "maximum": args.max
        }
        response = do_post("autoscale/rules/set", data)
        if response.status_code == 200:
            print("Succeeded")
        if response.status_code == 400 and response.json().get("message") == "aws is not configured":
            sys.exit(f"Call 'dstack aws config' first")
        if response.status_code == 404 and response.json().get("message") == "instance type not found":
            sys.exit(f"Instance type is not supported")
        else:
            response.raise_for_status()
    except ConfigurationError:
        sys.exit(f"Call 'dstack login' or 'dstack register' first")


def clear_rules_func(_: Namespace):
    try:
        response = do_post("autoscale/rules/clear")
        if response.status_code == 200:
            print("Succeeded")
        else:
            response.raise_for_status()
    except ConfigurationError:
        sys.exit(f"Call 'dstack login' or 'dstack register' first")


def list_rules_func(_: Namespace):
    try:
        response = do_get("autoscale/rules/list")
        if response.status_code == 200:
            table_headers = [
                f"{colorama.Fore.LIGHTMAGENTA_EX}INSTANCE TYPE{colorama.Fore.RESET}",
                f"{colorama.Fore.LIGHTMAGENTA_EX}NUMBER{colorama.Fore.RESET}"
            ]
            table_rows = []
            for rule in response.json()["rules"]:
                table_rows.append([
                    rule["instance_type"],
                    rule["maximum"]
                ])
            print(tabulate(table_rows, headers=table_headers, tablefmt="plain"))
        else:
            response.raise_for_status()
    except ConfigurationError:
        sys.exit(f"Call 'dstack login' or 'dstack register' first")


def info_func(_: Namespace):
    try:
        response = do_post("autoscale/info")
        if response.status_code == 200:
            response_json = response.json()
            print("Paused" if response_json.get("paused") is True else "Active")
        else:
            response.raise_for_status()
    except ConfigurationError:
        sys.exit(f"Call 'dstack login' or 'dstack register' first")


def register_parsers(main_subparsers):
    parser = main_subparsers.add_parser("autoscale", help="Manage autoscaling settings")

    subparsers = parser.add_subparsers()

    info_parser = subparsers.add_parser("info", help="Display the current configuration")
    info_parser.set_defaults(func=info_func)

    pause_parser = subparsers.add_parser("pause", help="Pause autoscaling")
    pause_parser.set_defaults(func=pause_rules_func)

    rules_parser = subparsers.add_parser("rules", help="Manage rules")

    unpause_parser = subparsers.add_parser("unpause", help="Unpause autoscaling")
    unpause_parser.set_defaults(func=unpause_func)

    rules_subparsers = rules_parser.add_subparsers()
    set_rule_parser = rules_subparsers.add_parser("set", help="Set an autoscaling rule for a given instance type")
    set_rule_parser.add_argument('instance_type', metavar='INSTANCE_TYPE', type=str)
    set_rule_parser.add_argument("--max", type=str, help="The maximum number of instances", required=True)
    set_rule_parser.set_defaults(func=set_rule_func)

    clear_rules_parser = rules_subparsers.add_parser("clear", help="Delete all rules")
    clear_rules_parser.set_defaults(func=clear_rules_func)

    list_rules_parser = rules_subparsers.add_parser("list", help="List existing rules")
    list_rules_parser.set_defaults(func=list_rules_func)
