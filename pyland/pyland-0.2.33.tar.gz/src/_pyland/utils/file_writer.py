# coding=utf8
from yaml import dump as y_dump
from json import dump as j_dump


class YamlWriter(object):
    def __init__(self, yaml_obj, yaml_file, overwrite=False):
        if isinstance(yaml_obj, dict) or isinstance(yaml_obj, list):
            if overwrite:
                with open(yaml_file, "w") as f:
                    y_dump(yaml_obj, f, default_flow_style=False)
            else:
                with open(yaml_file, "a") as f:
                    y_dump(yaml_obj, f, default_flow_style=False)
        else:
            raise ValueError("只接受字典写入YAML文件,或列表追加YAML文件")


class JsonWriter(object):
    def __init__(self, json_obj, json_file):
        if isinstance(json_obj, dict):
            with open(json_file, "w") as f:
                j_dump(json_obj, f)
        else:
            raise ValueError("只接受字典写入JSON文件")


class RawWriter(object):
    def __init__(self, raw_obj, raw_file):
        with open(raw_file, "w") as f:
            f.write(raw_obj)


if __name__ == "__main__":
    import yaml
    with open("../api/config/config.yml", "r") as yaml_file:
        yaml_obj = yaml.load(yaml_file.read())
        print(yaml_obj)
    yaml_obj["sql_data1"]["sql_port"] = 1234
    with open("../api/config/config.yml", "w") as f:
        y_dump(yaml_obj, f, default_flow_style=False)