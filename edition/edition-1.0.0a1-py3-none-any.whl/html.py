def to_anchor(value: str) -> str:
    a = ""
    value = value.replace(" ", "-")
    for c in value:
        if c == "-":
            a += c.lower()
            continue

        if not str.isalnum(c):
            continue
        a += c.lower()
    return a
