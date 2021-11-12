import click
from .calculate import checksums

@click.group()
@click.version_option("0.0.1")
def cli():
    """A tool that show/verify checksums for a file."""
    pass

class style():
    RED = '\033[31m'
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    MAGENTA = "\033[35m"
    RESET = "\033[0m"

@cli.command()
@click.argument('filepath', required=True)
def get(filepath):
    """Get the checksums of a file. Including MD5, SHA-1, SHA-256, SHA-512."""
    md5_result = checksums("md5", filepath)
    sha1_result = checksums("sha1", filepath)
    sha256_result = checksums("sha256", filepath)
    sha512_result = checksums("sha512", filepath)
    click.echo(f"Displaying checksums for {filepath}\n")
    click.echo(f"{style.YELLOW}MD5 checksum:{style.RESET} {md5_result}\n")
    click.echo(f"{style.BLUE}SHA-1 checksum:{style.RESET} {sha1_result}\n")
    click.echo(f"{style.MAGENTA}SHA-256 checksum:{style.RESET} {sha256_result}\n")
    click.echo(f"{style.GREEN}SHA-512 checksum:{style.RESET} {sha512_result}\n")

@cli.command()
@click.argument('md5_checksum', required=True)
@click.argument('filepath', required=True)
def check_md5(md5_checksum, filepath):
    """Verify MD5 checksum."""
    if md5_checksum == checksums("md5", filepath):
        click.echo(f"{style.BLUE}Success: MD5 checksum of {filepath} is correct!{style.RESET}")
    else:
        click.echo(f"{style.RED}Failed: MD5 checksum of {filepath} is incorrect!{style.RESET}")

@cli.command()
@click.argument('sha1_checksum', required=True)
@click.argument('filepath', required=True)
def check_sha1(sha1_checksum, filepath):
    """Verify SHA-1 checksum."""
    if sha1_checksum == checksums("sha1", filepath):
        click.echo(f"{style.BLUE}Success: SHA-1 checksum of {filepath} is correct!{style.RESET}")
    else:
        click.echo(f"{style.RED}Failed: SHA-1 checksum of {filepath} is incorrect!{style.RESET}")

@cli.command()
@click.argument('sha256_checksum', required=True)
@click.argument('filepath', required=True)
def check_sha256(sha256_checksum, filepath):
    """Verify SHA-256 checksum."""
    if sha256_checksum == checksums("sha256", filepath):
        click.echo(f"{style.BLUE}Success: SHA-256 checksum of {filepath} is correct!{style.RESET}")
    else:
        click.echo(f"{style.RED}Failed: SHA-256 checksum of {filepath} is incorrect!{style.RESET}")

@cli.command()
@click.argument('sha512_checksum', required=True)
@click.argument('filepath', required=True)
def check_sha512(sha512_checksum, filepath):
    """Verify SHA-512 checksum."""
    if sha512_checksum == checksums("sha512", filepath):
        click.echo(f"{style.BLUE}Success: SHA-512 checksum of {filepath} is correct!{style.RESET}")
    else:
        click.echo(f"{style.RED}Failed: SHA-512 checksum of {filepath} is incorrect!{style.RESET}")

if __name__ == "__main__":
    cli()

