import logging
import os.path
from functools import partial
from typing import Any

import configparser
import nacos
import hashlib

from ark.decrypt import decrypt

log = logging.getLogger("ark_config")
configs = dict(
    property={},
    cache=[]
)

ENV = None
PASSWORD = None


# 初始化配置
def init(address: str, namespace: str, group: str, data_ids=None, env=None, overwrite=None, root=None):
    if data_ids is None or len(data_ids) == 0:
        raise ValueError("data_ids不能为空")

    global ENV, PASSWORD
    ENV = env
    md = hashlib.md5()
    md.update((group + namespace).encode('utf-8'))
    PASSWORD = md.hexdigest()
    client = nacos.NacosClient(address, namespace=namespace)

    if root:
        if not os.path.exists(root):
            log.warn("not found root dir:%s" % root)
            os.makedirs(root)
        client.failover_base = os.path.join(root, client.failover_base)
        client.snapshot_base = os.path.join(root, client.snapshot_base)

    for data_id in data_ids:
        content = client.get_config(data_id, group=group, timeout=10)
        read(content)

    if overwrite:
        if isinstance(overwrite, str):
            overwrite = [overwrite]
        for file in overwrite:
            if root is not None and not file.startswith("/"):
                file = os.path.join(root, file)
            if not os.path.exists(file):
                log.warn("not found overwrite file:%s", file)
                continue
            with open(file, "r") as f:
                read(f.read())


# 加载配置
def read(content):
    if not content:
        return
    dft = "[DEFAULT]\n" + content
    cfg = configparser.ConfigParser()
    cfg.read_string(dft)
    config = cfg.defaults()
    configs['property'].update(config)


# 获取子节点下所有配置
def find(prefix: str, with_env: bool = False) -> dict:
    prefix = prefix.lower()
    data = {
        x[len(prefix) + 1:]: decrypt_config(configs['property'][x]) for x in configs['property'] if x.startswith(prefix)
    }
    if with_env:
        data = {ENV: data}

    return data


# 获取单个配置
def get(key: str, default: Any = None, is_int: bool = False, is_float: bool = False):
    key = key.lower()
    raw = configs['property'][key] if key in configs['property'] else default
    if raw is None:
        return raw
    raw = decrypt_config(raw)
    if is_int:
        raw = int(raw)
    elif is_float:
        raw = float(raw)

    return raw


get_int = partial(get, is_int=True, is_float=False)
get_float = partial(get, is_float=True, is_int=False)


def decrypt_config(val: str):
    if val is None or PASSWORD is None:
        return val

    if not val.startswith("ENC(") or not val.endswith(")"):
        return val

    return decrypt(PASSWORD, val[4:-1], 1000)


# 获取全部配置
def all_config():
    return configs['property']
