import click

from autobright.colorhugals import ColorHug
from autobright.ddccontrol import DDCControl
from autobright.models import ProportionalBrightnessModel


@click.group()
def main():
    pass


@main.command()
def adjust() -> None:
    sensor = ColorHug()
    display = DDCControl(7)
    model = ProportionalBrightnessModel()

    reading = sensor.get_reading()
    brightness = model.map(reading)
    display.set_brightness(brightness)


@main.command()
def web_ui() -> None:
    from autobright.webui import main as webui_main

    webui_main()


if __name__ == "__main__":
    main()
