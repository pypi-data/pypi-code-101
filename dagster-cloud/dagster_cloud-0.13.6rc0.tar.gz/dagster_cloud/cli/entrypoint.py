from dagster_cloud.agent.cli import app as agent_app
from dagster_cloud.settings import app as settings_app
from dagster_cloud.workspace.cli import app as workspace_app
from typer import Typer

app = Typer(help="CLI tools for working with Dagster Cloud.")
app.add_typer(agent_app, name="agent")
app.add_typer(workspace_app, name="workspace")
app.add_typer(settings_app, name="settings")


if __name__ == "__main__":
    app()
