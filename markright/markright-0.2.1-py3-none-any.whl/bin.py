def main():
    import argparse
    ap = argparse.ArgumentParser(description="Templateless markdown template engine (CLI)")
    ap.add_argument("-f", "--file", type=str, required=True, help="Destination file")
    ap.add_argument("-d", "--data", type=str, required=True, help="Data source: JSON string or path file (json or ini)")

    args = ap.parse_args()

    data = args.data
    dest = args.file

    import json
    model = None
    try:
        model = json.loads(data)
    except ValueError:
        try:
            with open(data, "r") as file:
                model = json.load(file)
        except (ValueError, IOError):
            from configparser import ConfigParser
            config = ConfigParser()
            try:
                config.read(data)
                model = config["markright"]
            except KeyError:
                raise SystemExit("Data source is corrupt")

    replacer = {}
    for key in model:
        value = model[key]
        if not isinstance(value, (str, int, bool)):
            raise SystemExit(f"Data source is corrupt: {key} -> {value}")
        replacer[key] = str(value)

    from markright import mark
    try:
        mark(dest, replacer)
    except IOError:
        raise SystemExit(f"Destinaton file {dest} is corrupt")

    import os
    print(f"Markright {os.path.abspath(dest)} success!")


if __name__ == "__main__":
    main()
