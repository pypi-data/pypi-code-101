"""
Send email notifications 
"""

import smtplib
from email.message import EmailMessage

import click

from pynotify.config import load_config, write_config


def obfuscate(text):
    return int.from_bytes(text.encode(), "big")


def deobfuscate(number):
    return number.to_bytes(100, "big").replace(b"\x00", b"").decode()


@click.group()
def cli():
    """Example script."""

@cli.group()
def sender():
    """Update sender information."""


@sender.command("update")
@click.option("--email")
@click.option("--password")
@click.option("--host", default="smtp.gmail.com")
@click.option("--port", default=465)
def update(email, password, host, port):
    """Set the email bot information."""
    config = load_config()
    bot_details = config.get("bot", {})
    bot_details["email"] = email
    bot_details["password"] = obfuscate(password)
    bot_details["host"] = host
    bot_details["port"] = port
    config["bot"] = bot_details
    write_config(config)


@sender.command()
def show():
    """Show the bot information"""
    config = load_config()
    bot_details = config.get("bot", {})
    if "password" in bot_details:
        bot_details["password"] = deobfuscate(bot_details["password"])
    click.echo(bot_details)


@cli.command("add")
@click.argument("recipients", nargs=-1)
def add(recipients):
    """Add new recipients.

    notify add recipient1@gmail.com recipient2@gmail.com
    """
    config = load_config()
    existing = config.get("recipients", [])
    existing.extend(recipients)
    existing = sorted(set(existing))
    config["recipients"] = existing
    write_config(config)
    click.echo(f"ADDED   " + ", ".join(recipients))


@cli.command()
@click.argument("recipient")
def remove(recipient):
    """Remove a recipient by index or value."""
    config = load_config()
    recipients = config.get("recipients", [])

    try:
        removed = None
        if recipient.isdigit():
            removed = recipients.pop(int(recipient))
        else:
            removed = recipients.pop(recipients.index(recipient))

        write_config(config)
        click.echo(f"REMOVED {removed}")

    except:
        click.echo(f"Could not remove recipient: '{recipient}'.")


@cli.command("list")
def list_recipients():
    """Display all recipients."""
    config = load_config()
    recipients = config.get("recipients", [])

    click.echo("INDEX   RECIPIENT")
    for idx, recipient in enumerate(recipients):
        click.echo(f"{idx:<5}   {recipient}")


@cli.command("send")
@click.argument("subject")
@click.argument("content", default="")
@click.option("--pipe", default=False, is_flag=True)
def cli_send(subject, content, pipe):
    """Send an email."""
    if pipe:
        stream = click.get_text_stream('stdin')
        send(subject, content + stream.read())
        return 

    send(subject, content)


def send(subject, content):
    """Send an email"""
    config = load_config()
    try:
        username = config["bot"]["email"]
        password = deobfuscate(config["bot"]["password"])
    except Exception as e:
        click.echo(e)
        click.echo(
            "Error loading sender username and password. Check that they are set."
        )
        return

    msg = EmailMessage()
    msg.set_content(content)
    msg["Subject"] = subject
    msg["To"] = ", ".join(config.get("recipients", []))
    msg["From"] = username
    
    try:
        server = smtplib.SMTP_SSL(config["bot"]["host"], config["bot"]["port"])
        server.ehlo()
        server.login(username, password)
        server.send_message(msg)
        server.close()
        click.echo("Message sent.")
    except Exception as e:
        click.echo(e)
        click.echo("Error sending message")
