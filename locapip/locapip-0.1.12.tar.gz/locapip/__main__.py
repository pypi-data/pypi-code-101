import json
from pathlib import Path

import click

import locapip


@click.command()
@click.option('--port', type=int, default=6547)
@click.option('--config', type=click.Path(file_okay=True, dir_okay=False))
@click.option('--logging', type=click.Path(file_okay=True, dir_okay=False))
def main(port: int, config, logging):
    if logging is not None:
        locapip.set_logging(logging)

    if config is not None:
        locapip.config.update(json.loads(Path(config).read_text()))

    locapip.serve(port)


if __name__ == '__main__':
    main()
