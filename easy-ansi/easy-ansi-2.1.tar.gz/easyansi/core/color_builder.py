from enum import Enum
from easyansi.core.core import CSI
from typing import Optional, Union, Any, Tuple, List, cast
from easyansi.common import field_validations as _validator

# Default Colors
DEFAULT_IDX = -1
DEFAULT_IDX_STR = "-1"
DEFAULT_FG = f"{CSI}39m"
DEFAULT_BG = f"{CSI}49m"
DEFAULT = DEFAULT_FG

MIN_VALUE = 0

# Color Types
_COLOR_TYPE_INTEGER = "integer"
_COLOR_TYPE_HEX_STRING = "hex_string"
_COLOR_TYPE_SEQUENCE = "sequence"
_COLOR_TYPE_UNKNOWN = "unknown"


class ColorBuilder(Enum):

    PALETTE_16 = (16, 15, 1, (1, -1))
    PALETTE_256 = (256, 255, 2, (1, -1))
    PALETTE_RGB = (16777216, 255, 6, (1, 3))

    def __init__(self, palette: int, max_color_value: int, max_hex_digits: int,
                 sequence_len: Tuple[int, int]):
        self._palette = palette
        self._max_color_seq = palette - 1
        self._max_color_value = max_color_value
        self._max_hex_digits = max_hex_digits
        self._sequence_len = sequence_len

    @property
    def min_value(self) -> int:
        """Return the minimum index value for a color palette."""
        return MIN_VALUE

    @property
    def max_value(self) -> int:
        """Return the maximum index value for a color palette."""
        return self._max_color_value

    @property
    def max_value_seq(self) -> int:
        """Return the maximum integer value for a color palette within a sequence."""
        return self._max_color_seq

    @property
    def default_value(self) -> int:
        """Return the default index value for a color palette palette."""
        return DEFAULT_IDX

    @property
    def palette(self) -> int:
        """Return the total number of colors for the palette."""
        return self._palette

    ######################################################################################
    # Main color entry point
    ######################################################################################

    def color(self,
              fg: Optional[Union[int, str, List[Union[int, str]], Tuple[Union[int, str]]]] = None,
              bg: Optional[Union[int, str, List[Union[int, str]], Tuple[Union[int, str]]]] = None) -> str:
        """Return the ANSI foreground and/or background color code(s).

        Parameters:
            fg: The foreground color value in one of several supported formats.
            bg: The background color value in one of several supported formats.
        """
        _validator.check_if_any_have_value("Color Values", fg, bg)
        ansi_code = ""
        if fg is not None:
            ansi_code += self._get_color_code(fg, False)
        if bg is not None:
            ansi_code += self._get_color_code(bg, True)
        return ansi_code

    def _get_color_code(self, color_value: Union[int, str, List[Union[int, str]], Tuple[Union[int, str]]],
                        is_bg: bool) -> str:
        """Return the ANSI color code for the value provided.

        Parameters:
            color_value: The color value in one of several supported formats.
            is_bg: True = Return background color code, else return foreground color code.
        """
        color_code = None
        color_type = self._get_color_value_type(color_value)
        if color_type == _COLOR_TYPE_INTEGER:
            color_value = cast(int, color_value)
            self._validate_int_color_value(color_value, is_bg)
            color_code = self._get_color_code_by_int(color_value, is_bg)
        elif color_type == _COLOR_TYPE_HEX_STRING:
            color_value = cast(str, color_value)
            self._validate_hex_color_value(color_value, is_bg)
            color_code = self._get_color_code_by_hex(color_value, is_bg)
        elif color_type == _COLOR_TYPE_SEQUENCE:
            color_value = cast(Union[List[Union[int, str]], Tuple[Union[int, str]]], color_value)
            self._validate_sequence_color_value(color_value, is_bg)
            color_code = self._get_color_code_by_sequence(color_value, is_bg)
        else:  # color_type == _COLOR_TYPE_UNKNOWN
            self._unknown_color_value_error(color_value, is_bg)
        color_code = cast(str, color_code)
        return color_code

    @staticmethod
    def _get_color_value_type(color_value: Union[int, str, List[Union[int, str]], Tuple[Union[int, str]]]) -> str:
        """Given a color value, determine the type of the data.

        Parameters:
            color_value: The value to determine the type of data.
        """
        if (isinstance(color_value, int)) and (not isinstance(color_value, bool)):
            return _COLOR_TYPE_INTEGER
        elif isinstance(color_value, str):
            return _COLOR_TYPE_HEX_STRING
        elif (isinstance(color_value, list)) or (isinstance(color_value, tuple)):
            return _COLOR_TYPE_SEQUENCE
        else:
            return _COLOR_TYPE_UNKNOWN

    @staticmethod
    def _unknown_color_value_error(color_value: Any, is_bg: bool) -> None:
        """Could not determine the type of the color value, throw an error.

        Parameters:
            color_value: The color value in question.
            is_bg: True = this is a background color, False = this is a foreground color.
        """
        field = "Background Color Type" if is_bg else "Foreground Color Type"
        msg = "Unknown color value type"
        _validator._raise_error(field, str(color_value), msg, TypeError)

    ######################################################################################
    # Process integer color values
    ######################################################################################

    def _validate_int_color_value(self, color_value: int, is_bg: bool) -> None:
        """Given a color value, determine if it is a valid integer value.

        Parameters:
            color_value: The color value to check to be a valid color integer.
            is_bg: True = this is a background color, False = this is a foreground color.
        """
        field = "Color Background Integer Value" if is_bg else "Color Foreground Integer Value"
        _validator.check_int_in_range(color_value, DEFAULT_IDX, self.max_value_seq, field)

    def _get_color_code_by_int(self, color_value: int, is_bg: bool) -> str:
        """Return the ANSI color code for the integer value provided.

        Parameters:
            color_value: The integer color value.
            is_bg: True = Return background color code, False = return foreground color code.
        """
        if color_value == DEFAULT_IDX:
            return DEFAULT_BG if is_bg else DEFAULT_FG
        elif self.palette == ColorBuilder.PALETTE_16.palette:
            color_code = 30 + (is_bg * 10) + ((color_value // 8) * 60) + (color_value % 8)
            return f"{CSI}{color_code}m"
        elif self.palette == ColorBuilder.PALETTE_256.palette:
            ground_code = "48" if is_bg else "38"
            return f"{CSI}{ground_code};5;{color_value}m"
        else:  # RGB palette
            digits = []
            temp_value = color_value
            for i in range(0, 6):
                power = 5 - i
                digits.append(temp_value // (16 ** power))
                temp_value -= digits[i] * (16 ** power)
            red = (digits[0] * 16) + digits[1]
            green = (digits[2] * 16) + digits[3]
            blue = (digits[4] * 16) + digits[5]
            return self._get_rgb_color_code_by_digits(red, green, blue, is_bg)

    @staticmethod
    def _get_rgb_color_code_by_digits(red: int, green: int, blue: int, is_bg: bool) -> str:
        """Given rgb values, return the RGB ANSI color code.

        Parameters:
             red: The red value (0 - 255)
             green: The green value (0 - 255)
             blue: The blue value (0 - 255)
             is_bg: True = Return background color code, False = return foreground color code.
        """
        ground_code = "48" if is_bg else "38"
        return f"{CSI}{ground_code};2;{red};{green};{blue}m"

    ######################################################################################
    # Process string hex color values
    ######################################################################################

    def _validate_hex_color_value(self, color_value: str, is_bg: bool) -> None:
        """Given a string color value, validate it is in a proper hex format.

        Parameters:
            color_value: The color value to check.
            is_bg: True = this is a background color, False = this is a foreground color
        """
        if not (isinstance(color_value, str) and color_value == DEFAULT_IDX_STR):
            field = "Color Background Hex String Value" if is_bg else "Color Foreground Hex String Value"
            hex_regex_1 = r"^[ ]*#?[ ]*[0-9a-fA-F]{1," + str(self._max_hex_digits) + r"}[ ]*$"
            hex_regex_2 = r"^[ ]*0x[0-9a-fA-F]{1," + str(self._max_hex_digits) + r"}[ ]*$"
            try:
                _validator.check_if_string_matches_regex(color_value, hex_regex_1, field)
            except ValueError:
                _validator.check_if_string_matches_regex(color_value, hex_regex_2, field)

    def _get_color_code_by_hex(self, color_value: str, is_bg: bool) -> str:
        """Return the ANSI color code for the string hex code value provided.

        Parameters:
            color_value: The string hex code color value.
            is_bg: True = Return background color code, False = return foreground color code.
        """
        if color_value == DEFAULT_IDX_STR:
            return self._get_color_code_by_int(DEFAULT_IDX, is_bg)
        int_value = self._hex_to_int(color_value)
        return self._get_color_code_by_int(int_value, is_bg)

    @staticmethod
    def _hex_to_int(hex_value: str) -> int:
        """Given a hex string code, return the integer value.

        Parameters:
            hex_value: The string hex code color value.
        """
        hex_vl = hex_value.replace("0x", "")
        hex_vl = hex_vl.replace("#", "")
        hex_vl = hex_vl.replace(" ", "")
        return int(hex_vl, 16)

    ######################################################################################
    # Process color sequences
    ######################################################################################

    def _validate_sequence_color_value(self, color_value: Union[List[Union[int, str]], Tuple[Union[int, str]]],
                                       is_bg: bool) -> None:
        """Given a color_value sequence, validate it and its values.

        Parameters:
            color_value: The color sequence to check
            is_bg: True = this is a background color, False = this is a foreground color
        """
        field = "Color Background Sequence Length" if is_bg else "Color Foreground Sequence Length"
        color_value_len = len(color_value)
        if self.palette == ColorBuilder.PALETTE_RGB.palette:
            try:
                _validator.check_int_in_range(color_value_len, self._sequence_len[0], self._sequence_len[0], field)
            except (ValueError, TypeError):
                _validator.check_int_in_range(color_value_len,
                                              self._sequence_len[1],
                                              self._sequence_len[1], field)
        else:
            _validator.check_int_in_range(color_value_len, self._sequence_len[0], self._sequence_len[0], field)
        for color_vl in color_value:
            color_type = self._get_color_value_type(color_vl)
            if color_type == _COLOR_TYPE_INTEGER:
                if (self.palette == ColorBuilder.PALETTE_RGB.palette and
                        color_value_len == self._sequence_len[1]):
                    color_vl = cast(int, color_vl)
                    ColorBuilder.PALETTE_256._validate_int_color_value(color_vl, is_bg)
                else:
                    color_vl = cast(int, color_vl)
                    self._validate_int_color_value(color_vl, is_bg)
            elif color_type == _COLOR_TYPE_HEX_STRING:
                if (self.palette == ColorBuilder.PALETTE_RGB.palette and
                        color_value_len == self._sequence_len[1]):
                    color_vl = cast(str, color_vl)
                    ColorBuilder.PALETTE_256._validate_hex_color_value(color_vl, is_bg)
                else:
                    color_vl = cast(str, color_vl)
                    self._validate_hex_color_value(color_vl, is_bg)
            else:
                self._unknown_color_value_error(color_vl, is_bg)

    def _get_color_code_by_sequence(self, color_value: Union[List[Union[int, str]], Tuple[Union[int, str]]],
                                    is_bg: bool) -> str:
        """Return the ANSI color code for the list/tuple value provided.
        The sequence should contain either integer or hex strings.

        Parameters:
            color_value: The sequence color value(s).
            is_bg: True = Return background color code, False = return foreground color code.
        """
        if (DEFAULT_IDX in color_value) or (DEFAULT_IDX_STR in color_value):
            return DEFAULT_BG if is_bg else DEFAULT_FG
        color_value_len = len(color_value)
        if color_value_len == self._sequence_len[0]:
            color_vl = color_value[0]
            color_type = self._get_color_value_type(color_vl)
            if color_type == _COLOR_TYPE_INTEGER:
                color_vl = cast(int, color_vl)
                return self._get_color_code_by_int(color_vl, is_bg)
            else:  # color type == string
                color_vl = cast(str, color_vl)
                return self._get_color_code_by_hex(color_vl, is_bg)
        else:  # sequence length = 3
            digits = []
            for color_vl in color_value:
                color_type = self._get_color_value_type(color_vl)
                if color_type == _COLOR_TYPE_INTEGER:
                    color_vl = cast(int, color_vl)
                    digits.append(color_vl)
                else:  # color type = string
                    color_vl = cast(str, color_vl)
                    digits.append(self._hex_to_int(color_vl))
            return self._get_rgb_color_code_by_digits(digits[0], digits[1], digits[2], is_bg)
