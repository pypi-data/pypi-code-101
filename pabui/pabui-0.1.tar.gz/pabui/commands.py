from flask import current_app as app

@app.cli.command("my_command")
def init_app():
	# My command would go here, if I had any...
	pass