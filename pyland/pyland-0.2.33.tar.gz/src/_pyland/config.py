"""
读取配置。采用yaml格式配置文件，也可以采用xml、ini等，需要在file_rader添加响应Reader处理。
❗️ 注意：基础脚本【config， support】，不能import更高级的脚本如logger， Sql
"""
import sys
import os
from .utils.file_reader import (
    YamlReader,
    JsonReader,
    RawReader
)
from .utils.file_writer import (
    YamlWriter,
    JsonWriter,
    RawWriter
)
from .utils.support import (
    to_list,
    eval_param,
    get_suffix_list
)

__all__ = [
    "BASE_PATH",
    "Config",
    "YamlParam",
    "com_params"
]

# current workspace path
# BASE_PATH = os.path.split(os.path.dirname(os.path.abspath(__file__)))[0]
BASE_PATH = os.getcwd()


def is_base(pathname):
    # condition: BASE_PATH must have a sub-dir named with `data` and `test_suits`
    _data_path = os.path.join(pathname, 'data')
    _tests_path = os.path.join(pathname, 'test_suits')
    if os.path.isdir(_data_path) and os.path.isdir(_tests_path):
        return True
    else:
        return False


class Config:
    """
    get/put data from/to yaml/json/text
    Config(): default use ${workspace}/config/config.yml
    Config('api_config.yml'): use ${workspace}/config/api_config.yml
    Config('testAPI/interface/mod_2_video/test.yml'): use ${workspace}/testAPI/interface/mod_2_video/test.yml
    Config('/usr/data/images'): use /usr/data/images
    """

    def __init__(self, config='config.yml', index=0, path=None):
        """
        :param config: the config file path,
            - if absolute path like `/xx/config.yml`, will directly use it
            - if relative path like `xx/config.yml`, will Relative to the current workspace
            - if file name like `config.yml`, will Relative to the `config` foler in current worspace
            - if empty, will Relative to the `config/config.yml` foler in current worspace
        :param path: change workspace path
            - accept absolute/relative path
            - affect the variable DATA_PATH/LOG_PATH/CONFIG_PATH/REPORT_PATH and so on.
            - if config is abspath, will still use the config abspath
        :param index: yaml index
        """
        # use current workspace path as default BASE_PATH
        self.BASE_PATH = os.getcwd()

        # when path set, use path as BASE_PATH
        if path:
            if os.path.isdir(path):
                self.BASE_PATH = os.path.abspath(path)
            elif os.path.isfile(path):
                self.BASE_PATH = os.path.abspath(os.path.dirname(path))

        if is_base(self.BASE_PATH):
            # print(f"has found BASE_PATH: {self.BASE_PATH}")
            pass
        else:
            # print("try using config file to locate base path")
            _cfg_path = os.path.dirname(os.path.abspath(config))
            _base_path = os.path.dirname(_cfg_path)
            if os.path.isdir(os.path.join(_cfg_path, 'data')):
                self.BASE_PATH = _cfg_path
            if os.path.isdir(os.path.join(_base_path, 'data')):
                self.BASE_PATH = _base_path
        #
        # if path and os.path.isdir(path):
        #     self.BASE_PATH = os.path.abspath(path)
        #     sys.path.extend([self.BASE_PATH])
        #     # os.chdir(self.BASE_PATH)
        #     print(f"path: {path}\n{sys.path}\n{os.getcwd()}")
        # else:
        #     self.BASE_PATH = os.getcwd()

        self.CONFIG_PATH = os.path.join(self.BASE_PATH, 'config')
        self.DATA_PATH = os.path.join(self.BASE_PATH, 'data')
        self.LOG_PATH = os.path.join(self.BASE_PATH, 'log')
        self.REPORT_PATH = os.path.join(self.BASE_PATH, 'report')
        self.CONFIG_FILE = os.path.join(self.CONFIG_PATH, 'config.yml')
        self.DRIVERS_PATH = os.path.join(self.BASE_PATH, 'drivers')
        self.RESULT_PATH = os.path.join(self.BASE_PATH, "allure-result")

        self.COMMON_PATH = os.path.join(self.BASE_PATH, "common")
        sys.path.insert(0, self.COMMON_PATH)
        sys.path.insert(0, self.BASE_PATH)

        self.abspath = ''

        if config.startswith("/"):
            self.abspath = config
        elif '/' in config:
            self.abspath = os.path.join(self.BASE_PATH, config)
        else:
            self.abspath = os.path.join(self.CONFIG_PATH, config)

        try:
            self.config = self.get(index=index)
        except Exception as e:
            self.config = None

    def get(self, element=None, index=0):
        """
        get config element
        :param element: yaml element
        :param index: yaml is separated to lists by '---'
        :return:
        """
        try:
            self.config = YamlReader(self.abspath).data[index]
        except Exception as e:
            raise Exception("Yaml read error")

        if element:
            res = self.config.get(element)
        else:
            res = self.config
        return res

    def global_var(self, index=0):
        """
        Be careful! Transfer yaml key to global var name
        :return:
        """
        if index:
            self.config = YamlReader(self.abspath).data[index]

        for key in sorted(self.config.keys()):
            globals()[key] = self.config[key]

    def json_get(self):
        """get data from json file"""
        json_data = JsonReader(self.abspath).data
        return json_data

    def json_put(self, json_obj, abspath=None):
        """put json object to json file"""
        abspath = self.abspath if not abspath else abspath
        self.touch(abspath)
        JsonWriter(json_obj, self.abspath)

    def json_update(self):
        pass

    def raw_get(self):
        raw_data = RawReader(self.abspath).data
        return raw_data

    def raw_put(self, raw_obj):
        RawWriter(raw_obj, self.abspath)

    @classmethod
    def touch(cls, abspath):
        """When writing a file, to ensure that the path and files exist."""
        dirname = os.path.dirname(abspath)
        os.makedirs(dirname, exist_ok=True)
        with open(abspath, 'a'):
            os.utime(abspath, None)

    @classmethod
    def put(cls, yaml_obj, abspath):
        """Write the YAML format object to a new YAML file (overwritten)"""
        Config.touch(abspath)
        YamlWriter(yaml_obj, abspath, overwrite=True)

    @classmethod
    def update(cls, yaml_obj, abspath=None):
        """Write the YAML format object to an old YAML file (append)"""
        try:
            dest = YamlReader(abspath).data[0]
            if isinstance(dest, list) and isinstance(yaml_obj, list):
                YamlWriter(yaml_obj, abspath, overwrite=False)
            elif isinstance(dest, dict) and isinstance(yaml_obj, dict):
                dest.update(yaml_obj)
                YamlWriter(dest, abspath, overwrite=True)
            else:
                raise ValueError("Try to write different types of data to YAML files, please check! ")
        except FileNotFoundError:
            cls.put(yaml_obj, abspath)


VALID_TYPE = 'valid'
INVALID_TYPE = 'invalid'


class YamlParam(Config):
    """
    Read and Format Input Param from config
    """

    @staticmethod
    def parse_by_case_type(original_data, type=VALID_TYPE):
        # transfer `{a: {valid: []}, b: {valid: []}}` to `{a: [], b: []}`
        original_data = eval_param(original_data)
        param = {}
        param_list = []
        missing_type = "Pyland_Missing_" + type

        if isinstance(original_data, dict):
            type_value = original_data.get(type)
            if type_value:
                type_value = to_list(type_value)
                param_list = YamlParam.parse_by_case_type(type_value, type)
                return param_list
            else:
                # condition of missing the type key
                if VALID_TYPE in original_data or INVALID_TYPE in original_data:
                    return missing_type
                for key in original_data.keys():
                    _value = YamlParam.parse_by_case_type(original_data.get(key), type)
                    if _value != missing_type:
                        param[key] = _value
                return param

        elif isinstance(original_data, list):
            for value in original_data:
                param = YamlParam.parse_by_case_type(value, type)
                param_list.append(param)
            return param_list
        else:
            return original_data

    @staticmethod
    def dict_value_to_list(src_dict: dict):
        """
        To transfer a dict to a permutation lists
        :param src_dict: {key1: [a1,a2], key2: [b1,b2,b3], key3:[c1]}
        :return: [[a1,b1,c1], [a2,b2,c1], [a2,b3,c1]]
        """
        res = []
        over_key = set()
        while len(over_key) < len(src_dict):
            lr = len(res)
            res_i = {}
            for key in src_dict.keys():
                # ensure the value list is this format: [value]
                if src_dict[key] and isinstance(src_dict[key], list):
                    value_list = src_dict[key]
                elif src_dict[key] and isinstance(src_dict[key], dict):
                    value_list = YamlParam.dict_value_to_list(src_dict[key])
                else:
                    value_list = [src_dict[key]]

                # combine valid params
                if lr < len(value_list) - 1:
                    res_i[key] = value_list[lr]
                else:
                    over_key.add(key)
                    res_i[key] = value_list[-1]

                # disable key if value is 'x'
                if res_i[key] == 'x':
                    res_i.pop(key)
            if res_i not in res:
                res.append(res_i)
        return res

    @staticmethod
    def replace_json_with_dict(src_dict: dict, json: dict) -> list:
        """
        To combine yml wrong params with the template
        :param src: {arg1: [1,2,3]}
        :param json: {arg1: 0, arg2:9}
        :return: [{arg1: 1, arg2:9},{arg1: 2, arg2:9},{arg1: 3, arg2:9}]
        """
        res = []
        for key in src_dict.keys():
            # ensure the value list is this format: [value]
            if src_dict[key] and isinstance(src_dict[key], list):
                value_list = src_dict[key]
            elif src_dict[key] and isinstance(src_dict[key], dict):
                value_list = YamlParam.replace_json_with_dict(src_dict[key], json[key])
            else:
                value_list = [src_dict[key]]

            for val in value_list:
                tmp = json.copy()
                tmp[key] = val

                # disable key if value is 'x'
                if val == 'x':
                    tmp.pop(key)

                if tmp not in res:
                    res.append(tmp)
        return res

    def valid_params(self, element):
        """
        Get a combined valid data field list
        """
        # ele_valid = self.get(element).get('valid')
        ele = self.get(element)
        ele_valid = self.parse_by_case_type(ele, type='valid')
        if ele_valid and isinstance(ele_valid, dict):
            ele_valid = self.dict_value_to_list(ele_valid)
        self.ele_valid = ele_valid
        return self.ele_valid

    def invalid_params(self, element, template_file=None):
        """
        Get a combined invalid data field list
        """
        # ele_invalid = self.get(element).get('invalid')
        ele = self.get(element)
        ele_invalid = self.parse_by_case_type(ele, type='invalid')
        if ele_invalid and isinstance(ele_invalid, dict):
            try:
                if template_file:
                    template = Config(template_file).json_get()
                elif self.valid_params(element) and isinstance(self.ele_valid[-1], dict):
                    template = self.ele_valid[-1]
                ele_invalid = self.replace_json_with_dict(ele_invalid, template)
            except Exception as e:
                raise e
        self.ele_invalid = ele_invalid
        return self.ele_invalid

    def combined_params(self):
        """
        Combine all PARAMs under this YML file, generate _combined_xx.yml file
        :return: its dictionary format data
        """
        res = {}
        try:
            all_params = self.config
            if not all_params:
                raise Exception("yaml read failed. check the yaml format")
            for key in all_params.keys():
                if key.startswith("param"):
                    valid = self.valid_params(key)
                    invalid = self.invalid_params(key)
                    res.update({f"{key}_valid": valid, f"{key}_invalid": invalid})
                    if valid == invalid:
                        res.update({f"{key}": all_params[key]})
                else:
                    res.update({f"{key}": all_params[key]})
            original_path = os.path.split(self.abspath)
            out_path = os.path.join(original_path[0], "_combined_" + original_path[1])
            self.put(res, out_path)
        except Exception as e:
            raise e
        return res


def com_params(yaml_files_list=None, path=None, strict=True):
    """
    :param path: find all yml files in this path
    :param yaml_files_list: read data from a list of yaml file abspaths
    :param strict: when files contain duplicated keys,
        if True, will raise error;
        if False, will use the last value of last file
    :return: an input parameter dictionary according to the list of YAML files
    """
    if path:
        if not os.path.isdir(path):
            return None
        if yaml_files_list:
            if isinstance(yaml_files_list, str):
                yaml_files_list = [yaml_files_list]
            if isinstance(yaml_files_list, list):
                yaml_files_list = [os.path.join(path, i) for i in yaml_files_list if isinstance(i, str)]
        else:
            yaml_files_list = get_suffix_list(path, suffix=".yml")
    else:
        if not yaml_files_list or not isinstance(yaml_files_list, list):
            return None

    param_dict = {}
    for file in yaml_files_list:
        yp = YamlParam(file)
        combined = yp.combined_params()
        if strict:
            for key in combined.keys():
                if param_dict.get(key):
                    raise ValueError(f"Duplicated Key {key} found, please check")
        param_dict.update(combined)
    return param_dict


def com_params_obj(yaml_files_list=None, path=None, strict=True, obj=None):
    """
    :param path: find all yml files in this path
    :param yaml_files_list: read data from a list of yaml file abspaths
    :param strict: when files contain duplicated keys,
        if True, will raise error;
        if False, will use the last value of last file
    :return: an object which has attributes same with yaml keys `param_***`
    """
    param_dict = com_params(yaml_files_list=yaml_files_list, path=path, strict=strict)
    if obj:
        params_obj = obj
    else:
        params_obj = Params() 
    objDictTool.to_obj(params_obj, **param_dict)
    return params_obj


class objDictTool:
    """to change a dict to an object, or change an object to a dict"""

    @staticmethod
    def to_obj(obj: object, **data):
        obj.__dict__.update(data)

    @staticmethod
    def to_dic(obj):
        dic = {}
        for fieldkey in dir(obj):
            fieldvaule = getattr(obj, fieldkey)
            if not fieldkey.startswith("__") and not callable(fieldvaule) and not fieldkey.startswith("_"):
                dic[fieldkey] = fieldvaule
        return dic


class Params():
    """ store all the params as an object"""
    pass

# def auto_combine_params(path=BASE_PATH):
#     yaml_files_list = get_suffix_list(path, suffix=".yml")
#     return com_params(yaml_files_list)


# # combine params automatically
# BASE_PATH = os.path.dirname(os.path.abspath(__file__))
# PARAM_PATH = os.path.join(BASE_PATH, "data/input_loads")
# COMBINED_PARAMS = auto_combine_params(PARAM_PATH)
