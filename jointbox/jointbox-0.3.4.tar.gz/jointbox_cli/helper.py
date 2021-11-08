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

from typing import Any, Dict, Callable
from cli_rack_validation import crv

MCP23017_ADDRESS_MAPPING = {
    "000": 0x27,
    "100": 0x26,
    "010": 0x25,
    "110": 0x24,
    "001": 0x23,
    "101": 0x22,
    "011": 0x21,
    "111": 0x20,
}


def create_mapping_helper(mapping: Dict[str, Any]) -> Callable[[Any], Any]:
    def _mapper(value):
        if value not in mapping:
            raise crv.Invalid(
                "Value {} is not allowed. Allowed options are: {}".format(value, ", ".join(mapping.keys()))
            )
        return mapping[value]

    return _mapper


def create_address_mapper(mapping: Dict[str, Any]) -> Callable[[Any], Any]:
    def validator(value):
        value = crv.string(value)
        if value:
            mapper = create_mapping_helper(mapping)
            try:
                return mapper(value)
            except crv.Invalid:
                pass
        return crv.hex_int(value)

    return validator
