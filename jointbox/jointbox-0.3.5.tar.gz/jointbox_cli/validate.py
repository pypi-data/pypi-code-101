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

import logging
import random
import re
import string
import typing
from typing import Dict, Callable

from cli_rack_validation import crv
from cli_rack_validation.validate import Any
from jointbox_cli import const, helper

_LOGGER = logging.getLogger("jb.validation")

COMBINE_OPERATOR = "&"
CMD_GENERATE = "$generate"
SPECIAL_CHARS = "-_*&^%$#@!~"
API_KEY_CHARS = string.ascii_uppercase + string.ascii_lowercase + string.digits + SPECIAL_CHARS
ID_CHARS = string.ascii_letters + string.digits + "_"
VALID_PARAM_NAME_REGEX = re.compile(r"^[a-zA-Z_][a-zA-Z0-9_]*([a-zA-Z_][a-zA-Z0-9_]*)*$")
VALID_LOCATOR_REGEX = re.compile(r"^[a-zA-Z_0-9\-]+:(.*)$")

_REGISTERED_IDS = []


def valid_param_name(value):
    """
    Validate that given value is a valid parameter name. It could include latin letters,
    numbers and symbol _. It also can't start with number
    """
    value = crv.string_strict(value)
    if not VALID_PARAM_NAME_REGEX.fullmatch(value):
        raise crv.Invalid(
            'Invalid name "{}". Name should consist of latin letters, '
            "numbers symbol _ and can't start with digit".format(value)
        )
    return value


def valid_locator(value):
    value = crv.string_strict(value)
    if not VALID_LOCATOR_REGEX.fullmatch(value):
        raise crv.Invalid(
            'Invalid locator "{}". Locator must include locator prefix separated by colon from the locator body'.format(
                value
            )
        )
    return value


def generate_api_key(length=16):
    return "".join(random.choice(API_KEY_CHARS) for _ in range(length))


def generate_id(prefix="auto_", length=10):
    while True:
        new_id = prefix + "".join(random.choice(ID_CHARS) for _ in range(length))
        if new_id not in _REGISTERED_IDS:
            _REGISTERED_IDS.append(new_id)
            break
    return new_id


def ensure_api_key(value):
    value = crv.string(value)
    if not value or value == CMD_GENERATE:
        value = generate_api_key(24)
    else:
        if len(value) < 16:
            raise crv.Invalid("Api key length must be at least 16 characters")
        for c in value:
            if c not in API_KEY_CHARS:
                raise crv.Invalid(
                    "Api key must contain only latin letters, digits and special chars ({})".format(SPECIAL_CHARS)
                )

    return value


def hostname(value):
    value = crv.string(value)
    if len(value) > 63:
        raise crv.Invalid("Hostnames can only be 63 characters long")
    show_warn = False
    for c in value:
        if not (c.isalnum() or c in "_-"):
            raise crv.Invalid("Hostname can only have alphanumeric characters and _ or -")
        if "_" == c:
            show_warn = True
    if show_warn:
        _LOGGER.warning(
            'Avoid using "_" character in host names. While it might work and is allowed by EspHome '
            "because of historical reasons it violates some standards and might cause some strange issues"
        )
    return value


def valid_id(value):
    """Validate that the given value would be a valid C++ identifier name."""
    value = crv.string(value)
    if not value:
        raise crv.Invalid("ID must not be empty")
    if value[0].isdigit():
        raise crv.Invalid("First character in ID cannot be a digit.")
    if "-" in value:
        raise crv.Invalid("Dashes are not supported in IDs, please use underscores instead.")
    for char in value:
        if char not in ID_CHARS:
            raise crv.Invalid(
                "IDs must only consist of upper/lowercase characters, the underscore"
                "character and numbers. The character '{}' cannot be used"
                "".format(char)
            )
    return value


def ensure_valid_id(value):
    value = crv.string(value)
    if not value or value == CMD_GENERATE:
        value = generate_id()
    return valid_id(value)


def valid_id_prefix(value):
    """Should be either empty string or valid id"""
    value = crv.string(value)
    if not value:
        return value
    return valid_id(value)


def domain_name(value):
    value = crv.string_strict(value)
    if not value:
        return value
    if not value.startswith("."):
        raise crv.Invalid("Domain name must start with .")
    if value.startswith(".."):
        raise crv.Invalid("Domain name must start with single .")
    for c in value:
        if not (c.isalnum() or c in "._-"):
            raise crv.Invalid("Domain name can only have alphanumeric characters and _ or -")
    return value


frequency = crv.float_with_unit("frequency", "(Hz|HZ|hz)?", no_conversion=True)
resistance = crv.float_with_unit("resistance", "(Ω|Ω|ohm|Ohm|OHM)?", no_conversion=True)
current = crv.float_with_unit("current", "(a|A|amp|Amp|amps|Amps|ampere|Ampere)?", no_conversion=True)
voltage = crv.float_with_unit("voltage", "(v|V|volt|Volts)?", no_conversion=True)
distance = crv.float_with_unit("distance", "(m)", no_conversion=True)
framerate = crv.float_with_unit("framerate", "(FPS|fps|Fps|FpS|Hz)", no_conversion=True)
angle = crv.float_with_unit("angle", "(°|deg)", optional_unit=True, no_conversion=True)
_temperature_c = crv.float_with_unit("temperature", "(°C|° C|°|C)?", no_conversion=True)
_temperature_k = crv.float_with_unit("temperature", "(° K|° K|K)?", no_conversion=True)
_temperature_f = crv.float_with_unit("temperature", "(°F|° F|F)?", no_conversion=True)
decibel = crv.float_with_unit("decibel", "(dB|dBm|db|dbm)", optional_unit=True, no_conversion=True)
pressure = crv.float_with_unit("pressure", "(bar|Bar)", optional_unit=True, no_conversion=True)


def temperature(value):
    try:
        return _temperature_c(value)
    except Invalid as orig_err:  # noqa
        pass

    try:
        return _temperature_k(value)
    except crv.Invalid:
        pass

    try:
        return _temperature_f(value)
    except crv.Invalid:
        pass

    raise orig_err  # noqa


class ParamsHolder(object):
    def __init__(self, data: Dict[str, Dict]) -> None:
        super().__init__()
        self.original_dict: Dict[str, Dict] = data

    def __getitem__(self, item):
        return self.original_dict[item]

    def __setitem__(self, key, value):
        self.original_dict[key] = value

    def __dict__(self):
        return self.original_dict

    def __call__(self, *args, **kwargs):
        return ParameterValidators.create_schema_for_param_def(self.original_dict)(*args)


class _ParameterValidators:
    def __init__(self) -> None:
        super().__init__()
        self.__cache_initialized = False
        self.__cache: Dict[str, typing.Any] = {}

    def build_cache(self):
        for x in dir(crv):
            if x.startswith("_") or x.isupper():
                continue
            self.__cache[x] = getattr(crv, x)
        self.__cache["int"] = self.__cache["int_"]
        self.__cache["float"] = self.__cache["float_"]
        self.__cache["string"] = self.__cache["string"]
        self.__cache["package_params"] = package_params
        self.__cache["package_params_list"] = package_params_list
        self.__cache["valid_param_name"] = valid_param_name
        self.__cache["valid_id"] = valid_id
        self.__cache["valid_id_prefix"] = valid_id_prefix
        self.__cache["hostname"] = hostname
        self.__cache["domain_name"] = domain_name
        self.__cache["ensure_api_key"] = ensure_api_key
        self.__cache["ensure_valid_id"] = ensure_valid_id
        self.__cache["sensor"] = sensor
        self.__cache["polling"] = polling
        self.__cache["optional"] = optional
        self.__cache["polling_sensor"] = polling_sensor
        self.__cache["optional_sensor"] = optional_sensor
        self.__cache["optional_polling_sensor"] = optional_polling_sensor
        self.__cache["combine"] = combine
        self.__cache["frequency"] = frequency
        self.__cache["resistance"] = resistance
        self.__cache["current"] = current
        self.__cache["voltage"] = voltage
        self.__cache["distance"] = distance
        self.__cache["framerate"] = framerate
        self.__cache["angle"] = angle
        self.__cache["decibel"] = decibel
        self.__cache["pressure"] = pressure
        self.__cache["temperature"] = temperature
        self.__cache["actions_with_fallback"] = actions_with_fallback
        self.__cache["mcp23017_address"] = mcp23017_address
        self.__cache["pcf8574_address"] = pcf8574_address
        self.__cache["ads1115_address"] = ads1115_address
        self.__cache["pca9685_address"] = pca9685_address
        self.__cache_initialized = True

    @property
    def validators(self):
        if not self.__cache_initialized:
            self.build_cache()
        return self.__cache

    def validator_by_name(self, name: str) -> Any:
        return self.validators[name]

    def validator_exists(self, name: str) -> bool:
        return name in self.validators

    def validator_def_to_fn(self, validator_def_dict: dict) -> Callable[[Any], Any]:
        funct = self.validators[validator_def_dict[const.CONF_NAME]]
        args = validator_def_dict.get(const.CONF_ARGS)
        if args is not None:
            if isinstance(args, dict):
                funct = funct(**args)
            elif isinstance(args, list):
                funct = funct(*args)
        return funct

    def create_schema_for_param_def(self, param_def_dict: Dict[str, Dict]) -> crv.Schema:
        res = {}
        for name, cfg in param_def_dict.items():
            default = cfg.get(const.CONF_DEFAULT, crv.UNDEFINED)
            if cfg.get(const.CONF_REQUIRED, True):
                name = crv.Required(name, default=default, description=cfg.get(const.CONF_DESCRIPTION))
            else:
                name = crv.Optional(name, default=default, description=cfg.get(const.CONF_DESCRIPTION))
            validator_fn = cfg.get(const.CONF_VALIDATOR, crv.anything)
            res[name] = validator_fn
        return crv.Schema(res)


ParameterValidators = _ParameterValidators()


def valid_validator_name(value):
    value = crv.string_strict(value)
    if ParameterValidators.validator_exists(value):
        return value
    raise crv.Invalid(
        "Invalid validator name '{}'. Valid options are: {}".format(value, ", ".join(ParameterValidators.validators))
    )


validator_def = crv.Schema(
    {
        crv.Required(const.CONF_NAME): valid_validator_name,
        crv.Optional(const.CONF_ARGS): crv.Any({valid_param_name: crv.anything}, crv.ensure_list(crv.anything)),
    }
)


def ensure_validator_def(value):
    if isinstance(value, str):
        # If just string - check if it has & operator first
        if COMBINE_OPERATOR in value:
            parts = [x.strip() for x in value.split(COMBINE_OPERATOR)]
            return validator_def({const.CONF_NAME: "combine", const.CONF_ARGS: parts})
        # Otherwise - just convert to dict
        return validator_def({const.CONF_NAME: value})
    return validator_def(value)


def ensure_valid_validator(value):
    """Normalizes validator definition and converts it into validation function"""
    val_def = ensure_validator_def(value)
    return ParameterValidators.validator_def_to_fn(val_def)


valid_params_def = crv.ensure_schema(
    {
        valid_param_name: {
            crv.Optional(const.CONF_DESCRIPTION): crv.string_strict,
            crv.Optional(const.CONF_DEFAULT): crv.anything,
            crv.Optional(const.CONF_REQUIRED, default=True): crv.boolean,
            crv.Optional(const.CONF_VALIDATOR): ensure_valid_validator,
        }
    }
)


def package_params(**kwargs):
    params_def = valid_params_def(kwargs)
    holder: ParamsHolder = ParamsHolder(params_def)
    # holder.original_dict = params_def
    return holder


def package_params_list(**kwargs):
    return crv.ensure_list(package_params(**kwargs))


valid_export_def = crv.ensure_schema(
    {crv.Required(const.CONF_NAME): valid_param_name, crv.Optional(const.CONF_DESCRIPTION): crv.string}
)


def ensure_valid_export_def(value):
    if isinstance(value, str):
        return valid_export_def({const.CONF_NAME: value})
    return valid_export_def(value)


valid_macros_def = crv.Schema(
    {crv.Required(valid_id): {const.CONF_PARAMS: valid_params_def, const.CONF_BODY: crv.Any(list, dict)}}
)

sensor = crv.Schema(
    {
        crv.Required("expose", default=True): crv.boolean,
        crv.Required("disabled_by_default", default=False): crv.boolean,
    }
)

polling = crv.Schema(
    {
        crv.Required("update_interval", default="5min"): crv.update_interval,
    }
)

optional = crv.Schema(
    {
        crv.Required("enable", default=True): crv.boolean,
    }
)

optional_sensor = sensor.extend(optional.schema)
optional_polling_sensor = optional_sensor.extend(polling.schema)
polling_sensor = sensor.extend(polling.schema)

actions_with_fallback_schema = crv.ensure_schema(
    crv.Any(
        {
            const.CONF_DEFAULT: crv.ensure_list(crv.anything),
            const.WHEN_ONLINE: crv.ensure_list(crv.anything),
        },
        crv.ensure_list(crv.anything),
    )
)


def combine(*args, **kwargs):
    if len(args) > 0:
        kwargs = {}
        for x in args:
            if isinstance(x, str):
                kwargs[x] = None
            elif isinstance(x, dict):
                validated_arg = validator_def(x)
                kwargs[validated_arg[const.CONF_NAME]] = validated_arg[const.CONF_ARGS]
    final_schema = crv.Schema({})
    for name, args in kwargs.items():
        if not ParameterValidators.validator_exists(name):
            raise crv.Invalid(
                "Combine validator expects a collection of schema based validators to merge. "
                "{} is not existing validator".format(name)
            )
        validator = ParameterValidators.validator_by_name(name)
        if isinstance(validator, typing.Callable):
            validator = ParameterValidators.validator_def_to_fn({const.CONF_NAME: name, const.CONF_ARGS: args})
        if isinstance(validator, ParamsHolder):
            validator = ParameterValidators.create_schema_for_param_def(validator.original_dict)
        if not isinstance(validator, crv.Schema):
            raise crv.Invalid(
                "Combine validator expects a collection of schema based validators to merge. "
                "{} is not existing validator".format(name)
            )
        final_schema = final_schema.extend(validator.schema)
    return final_schema


def actions_with_fallback(value):
    value = actions_with_fallback_schema(value)
    if isinstance(value, list):
        return actions_with_fallback_schema({const.CONF_DEFAULT: value})
    return value


mcp23017_address = helper.create_address_mapper(helper.MCP23017_ADDRESS_MAPPING)
pcf8574_address = helper.create_address_mapper(helper.PCF8574_ADDRESS_MAPPING)
ads1115_address = helper.create_address_mapper(helper.ADS1115_ADDRESS_MAPPING)
pca9685_address = helper.create_address_mapper(helper.PCA9685_ADDRESS_MAPPING)
