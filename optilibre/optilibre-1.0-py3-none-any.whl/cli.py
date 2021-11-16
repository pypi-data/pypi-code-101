import logging
import click
import os
import subprocess
import optilibre.helpers as helpers
import optilibre.runner as runner


@click.group()
def cli():
    pass


@cli.command()
def check_codecs():
    """
    Check that all codec supported by optilibre are also supported by the tools available on the system.
    :return:
    """
    msg_tool_present = "{} found; {} files can be optimized."
    msg_tool_missing = "{} could not be found. {} files can't be optimized."
    msg_codec_present = "{} optimization is supported."
    msg_codec_missing = "{} optimization is not supported. Check {} codecs."
    if helpers.is_tool("ffmpeg"):
        logging.info(msg_tool_present.format("ffmpeg", "video"))
        enabled_codec = str(subprocess.run(['ffmpeg', '-version'], capture_output=True).stdout).split(' ')
        if '--enable-libx264' in enabled_codec:
            logging.info(msg_codec_present.format("h264"))
        else:
            logging.warning(msg_codec_missing.format("h264", "ffmpeg"))
        if '--enable-libx265' in enabled_codec:
            logging.info(msg_codec_present.format("h265"))
        else:
            logging.warning(msg_codec_missing.format("h265", "ffmpeg"))

    else:
        logging.warning(msg_tool_missing.format("ffmpeg", "video"))

    if helpers.is_tool('jpegoptim'):
        logging.info(msg_tool_present.format("jpegoptim", "JPEG"))
    else:
        logging.warning(msg_tool_missing.format("jpegoptim", "JPEG"))

    if helpers.is_tool('cjxl'):
        logging.info(msg_tool_present.format("cjxl", "JPEG XL"))
    else:
        logging.warning(msg_tool_missing.format("cjxl", "JPEG XL"))


@cli.command()
@click.option("--config", default=os.path.join(os.path.dirname(__file__), '../../optilibre.conf'), help="Configuration file to use.")
def optimize(config):
    runner.main(config_file=config)

