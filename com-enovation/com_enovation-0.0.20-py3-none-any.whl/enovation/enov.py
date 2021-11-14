import logging
from inspect import stack

import click

from com.enovation.helper.click.df_load import df_load_csv, df_load_xls
from com.enovation.helper.click.df_write import df_to_stdout, df_to_xlsx
from com.enovation.helper.click.df_modify import df_rename_columns, df_cleanse_null, df_compress
from com.enovation.toolbox.predictability.click.dp_compute import dp_compute_date_predictability
from com.enovation.toolbox.predictability.click.dp_demo import dp_demo_date_predictability
from com.enovation.toolbox.predictability.click.dp_persist \
    import dp_write_bean_date_predictability, dp_load_bean_date_predictability
from com.enovation.toolbox.predictability.click.dp_graph import dp_graph_to_dash_date_predictability


_logger: logging.Logger = logging.getLogger(__name__)


@click.group(chain=True)
@click.pass_context
@click.option(
    '--verbose/--no-verbose', type=bool, default=None,
    help='Level of logging verbosity: INFO (--verbose), WARNING (default) or ERROR (--no-verbose).',
)
def enov(ctx_context, verbose):

    _logger.debug(f"Function '{stack()[0].filename} - {stack()[0].function}' is called")

    if verbose is True:
        click.echo("logging: INFO")
        logging.basicConfig(level="INFO")
    elif verbose is False:
        click.echo("logging: ERROR")
        logging.basicConfig(level="ERROR")
    else:
        click.echo("logging: WARNING")
        logging.basicConfig(level="WARNING")
    _logger.info(f"Welcome!")

    # Ensure that ctx_context.obj exists and is a dict (in case `cli()` is called
    # by means other than the `if` block below)
    # This is effectively the context, that is shared across commands
    if ctx_context.obj:
        pass
    else:
        _logger.debug(f"We call function ctx_context.ensure_object(dict)")
        ctx_context.ensure_object(dict)

    _logger.debug(f"Function '{stack()[0].filename} - {stack()[0].function}' is returning")


# com.enovation.helper.click.df_load
# noinspection PyTypeChecker
enov.add_command(df_load_csv)
# noinspection PyTypeChecker
enov.add_command(df_load_xls)

# com.enovation.helper.click.df_write
# noinspection PyTypeChecker
enov.add_command(df_to_stdout)
# noinspection PyTypeChecker
enov.add_command(df_to_xlsx)

# com.enovation.helper.click.df_modify
# noinspection PyTypeChecker
enov.add_command(df_rename_columns)
# noinspection PyTypeChecker
enov.add_command(df_cleanse_null)
# noinspection PyTypeChecker
enov.add_command(df_compress)

# com.enovation.toolbox.predictability.click - Date Predictability
# noinspection PyTypeChecker
enov.add_command(dp_compute_date_predictability)
# noinspection PyTypeChecker
enov.add_command(dp_write_bean_date_predictability)
# noinspection PyTypeChecker
enov.add_command(dp_load_bean_date_predictability)
# noinspection PyTypeChecker
enov.add_command(dp_graph_to_dash_date_predictability)
# noinspection PyTypeChecker
enov.add_command(dp_demo_date_predictability)


if __name__ == '__main__':
    enov()
