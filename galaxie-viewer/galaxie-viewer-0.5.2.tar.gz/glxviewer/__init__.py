import datetime
import term

__all__ = ['Viewer', 'viewer']


def resize_text(text=None, max_width=0, separator='~'):
    """
    Resize the text , and return a new text

    example: return '123~789' for '123456789' where max_width = 7 or 8

    :param text: the original text to resize
    :type text: str
    :param max_width: the size of the text
    :type max_width: int
    :param separator: a separator a in middle of the resize text
    :type separator: str
    :return: a resize text
    :rtype: str
    """
    if type(text) != str:
        raise TypeError('"text" must be a str type')
    if type(max_width) != int:
        raise TypeError('"max_width" must be a int type')
    if type(separator) != str:
        raise TypeError('"separator" must be a str type')

    if max_width < len(text):
        if max_width <= 0:
            return ''
        elif max_width == 1:
            return text[:1]
        elif max_width == 2:
            return text[:1] + text[-1:]
        elif max_width == 3:
            return text[:1] + separator[:1] + text[-1:]
        else:
            max_width -= len(separator[:1])
            return text[:int(max_width / 2)] + separator[:1] + text[-int(max_width / 2):]
    else:
        return text


def center_text(text=None, max_width=None):
    """
    Return a centred text from max_width, if max_width is None it will use the terminal width size.

    example:
    center_text(text="DLA", max_width=5) return " DLA "

    :param text: text to center
    :param max_width: the maximum width
    :type max_width: int
    :return: the centred text
    :rtype: str
    """
    if type(text) != str:
        raise TypeError('"text" must be a str type')
    if max_width is None:
        try:
            _, max_width = term.getSize()
        except TypeError:
            max_width = 80
    if type(max_width) != int:
        raise TypeError('"max_width" must be a int type')

    return "{0}{1}{2}".format(
        ' ' * int((max_width / 2) - (len(text) / 2)),
        text,
        ' ' * int(max_width - len(' ' * int((max_width / 2) - (len(text) / 2)) + text))
    )


def bracket_text(text=None, symbol_inner="[", symbol_outer="]"):
    """
    Surround a text with a inner and outer char.

    Not you should center you text with center_text()before call it function

    :param symbol_inner: the symbol to use for as inner, generally that '[', '<', '('
    :type symbol_inner: str
    :param symbol_outer: the symbol to use for as outer, generally that ']', '>', ')'
    :type symbol_outer: str
    :param text: the text it will be sur surround by the inner and outer chars
    :type text: str
    :return: the text surrounded by inner and outer
    :rtype: str
    """
    if type(text) != str:
        raise TypeError('"text" must be a str type')
    if type(symbol_inner) != str:
        raise TypeError('"symbol_inner" must be a str type')
    if type(symbol_outer) != str:
        raise TypeError('"symbol_outer" must be a str type')

    return "{0}{1}{2}".format(symbol_inner, text, symbol_outer)


class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None

    def __call__(cls, *args, **kw):
        if cls.instance is None:
            cls.instance = super(Singleton, cls).__call__(*args)
        return cls.instance


class Viewer(object, metaclass=Singleton):
    """
    The class viewer
    """

    def __init__(self):
        # protected variables
        self.__with_date = None
        self.__status_text = None
        self.__status_text_color = None
        self.__status_symbol = None
        self.__text_column_1 = None
        self.__text_column_2 = None
        self.__text_column_3 = None
        self.__size_line_actual = None
        self.__size_line_previous = None

        # init property's
        self.with_date = None
        self.status_text = None
        self.status_text_color = None
        self.status_symbol = None
        self.text_column_1 = None
        self.text_column_2 = None
        self.text_column_3 = None
        self.size_line_actual = None
        self.size_line_previous = None

    @property
    def with_date(self):
        """
        Property use for show date

        :return: with date property value
        :rtype: str
        """
        return self.__with_date

    @with_date.setter
    def with_date(self, value):
        """
        set the with_date property

        Default value is True

        :param value: the `with_date` property value
        :type value: bool
        :raise TypeError: if ``value`` is not a bool type
        """
        if value is None:
            value = True
        if type(value) != bool:
            raise TypeError("'with_date' property must be a bool type")
        if self.with_date != value:
            self.__with_date = value

    @property
    def status_text(self):
        """
        Property it store text of the status text like "DEBUG" "LOAD"

        Later the Viewer will add bracket's around it text, and set the color during display post-processing.

        see: ``status_text_color`` property

        :return: status_text property value
        :rtype: str
        """
        return self.__status_text

    @status_text.setter
    def status_text(self, value=None):
        """
        Set the status_text property value

        :param value: the status_text property value
        :type value: str
        :raise TypeError: if ``value`` is not a str type
        """
        if value is None:
            value = "DEBUG"
        if type(value) != str:
            raise TypeError("'status_text' property must be a str type")
        if self.status_text != value:
            self.__status_text = value

    @property
    def allowed_colors(self):
        """
        Allowed colors:

        ORANGE, RED, RED2, YELLOW, YELLOW2, WHITE, WHITE2, CYAN, GREEN, GREEN2

        Note that Upper, Lower, Tittle case are allowed

        :return: A list of allowed colors
        :rtype: list
        """
        return ["BLACK", "RED", "GREEN", "YELLOW", "BLUE", "MAGENTA", "CYAN", "WHITE"]

    @property
    def status_text_color(self):
        """
        Property it store one allowed color value, it value will be use to display ``status_text`` color.

        see: ``status_text`` property for more details

        :return: the ``status_text_color`` property value
        :rtype: str
        """
        return self.__status_text_color

    @status_text_color.setter
    def status_text_color(self, value):
        """
        Set the value of the ``status_text_color`` property.

        see: ``allowed_colors`` for more details

        :param value: The ``status_text_color`` property value
        :type value: str
        :raise TypeError: When ``status_text_color`` is not a str
        :raise ValueError: When ``status_text_color`` value is not a allowed color
        """
        if value is None:
            value = "WHITE"
        if type(value) != str:
            raise TypeError("'status_text_color' property must be a str type")
        if value.upper() not in self.allowed_colors:
            raise ValueError("{0} is not a valid color for 'status_text_color' property")
        if self.status_text_color != value:
            self.__status_text_color = value

    @property
    def status_symbol(self):
        """
        Property it store a symbol of one letter. like ! > < / - | generally for show you application fo something.

        it thing exist that because i use it for show if that a input or output message.

        Actually the symbol use CYAN color, and have 1 space character on the final template. Certainly something it can
        be improve. Will see in future need's ...

        :return: status_symbol character
        :rtype: str
        """
        return self.__status_symbol

    @status_symbol.setter
    def status_symbol(self, value):
        """"
        Set the symbol of ``status_symbol`` you want. Generally > or < or ?

        :param value: the symbol of ``status_symbol``
        :type value: str
        :raise TypeError: when ``status_symbol`` value is not a str type
        """
        if value is None:
            value = " "
        if type(value) != str:
            raise TypeError("'status_symbol' property must be set with str value")
        if self.status_symbol != value:
            self.__status_symbol = value

    @property
    def text_column_1(self):
        """
        Property it store ``text_column_1`` value. It value is use by template for display the column 1

        :return: The ``text_column_1`` value
        :rtype: str
        """
        return self.__text_column_1

    @text_column_1.setter
    def text_column_1(self, value):
        """
        Set the ``text_column_1`` value.

        :param value: The text you want display on it column
        :type value: str
        :raise TypeError: When ``text_column_1`` value is not a str type
        """
        if value is None:
            value = ""
        if type(value) != str:
            raise TypeError("'text_column_1' property must be set with str value")
        if self.text_column_1 != value:
            self.__text_column_1 = value

    @property
    def text_column_2(self):
        """
        Property it store ``text_column_2`` value. It value is use by template for display the column 2

        :return: The ``text_column_2`` value
        :rtype: str
        """
        return self.__text_column_2

    @text_column_2.setter
    def text_column_2(self, value):
        """
        Set the ``text_column_2`` value.

        :param value: The text you want display on it column
        :type value: str
        :raise TypeError: When ``text_column_2`` value is not a str type
        """
        if value is None:
            value = ""
        if type(value) != str:
            raise TypeError("'text_column_2' property must be set with str value")
        if self.text_column_2 != value:
            self.__text_column_2 = value

    @property
    def text_column_3(self):
        """
        Property it store ``text_column_3`` value. It value is use by template for display the column 3

        :return: The ``text_column_3`` value
        :rtype: str
        """
        return self.__text_column_3

    @text_column_3.setter
    def text_column_3(self, value):
        """
        Set the ``text_column_3`` value.

        :param value: The text you want display on it column
        :type value: str
        :raise TypeError: When ``text_column_3`` value is not a str type
        """
        if value is None:
            value = ""
        if type(value) != str:
            raise TypeError("'text_column_3' property must be set with str value")
        if self.text_column_3 != value:
            self.__text_column_3 = value

    @staticmethod
    def flush_a_new_line():
        term.writeLine()

    @property
    def formatted_date(self):
        return str(datetime.datetime.now().replace(microsecond=0).isoformat())

    def write(
            self,
            with_date=None,
            status_text=None,
            status_text_color=None,
            status_symbol=" ",
            column_1=None,
            column_2=None,
            column_3=None,
            prompt=None,
    ):
        """
        Flush a line a bit like you want

        :param with_date: show date if True
        :type with_date: bool
        :param status_text: The text to display ton the status part
        :type status_text: str
        :param status_text_color: allowed : BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE
        :type status_text_color: str
        :param status_symbol: str or None
        :param column_1: A Class name
        :type column_1: str or None
        :param column_2: The thing to print in column 2
        :type column_2: str or None
        :param column_3: The thing to print in column 3
        :type column_3: str or None
        :param prompt: value
        :type prompt: None, -1, +1
        """

        self.with_date = with_date
        self.status_text = status_text
        self.status_text_color = status_text_color
        self.status_symbol = status_symbol
        self.text_column_1 = column_1
        self.text_column_2 = column_2
        self.text_column_3 = column_3

        if self.status_text_color.lower() == "black":
            status_text_color = term.black
        elif self.status_text_color.lower() == "red":
            status_text_color = term.red
        elif self.status_text_color.lower() == "green":
            status_text_color = term.green + term.bold
        elif self.status_text_color.lower() == "yellow":
            status_text_color = term.yellow + term.bold
        elif self.status_text_color.lower() == "blue":
            status_text_color = term.blue
        elif self.status_text_color.lower() == "magenta":
            status_text_color = term.magenta
        elif self.status_text_color.lower() == "cyan":
            status_text_color = term.cyan
        elif self.status_text_color.lower() == "white":
            status_text_color = term.white + term.dim
        else:
            status_text_color = term.white

        # Status Clean up
        status_text = resize_text(text=self.status_text, max_width=5)
        status_text = center_text(text=status_text, max_width=5)
        status_text = bracket_text(text=status_text)

        try:
            line, _ = term.getSize()
        except TypeError:
            line = 1

        term.pos(line, 1)
        # Column state
        if self.with_date:
            string_print = "{0:} {1:<5} {2:<3}".format(
                term.bgwhite + term.black + self.formatted_date + term.off,
                status_text_color + status_text + term.off,
                term.bold + term.cyan + self.status_symbol + term.off,

            )

        else:
            string_print = "{0:<5} {1:<3}".format(
                status_text_color + status_text + term.off,
                term.bold + term.cyan + status_symbol + term.off,
            )
        if len(self.text_column_1):
            string_print += " {0:<10}".format(self.text_column_1)

        if len(self.text_column_2):
            string_print += " {0:<10}".format(self.text_column_2)

        if prompt is None:
            term.writeLine(string_print)
        else:
            term.write(string_print)

        term.clearLineFromPos()


viewer = Viewer()
