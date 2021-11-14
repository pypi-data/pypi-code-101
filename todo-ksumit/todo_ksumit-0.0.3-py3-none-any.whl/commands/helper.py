import click
from tabulate import tabulate
from ..constants import HEADER_COLOR, TABLE_FORMAT

def tabulateList(table, headers=[]):
  click.secho(
    tabulate(table, headers=headers, tablefmt=TABLE_FORMAT), 
    fg=HEADER_COLOR
    )
