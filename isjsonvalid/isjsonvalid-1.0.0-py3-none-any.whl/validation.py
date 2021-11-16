import json

from isjsonvalid.helpers import (
    createError,
    formatErrors,
    handleFallbacks,
    validateExistence,
    validateType,
    validationHasFailed,
)


def validate(data, validator):
    validation, errors = _validate(data, validator)
    if not validation:
        raise ValueError(json.dumps(errors))


def _validate(data, validator, errors=None):
    errors = errors or {}
    success = {}
    keys = validator.keys()
    for key in keys:

        # Validate Existence
        if not validateExistence(data, validator, errors, key):
            continue

        # Validate Type
        if not validateType(data, validator, errors, key):
            continue

        ## Custom Validation
        validation_function = validator[key].get("validator", None)
        if validation_function:

            try:
                valid = validation_function(data[key])
            except:
                valid = False

            if valid:
                success[key] = validator[key]
            else:
                createError(
                    key,
                    f"Incorrect value for {key}",
                    errors,
                    validator[key].get("fallback", None),
                )
                continue

        ## Choices Validation
        one_of_list = validator[key].get("one_of", None)
        if one_of_list and data[key] not in one_of_list:
            createError(
                key,
                f"Value for {key} must be one of {str(validator[key]['one_of'])}",
                errors,
                validator[key].get("fallback", None),
            )
            continue

        ## Dictionary Validation
        if validator[key].get("type", None) == dict:
            keys_validator = validator[key].get("keys", {})
            key_success, key_errors = _validate(data[key], keys_validator)
            if not key_success:
                errors[key] = key_errors
            continue

        ## List Validation
        if validator[key].get("type", None) == list:
            elements = data[key]

            ## List Length Validation
            length = len(elements)
            min_length = validator[key].get("min_length", 0)
            max_length = validator[key].get("max_length", float("inf"))

            if length < min_length or length > max_length:
                createError(
                    key,
                    f"{key} should contain at least {min_length} elements, with a max of {max_length}",
                    errors,
                    validator[key].get("fallback", None),
                )

            ## List Elements Validation
            element_validator = validator[key].get("element_validator", None)
            if element_validator:
                for element in elements:

                    try:
                        element_success = element_validator(element)
                    except:
                        element_success = False

                    if not element_success:
                        createError(
                            key,
                            f"{key} contains invalid elements.",
                            errors,
                            validator[key].get("fallback", None),
                        )
                        break
            continue

    handleFallbacks(errors, success)

    if validationHasFailed(errors):
        formatErrors(errors, validator)
        return False, errors

    return True, None
