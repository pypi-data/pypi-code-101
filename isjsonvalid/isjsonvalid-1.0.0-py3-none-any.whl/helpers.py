

def createError(name, cause, errors, fallback=None):
    if name not in errors.keys():
        errors[name] = {}
        errors[name]["cause"] = cause
        if fallback:
            errors[name]["fallback"] = fallback


def validateExistence(data, validator, errors, key):
    key_exists = key in data.keys()
    is_required = validator[key].get("required", False)
    if not key_exists and is_required:
        createError(
            key,
            f"Missing value for {key}",
            errors,
            validator[key].get("fallback", None),
        )
        return False
    elif not key_exists:
        return False
    return True


def validateType(data, validator, errors, key):
    valid_type = validator[key].get("type", None)
    value_type = type(data[key])
    if valid_type:

        if type(valid_type) not in (list, tuple, set):
            valid_type = [valid_type]

        if value_type not in valid_type:
            createError(
                key,
                f"Incorrect type value for {key}",
                errors,
                validator[key].get("fallback", None),
            )
            return False

    return True


def formatErrors(errors, validator):
    for key in list(errors.keys())[:]:

        if key not in validator:
            continue

        hint = validator[key].get("hint", None)

        errors[key]["hint"] = hint or ""


def validationHasFailed(errors):
    return len(list(errors.keys())[:]) > 0


def handleFallbacks(errors, success):
    for key in list(errors.keys())[:]:
        fallback = errors[key].get("fallback", None)
        if fallback and fallback in success.keys():
            del errors[key]
        elif fallback:
            del errors[key]["fallback"]

