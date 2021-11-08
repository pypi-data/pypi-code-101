# coding=utf8
# import allure
# import pytest
# import json
# from time import sleep
# from utils.extractor import extract
# # from testAPI.interface.image_stock import ImageStock
# # from testAPI.suite.test_suits.conftest import param_new_image
# from utils.sql import Sql
# from testAPI.suite.test_suits.conftest import *
# from utils.config import YamlParam, BASE_PATH
# from testAPI.suite.test_suits.test_11_attribute import env_add_attribute
# from testAPI.suite.test_suits.test_13_image import map_image_param
# import os


# def map_attribute_id(group_params):
#     # 把 group params 中的所有 attribute name 转化为 id
#     for group_param in group_params:
#         if isinstance(group_param["attributes"], list):
#             for attribute in group_param["attributes"]:
#                 if isinstance(attribute, dict) and attribute.get("id"):
#                     attribute["id"] = env_add_attribute(attribute["id"])
#     return group_params
#
#
# attribute_group_yml = 'data/input_loads/image_stock/image.yml'
# yp = YamlParam(attribute_group_yml)
# param_get_attribute_groups_valid = [tuple(i) for i in yp.valid_params("param_get_attribute_groups")]
# param_get_attribute_groups_invalid = [tuple(i) for i in yp.invalid_params("param_get_attribute_groups")]
# x = yp.invalid_params("param_add_attribute_group")
# param_add_attribute_group_valid = map_attribute_id(x)
# param_add_attribute_group_invalid = yp.invalid_params("param_add_attribute_group")
# param_get_attribute_group_valid = yp.valid_params("param_get_attribute_group")
# param_get_attribute_group_invalid = yp.invalid_params("param_get_attribute_group")
# param_edit_attribute_group_valid = yp.valid_params("param_edit_attribute_group")
# param_edit_attribute_group_invalid = yp.invalid_params("param_edit_attribute_group")
# param_delete_attribute_group_valid = yp.valid_params("param_delete_attribute_group")
# param_delete_attribute_group_invalid = yp.invalid_params("param_delete_attribute_group")
#
# param_add_attribute_group_invalid_special = yp.dict_value_to_list(yp.get('param_add_attribute_group_invalid_special'))
#
# print(param_add_attribute_group_valid)

# param_search_image_valid = yp.invalid_params("param_search_image")
# print(param_search_image_valid)

#
#
#
#
# param_add_image_valid = map_image_param(yp.valid_params("param_add_image"))
# param_add_image_invalid = map_image_param(yp.invalid_params("param_add_image"))
# param_get_image_valid = yp.valid_params("param_get_image")
# param_get_image_invalid = yp.invalid_params("param_get_image")
# param_edit_image_valid = map_image_param(yp.valid_params("param_edit_image"))
# param_edit_image_invalid = map_image_param(yp.invalid_params("param_edit_image"))
# param_delete_image_valid = yp.valid_params("param_delete_image")
# param_delete_image_invalid = yp.invalid_params("param_delete_image")
#
# param_search_image_valid = map_image_param(yp.valid_params("param_search_image"))
# param_search_image_invalid = map_image_param(yp.invalid_params("param_search_image"))
#
# print(param_add_image_valid)
# print(param_add_image_invalid)
# print(param_get_image_valid)
# print(param_get_image_invalid)
# print(param_edit_image_valid)
# print(param_edit_image_invalid)
# print(param_delete_image_valid)
# print(param_delete_image_invalid)

# param_search_image_special_nogroup_invalid = yp.invalid_params("param_search_image_special_nogroup")

# param_mass_upload_image_special_zip = yp.invalid_params("zip", template_file="data/templates/image_stock_mass_upload_image.json")
# mass_upload_zip_path = BASE_PATH + "data/mass_images"
# param_zip_path = [os.path.join(BASE_PATH, "data/mass_images", i) for i in yp.valid_params("zip")]
# mass_template = Config("data/templates/image_stock_mass_upload_image.json").json_get()
# print(param_zip_path[0].split('/')[-1][:30])
# print(mass_template)

#
# def db_attribute_group_info(attribute_id):
#     sql = Sql('sql_dl')
#     query_content = f'SELECT name, data_type, extra_data FROM image_stock_attribute_tab ' \
#                     f'WHERE id = {attribute_id};'
#     name, data_type, extra_data = sql.query(query_content)[0]
#     sql.close()
#     possible_values = json.loads(extra_data).get('possible_values')
#     attribute_info = {'name': name, 'data_type': data_type, 'possible_values': possible_values}
#     return attribute_info
#
#
# def pre_attribute_group_id(api, original_name='test_for_api'):
#     # prepare data: add attribute_id to edit
#     original_json = {"name": original_name, "data_type": 1}
#     sql = Sql('sql_dl')
#     query_content = f'SELECT id FROM image_stock_attribute_tab WHERE name = \'{original_name}\';'
#     if not sql.query(query_content):
#         api.new_attribute_group(json=original_json)
#     else:
#         api.attribute_id = sql.query(query_content)[0][0]
#     sql.close()
#
#
# @allure.severity('blocker')
# @allure.feature('ImageStock')
# @allure.story('Attributes')
# class TestAttributeGroup(object):
#
#     @allure.title('Get Attribute Groups Valid')
#     @pytest.mark.parametrize('offset, limit', param_get_attribute_groups_valid)
#     def test_get_attribute_groups_valid(self, offset, limit):
#         istk = ImageStock()
#         response = istk.list_groups(offset, limit)
#
#         res_attributes = extract("result.attribute_groups", response)
#         res_total = extract("result.total", response)
#         res_req = []
#         if res_attributes:
#             for req in res_attributes:
#                 id = req.get("id")
#                 name = req.get("name")
#                 res_req.append((id, name))
#
#         sql = Sql('sql_dl')
#         query_content = f'SELECT id, name FROM image_stock_attribute_group_tab ' \
#                         f'ORDER BY id DESC LIMIT {limit} OFFSET {offset};'
#         res_db = sql.query(query_content)
#         total = len(sql.query('SELECT id, name FROM image_stock_attribute_group_tab '))
#         sql.close()
#         assert set(res_req) == set(res_db)
#         assert res_total == total
#
#     @allure.title('Get Attributes Invalid')
#     @pytest.mark.parametrize('offset, limit', param_get_attribute_groups_invalid)
#     def test_get_attribute_groups_invalid(self, offset, limit):
#         istk = ImageStock()
#         response = istk.list_groups(offset, limit, status='FAIL')
#
#         req_status = extract("success", response)
#         assert req_status is False


#
# import json
#
# def env_get_image_info_from_db(image_id):
#     # 根据image id，在数据库中查找图片json信息
#     TABLENAME = "image_stock_image_tab_00000" + str(image_id % 1000)
#     ID = image_id // 1000
#     res_image_info = {}
#     sql = Sql('sql_dl')
#     query_image_id = f'SELECT name, hash, width, height, extension, attribute_group_id, extra_data ' \
#                      f'FROM {TABLENAME} ' \
#                      f'WHERE id = {ID}'
#     name, image_hash, width, height, extension, attribute_group_id, extra_data = sql.query(query_image_id)[0]
#     res_image_info['name'] = name
#     res_image_info['hash'] = image_hash
#     res_image_info['attribute_group_id'] = attribute_group_id
#     res_image_info['extension'] = extension
#     res_image_info['width'] = width
#     res_image_info['height'] = height
#     res_image_info['attributes'] = []
#
#     if extra_data:
#         attributes = json.loads(extra_data)["attributes"]
#         logger.info(attributes)
#         for attribute in attributes:
#             attr = {}
#             attr['id'] = attribute['id']
#             attr['value'] = attribute['value']
#             res_image_info['attributes'].append(attr)
#
#     sql.close()
#     return res_image_info
#
#
# print(env_get_image_info_from_db(1734))
#
# from src.api.utils.config import Config
#
# con = Config()
# print(con.get())

# data = '{"live_account_info": {"is_host": False, "is_banned": True}, "editable_username": False, "is_semi_inactive": True, "already_verified_phone": True, "gender": 1, "adult_consent": 1603289583, "tos_accepted_time": 1600757444, "access": {"wallet_setting": 1, "wallet_provider": 1}, "feed_account_info": {"can_post_feed": True}, "nickname": "Stonegogo"}'
#
# data = '{"live_account_info": {"is_host": "False", "is_banned": "True"}, "editable_username": "False", "is_semi_inactive": "True", "already_verified_phone": "True", "gender": 1, "adult_consent": 1603289583, "tos_accepted_time": 1600757444, "access": {"wallet_setting": 1, "wallet_provider": 1}, "feed_account_info": {"can_post_feed": "True"}, "nickname": "Stonegogo"}'
#
#
# data_1 = "{'live_account_info': " \
#          "{'is_host': False, 'is_banned': True}, " \
#          "'editable_username': False, 'is_semi_inactive': True, " \
#          "'already_verified_phone': True, 'gender': 1, 'adult_consent': 1603289583, 'tos_accepted_time': 1600757444, " \
#          "'access': {'wallet_setting': 1, 'wallet_provider': 1}, 'feed_account_info': {'can_post_feed': True}, " \
#          "'nickname': u'Stonegogo'}"

#
# info = json.loads(data)data_1
# print(type(info))

# data = eval(data_1)
# print(type(data))
# print(data)
# info = json.loads(eval(data_1))
# print(type(info))
#
#
# [
#             {
#                 "userid": 10661,
#                 "username": "bbbcccc",
#                 "shopid": 10661,
#                 "shop_name": "b",
#                 "logo": "7c1358eb1b0a57d9203fe631884d8d41",
#                 "logo_pc": "33ea569be630c8e5d86b1b4723f9f18a",
#                 "shop_collection_id": 0,
#                 "ctime": 1606905556,
#                 "brand_label": 1
#             },
#             {
#                 "userid": 10661,
#                 "username": "bbbcccc",
#                 "shopid": 10661,
#                 "shop_name": "b",
#                 "logo": "7c1358eb1b0a57d9203fe631884d8d41",
#                 "logo_pc": "33ea569be630c8e5d86b1b4723f9f18a",
#                 "shop_collection_id": 0,
#                 "ctime": 1606905556,
#                 "brand_label": 1
#             },
#             {
#                 "userid": 10661,
#                 "username": "bbbcccc",
#                 "shopid": 10661,
#                 "shop_name": "b",
#                 "logo": "7c1358eb1b0a57d9203fe631884d8d41",
#                 "logo_pc": "33ea569be630c8e5d86b1b4723f9f18a",
#                 "shop_collection_id": 0,
#                 "ctime": 1606905556,
#                 "brand_label": 1
#             },
#             {
#                 "userid": 10661,
#                 "username": "bbbcccc",
#                 "shopid": 10661,
#                 "shop_name": "b",
#                 "logo": "7c1358eb1b0a57d9203fe631884d8d41",
#                 "logo_pc": "33ea569be630c8e5d86b1b4723f9f18a",
#                 "shop_collection_id": 0,
#                 "ctime": 1606905556,
#                 "brand_label": 1
#             },
#             {
#                 "userid": 10661,
#                 "username": "bbbcccc",
#                 "shopid": 10661,
#                 "shop_name": "b",
#                 "logo": "7c1358eb1b0a57d9203fe631884d8d41",
#                 "logo_pc": "33ea569be630c8e5d86b1b4723f9f18a",
#                 "shop_collection_id": 0,
#                 "ctime": 1606905556,
#                 "brand_label": 1
#             },
#             {
#                 "userid": 10661,
#                 "username": "bbbcccc",
#                 "shopid": 10661,
#                 "shop_name": "b",
#                 "logo": "7c1358eb1b0a57d9203fe631884d8d41",
#                 "logo_pc": "33ea569be630c8e5d86b1b4723f9f18a",
#                 "shop_collection_id": 0,
#                 "ctime": 1606905556,
#                 "brand_label": 1
#             },
#             {
#                 "userid": 10661,
#                 "username": "bbbcccc",
#                 "shopid": 10661,
#                 "shop_name": "b",
#                 "logo": "7c1358eb1b0a57d9203fe631884d8d41",
#                 "logo_pc": "33ea569be630c8e5d86b1b4723f9f18a",
#                 "shop_collection_id": 0,
#                 "ctime": 1606905556,
#                 "brand_label": 1
#             },
#             {
#                 "userid": 0,
#                 "username": "",
#                 "shopid": 10101,
#                 "shop_name": "blueshkblue",
#                 "logo": "7c1358eb1b0a57d9203fe631884d8d41",
#                 "logo_pc": "33ea569be630c8e5d86b1b4723f9f18a",
#                 "shop_collection_id": 0,
#                 "ctime": 1606905532,
#                 "brand_label": 1
#             },
#             {
#                 "userid": 0,
#                 "username": "",
#                 "shopid": 11330,
#                 "shop_name": "Testwj102",
#                 "logo": "7c1358eb1b0a57d9203fe631884d8d41",
#                 "logo_pc": "33ea569be630c8e5d86b1b4723f9f18a",
#                 "shop_collection_id": 0,
#                 "ctime": 1606905582,
#                 "brand_label": 1
#             }
#         ]


# def sql_condition_generate(sql_str, condition):
#     """根据条件，产生数据库查询条件语句"""
#     if not condition:
#         return
#
#     condition_list = []
#     condition_param = []
#
#     if condition["name"]:
#         _ = str(condition["name"]).strip()
#         if condition["IsFuzzy"]:
#             condition_list.append("INSTR(name, {})")
#             condition_param.append(repr(_))
#         else:
#             condition_list.append("name = {}")
#             condition_param.append(repr(_))
#
#     if condition["attribute_group_name"]:
#         _ = str(condition["attribute_group_name"]).strip()
#         if condition["IsFuzzy"]:
#             condition_list.append("INSTR(attribute_group_name, {})")
#             condition_param.append(repr(_))
#         else:
#             condition_list.append("attribute_group_name = {}")
#             condition_param.append(repr(_))
#
#     if condition["status"]:
#         _ = str(condition["status"]).strip()
#         if condition["IsFuzzy"]:
#             condition_list.append("INSTR(status, {})")
#             condition_param.append(repr(_))
#         else:
#             condition_list.append("status = {}")
#             condition_param.append(repr(_))
#
#     if condition["id"]:
#         _ = str(condition["id"]).strip()
#         condition_list.clear()  # id享有最高唯一筛选权，且不支持模糊搜索
#         condition_list.append("id = {}")
#         condition_param.clear()
#         condition_param.append(repr(_))
#
#     if len(condition_list) > 0:
#         sql_str += " WHERE " + " AND ".join(condition_list)
#
#     if condition["OrderBy"]:
#         _ = str(condition["OrderBy"]).strip()
#         sql_str += f" ORDER BY repr(_)"
#         if condition["IsDesc"]:
#             sql_str += " DESC"
#
#     if condition["Limit"]:
#         _ = str(condition["Limit"]).strip()
#         sql_str += f" LIMIT repr(_)"
#
#     if condition["Offset"]:
#         _ = str(condition["Offset"]).strip()
#         sql_str += f" OFFSET repr(_)"
#
#     sql_str = sql_str.format(*condition_param) + ";"
#     return sql_str
#
#
# def list_images_by_filter(id, attribute, group, status, offset, limit):
#     """
#     通过各种条件，从数据库检索
#     """
#
#     query_base = "SELECT `id`, `name` FROM image_stock_mass_upload_tab"
#
#     ImageFilterCondition = {
#         "id": id,
#         "name": attribute,
#         "attribute_group_name": group,
#         "status": status,
#         "Limit": limit,
#         "Offset": offset,
#         "IsFuzzy": True,
#         "OrderBy": "",
#         "IsDesc": True
#     }
#
#     query_content = sql_condition_generate(query_base, ImageFilterCondition)
#     print(query_content)
#
#
# list_images_by_filter(0, "\'", "_ \" ", "", 0, 0)


# 待确认需求：
# #所有输入是否必须字符串，不是字符串如何处理，prefix/postfix如果为空该怎样处理，最终返回结果是否去重

# 需考虑情况（测试用例）：
# string空值，返回空
# prefix空值，postfix有值：要么只返回所有postfix本身（如果存在），要么返回所有从第一个字符开始到所有postfix的子串，要么返回所有以postfix结尾的子串
# postfix空值，prefix有值：要么只返回所有prefix本身（如果存在），要么返回所有从所有prefix开始到最后一个字符的子串，要么返回所有以prefix开头的子串
# prefix和postfix都是空，返回string本身，或者返回空
# prefix和postfix相同，这个值本身也要返回
# 要考虑prefix/postfix本身是重复字符的情形（所以要逐个字符比较）
# 要考虑prefix结尾和postfix开头有重复字符，包含与被包含等交叉重复情况

# 设计思路：
# string为空，返回空；string首先必须既包含prefix又包含postfix，否则可以直接返回空
# 在string中分别找到两个子串的位置索引列表（子串在string种的开始索引和结束索引）
# 当prefix的开始索引和结束索引都小于等于postfix的开始索引和结束索引时，取prefix开始索引和postfix结束索引之间的字符串即可


# def index_substring(string, substring, step=0):
#     try:
#         index = string.index(substring)
#         string = string[index + 1:]
#         next_index = index_substring(string, substring, index + step + 1)
#         index_list = [index + step]
#         index_list.extend(next_index)
#         return index_list
#     except:
#         return []
#
#
# def query_substring(string, prefix='', postfix=''):
#     if not string or not isinstance(string, str) or not isinstance(prefix, str) or not isinstance(postfix, str):
#         return []
#     if prefix not in string or postfix not in string:
#         return []
#     if not prefix:
#         prefix_index = range(len(string))  # prefix_index = [0], or raise Error
#     else:
#         prefix_index = index_substring(string, prefix)
#     if not postfix:
#         postfix_index = range(len(string))  # postfix_index = [len(string)], or raise Error
#     else:
#         postfix_index = index_substring(string, postfix)
#     # prefix_index = index_substring(string, prefix) if prefix else range(len(string))
#     # postfix_index = index_substring(string, postfix) if postfix else range(len(string))
#
#     subs = []
#     for pre in prefix_index:
#         for post in postfix_index:
#             pre_end = pre + len(prefix)
#             post_end = post + len(postfix)
#             if pre <= post and pre_end <= post_end:
#                 sub = string[pre:post_end]
#                 subs.append(sub)
#
#     subs = list(set(subs))
#     return subs
#
#
# print(index_substring("abababbbaaab", "1"))
#
# print(query_substring("abababbbabaaab", "bab", "ab"))



# 登陆认证

# import requests
# from google_auth_oauthlib.flow import Flow

url = "https://dl-admin.test.shopee.sg/api/v2/shop_campaign/cd_item/list?limit=10&offset=0"
# cookies = {"SSO_C": "s-7455nsCgG-J2TuvRPRvAli"}
# res = requests.get(url)
# #
# print(res.content)


# def get_redirect_url(url):
#     # 请求头，这里我设置了浏览器代理
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'}
#     # 请求网页
#     response = requests.get(url, headers=headers)
#     print(response.status_code)  # 打印响应的状态码
#     print(response.url)  # 打印重定向后的网址
#     # 返回重定向后的网址
#     return response.url
#
# redirect_uri = get_redirect_url(url)
#
# redirect_uri = get_redirect_url(redirect_uri)
#
# flow = Flow.from_client_secrets_file(
#     'client_secret_454252940472-g1qrhi6bmamkaqrn0tjbvelg8i5jht2b.apps.googleusercontent.com.json',
#     scopes=['profile', 'email'],
#     redirect_uri="https://soup.test.shopee.io/login/oauth2callback")
#
# authorization_url, state = flow.authorization_url(
#     access_type='offline',
#     include_granted_scopes='true')
# print(authorization_url)
# print(flow.redirect_uri)

# flow.fetch_token(authorization_response=authorization_url)

# res = requests.post(authorization_url, data=)
#
#
# app = flask.Flask(__name__)
#
# @app.route('/oauth2callback')
# def oauth2callback():
#     state = flask.session['state']
#     flow = Flow.from_client_secrets_file(
#         'client_secret_454252940472-g1qrhi6bmamkaqrn0tjbvelg8i5jht2b.apps.googleusercontent.com.json',
#         scopes=['https://dl-admin.test.shopee.sg'],
#         redirect_uri=flask.url_for('oauth2callback', _external=True),
#         state=state)
#
#     authorization_response = flask.request.url
#     flow.fetch_token(authorization_response=authorization_response)
#
#     credentials = flow.credentials
#     print(credentials)
#     return flask.redirect(flask.url_for('test_api_request'))
#
#
#
# from google_auth_oauthlib.flow import InstalledAppFlow
#
# flow = InstalledAppFlow.from_client_secrets_file(
#     'client_secret_454252940472-g1qrhi6bmamkaqrn0tjbvelg8i5jht2b.apps.googleusercontent.com.json',
#     scopes=['profile', 'email'])
#
# flow.run_local_server()

from os import path

# from src.pyland import config
#
# print(config.BASE_PATH)
#

# def ss():
#     from src.pyland.config import Config
#
#     print(Config().BASE_PATH)

# import sys
# sys.path.append("..")
# from config import Config
#
# print(Config().BASE_PATH)

# ss()



