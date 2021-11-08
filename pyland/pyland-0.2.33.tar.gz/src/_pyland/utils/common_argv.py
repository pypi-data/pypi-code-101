# coding=utf8
from re import split
from argparse import ArgumentParser
from ..log import logger
from .support import socket_open
from ..config import Config


def url_http(ip, port):
    return "http://{}:{}".format(ip, port)


def ip_port(http_url):
    ip, port = split("[/ :]", http_url.strip("http://"))
    return ip, port


def check_server_argv(ip="127.0.0.1", port=8080):
    # 检查指定的IP端口是否连接正常，否则重新输入，更新IP、端口
    port = int(port)
    verify_server = input("检测到以下服务器信息\tIP:{}\tPort:{}\t是否重设IP/端口(yes/no): ".format(ip, port))
    if verify_server == "yes" or verify_server == "y":
        while True:
            ip = str(input("请输入服务IP地址："))
            port = int(input("请输入服务端口："))
            if ip and port:
                if socket_open(ip, port):
                    break
            else:
                logger.error("输入不合法，请重新输入！")
    return ip, port


def get_base_url(url_name='', index=0):
    # 从config/config.yaml读取IP和端口，读取不到则从命令行读取
    default_ip, default_port = "127.0.0.1", 8080
    default_url = url_http(default_ip, default_port)

    if url_name in locals().keys():
        local_url = locals()[url_name]
        logger.info("LOCAL {}: {}".format(url_name, local_url))
        return local_url
    else:
        arg = ArgumentParser("Test Tool.")
        arg.add_argument("--ip", default=default_ip, type=str, help="the ip of server.")
        arg.add_argument("--port", default=default_port, type=int, help="the port of server.")
        args = arg.parse_args()
        argv_url = url_http(args.ip, int(args.port))

        if argv_url == default_url:
            try:
                config_url = Config().get(url_name, index=index)
                if config_url:
                    logger.info("CONFIG {}: {}".format(url_name, config_url))
                    args.ip, args.port = ip_port(config_url)
                    return config_url
                else:
                    logger.error("config.yml missing defination of `{}`".format(url_name))
                    return False
            except:
                logger.info("not found config")
                re_ip, re_port = check_server_argv(args.ip, args.port)
                input_url = url_http(re_ip, re_port)
                logger.info("INPUT {}: {}".format(url_name, input_url))
                return input_url
        else:
            logger.info("ARGV {}: {}".format(url_name, argv_url))
            return argv_url

# VIDAPP_URL = get_base_url('XX_URL', index=0)
