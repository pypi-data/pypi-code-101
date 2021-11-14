import argparse

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import RectangleSelector

from pdf2image import convert_from_path


def run():
    parser = argparse.ArgumentParser(
        description="""
    A tool that helps you include a subselection of a pdf using the
    \\includegraphics command in latex.

    You can use an interactive selector to draw a box on the pdf. The tool will
    then output a set of options that you should provide to \\includegraphics to
    display only that box.
    """
    )

    parser.add_argument("file", help="the path to the pdf.")
    parser.add_argument("page", help="the page you want to extract from.", type=int)

    args = parser.parse_args()

    pages = convert_from_path(args.file)
    page = pages[args.page]
    ax = plt.imshow(page)

    def line_select_callback(eclick, erelease):
        x1, y1 = eclick.xdata, eclick.ydata
        x2, y2 = erelease.xdata, erelease.ydata
        global SELECTION
        SELECTION = (x1, y1, x2, y2)

    def toggle_selector(event):
        global SELECTION
        if event.key == "enter":
            plt.close()
            x, y = page.size
            x1, y1, x2, y2 = SELECTION
            top = y1 / 200
            bottom = (y - y2) / 200
            right = x1 / 200
            left = (x - x2) / 200
            print(
                f"\\includegraphics[page={args.page + 1}, clip, trim={right}in {bottom}in {left}in {top}in]{{path/to/{args.file}}}"
            )

    # drawtype is 'box' or 'line' or 'none'
    toggle_selector.RS = RectangleSelector(
        ax.axes,
        line_select_callback,
        drawtype="box",
        useblit=True,
        button=[1, 3],  # don't use middle button
        minspanx=5,
        minspany=5,
        spancoords="pixels",
        interactive=True,
    )
    plt.connect("key_press_event", toggle_selector)
    plt.show()


if __name__ == "__main__":
    run()
