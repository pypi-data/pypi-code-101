from rich.console import Console
from rich.markdown import Markdown

def render_help(help_string : str):
    console = Console()
    console.print(help_string)
    input("Press enter to continue")

def help_projects():
    help_str = """
[bold cyan]Variables[/bold cyan] [bold]Page[/bold]

[bold green]Enter[/bold green] = [bold green]Go in a project[/bold green]
"""
    render_help(help_string = help_str)

def help_variables():
    help_str = """
[bold green]Variables[/bold green] [bold]Page[/bold]

[bold blue]c[/bold blue] = [bold blue]Create variables[/bold blue]

[bold blue]x[/bold blue] = [bold blue]Create variables on a loop[/bold blue]

[bold red]d[/bold red] = [bold red]Delete variables[/bold red]

[bold red]K[/bold red] = [bold red]Delete a whole environment[/bold red]

[bold blue]s[/bold blue] = [bold blue]Save an environment to a file[/bold blue]

[bold blue]p[/bold blue] = [bold blue]Copy one environment to another, new or not[/bold blue]

[bold green]Enter[/bold green] = [bold green]Go in a variable editor[/bold green]
    """
    render_help(help_string = help_str)

def help_variable_editor():
    help_str = """
[bold green]Variable Editor[/bold green] [bold]Page[/bold]

[bold blue]c[/bold blue] = [bold blue]Create variable environment[/bold blue]

[bold blue]x[/bold blue] = [bold blue]Create variables environments on a loop[/bold blue]

[bold red]d[/bold red] = [bold red]Delete variable environment[/bold red]

[bold green]Enter[/bold green] = [bold green]Edit the environment of a variable[/bold green]
"""
    render_help(help_string = help_str)