#    JointBox CLI
#    Copyright (C) 2021 Dmitry Berezovsky
#    The MIT License (MIT)
#
#    Permission is hereby granted, free of charge, to any person obtaining
#    a copy of this software and associated documentation files
#    (the "Software"), to deal in the Software without restriction,
#    including without limitation the rights to use, copy, modify, merge,
#    publish, distribute, sublicense, and/or sell copies of the Software,
#    and to permit persons to whom the Software is furnished to do so,
#    subject to the following conditions:
#
#    The above copyright notice and this permission notice shall be
#    included in all copies or substantial portions of the Software.
#
#    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
#    EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
#    MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
#    IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
#    CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
#    TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
#    SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

from cli_rack_validation import crv
from string import ascii_letters, digits

RESERVED_IDS = ("jb", "jointbox")


def valid_id(value):
    value = crv.string(value)
    if not value:
        raise crv.Invalid("ID must not be empty")
    if value[0].isdigit():
        raise crv.Invalid("First character in ID cannot be a digit.")
    if "-" in value:
        raise crv.Invalid("Dashes are not supported in IDs, please use underscores instead.")
    valid_chars = ascii_letters + digits + "_"
    for char in value:
        if char not in valid_chars:
            raise crv.Invalid(
                "IDs must only consist of upper/lowercase characters, the underscore"
                "character and numbers. The character '{}' cannot be used"
                "".format(char)
            )
    if value.lower() in RESERVED_IDS:
        raise crv.Invalid(f"ID '{value}' is reserved internally and cannot be used")

    return value
