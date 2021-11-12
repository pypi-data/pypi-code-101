import click

from cinemat.get_details import show_details, show_details_imdb
from cinemat.search import find
from cinemat.help import helper


@click.group()
def cinemator():
    pass


@cinemator.command()
@click.option(
    "--title",
    prompt="Names are difficult!!!, Please enter the name of the media or a keyword ",
    required=True,
    type=str,
)
def search(title):
    find(title, "", "keyword")


@cinemator.command()
@click.option(
    "--title",
    prompt="Names are difficult!!!, Please enter the name of the media or a keyword ",
    required=True,
    type=str,
)
@click.option(
    "--type",
    prompt="Do you know your type ? Please enter one of the options 'movie,series,episode' if you know your type",
    required=True,
    type=str,
)
def type(title, type):
    find(title, type, "type")


@cinemator.command()
@click.option(
    "--title",
    prompt="Names are difficult!!!, Please enter the name of the media or a keyword ",
    required=True,
    type=str,
)
@click.option(
    "--year",
    prompt="Are you a cinema geek? Please enter the year of release of the media if you know.",
    required=True,
    type=str,
)
def year(title, year):
    find(title, year, "year")


@cinemator.command()
@click.option(
    "--title", prompt="Please enter the title for the media to get details", required=True, type=str,
)
@click.option(
    "--tomatoes", prompt="Please enter tomat if you want rotten tomatoes details", default="", type=str,
)
@click.option(
    "--plot",
    prompt="Are you a cinema geek? Please enter 'short' or 'full' to choose how much details you want",
    required=True,
    type=str,
)
def details(title, plot, tomatoes):
    show_details(title, plot, tomatoes)


@cinemator.command()
@click.option(
    "--imdb", prompt="Please enter the imdb id of the media", required=True, type=str,
)
@click.option(
    "--plot",
    prompt="Are you a cinema geek? Please enter 'short' or 'full' to choose how much details you want",
    default="",
    type=str,
)
def imdb(imdb, plot):
    show_details_imdb(imdb, plot)


@cinemator.command()
def info():
    click.echo("")
    click.echo("Hey there!!!  If you want to do specific searches please try these commands bellow;")
    click.echo('"cinemator type","cinemator episode","cinemator imdb", "cinemator year","cinemator plot"')
    click.echo("----------------------------------------------------------------------------------------")
    click.echo("")
    click.echo('If you already know the media and want to get more details please try "cinemator details"')
    click.echo("-----------------------------------INFO-----------------------------------------------")
    click.echo("")
    helper()


if __name__ == "__main__":
    cinemator()
