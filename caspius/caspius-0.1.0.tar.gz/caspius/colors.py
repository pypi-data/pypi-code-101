class Colors:
    RED = "\033[1;31m"
    BLUE = "\033[1;34m"
    CYAN = "\033[1;36m"
    GREEN = "\033[0;32m"
    DEFAULT = "\033[0;0m"
    BOLD = "\033[;1m"
    REVERSE = "\033[;7m"

    color_list = [RED, BLUE, CYAN, GREEN, DEFAULT, BOLD, REVERSE]

    color_string_enum = {
        "RED": RED,
        "BLUE": BLUE,
        "CYAN": CYAN,
        "GREEN": GREEN,
        "DEFAULT": DEFAULT,
        "BOLD": BOLD,
        "REVERSE": REVERSE
    }

    @staticmethod
    def get_color(color: str) -> str:
        return Colors.color_string_enum.get(color.upper(), Colors.DEFAULT)