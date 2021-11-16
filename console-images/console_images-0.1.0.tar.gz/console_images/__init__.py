from to_ascii import *
from palette import *
from term import get_terminal_size

if __name__ == "__main__":
    show_gifs("example.gif",
              size=get_terminal_size(),
              color_function=color_it_full,
              dizering=True)
