"""Console script for ds_get."""
import sys

from .ds_get import (
    DSGetClient,
    DSGetClientException,
    load_config_from_env_args,
    parse_arguments,
)


def main():
    """Console script for ds_get."""

    args = parse_arguments()
    config = load_config_from_env_args(args)

    try:
        client = DSGetClient(**config)
        added, errors = client.add_links(args.links)
        for task in client.tasks():
            sys.stdout.write(f"{task['status']} -- {task['title']} \n")
        if added:
            sys.stdout.write(f"Succesfully added {len(added)} tasks\n")
        if errors:
            num_errors = len(errors)
            errors = "\n".join(map(str, errors))
            sys.stderr.write(f"Failed to add {num_errors} tasks.\nFailed tasks: {errors}\n")
            return -1
        return 0
    except DSGetClientException as e:
        raise SystemExit(e)


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
