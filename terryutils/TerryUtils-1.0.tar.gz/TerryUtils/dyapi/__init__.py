import json
import time
import uuid
import random
import string
import hashlib
import requests
from hashlib import md5
from urllib import parse


class DyApi():
    def __init__(self):
        self.user_agent = 'com.ss.android.ugc.aweme/1260 (Linux; U; Android 7.0; zh_CN; MT2-L05; Build/LMY47V; Cronet/58.0.2991.0)'
        self.common_device_params = {
            'retry_type': 'no_retry',
            'ac': '4G',
            'channel': 'oppo',
            'aid': '1128',
            'app_name': 'aweme',
            'version_code': '1260',
            'version_name': '12.6.0',
            'device_platform': 'android',
            'ssmix': 'a',
            'device_type': 'MT2-L05',
            'device_brand': 'HUAWEI',
            'language': 'zh',
            'os_api': '22',
            'os_version': '7.0',
            'manifest_version_code': '1260',
            'resolution': '720*1280',
            'dpi': '320',
            'update_version_code': '126002',
        }

    def __get_ck(self):
        pass

    def get_sign(self, url, cookie="", data=""):
        sign_form_params = {
            'url': url,
            'cookie': cookie,
            'nosign': '1',
            'sdk-version': '1'
        }
        url = sign_form_params['url'].split('?')[-1]
        sign_resp = self.X_Gorgon(url, data, sign_form_params['cookie'])
        sign = {
            'X-Khronos': sign_resp['X-Khronos'],
            'X-Gorgon': sign_resp['X-Gorgon'],
            'X-Pods': ""
        }
        return sign

    def add_other_params(self, douyin_url, device_params, params=None):
        if params is None:
            params = {}

        if not douyin_url.__contains__('?'):
            douyin_url = douyin_url + '?'

        common_params = parse.urlencode(device_params)
        if douyin_url.endswith('?') or douyin_url.endswith('&'):
            douyin_url = douyin_url + common_params
        else:
            douyin_url = douyin_url + '&' + common_params

        if len(params) > 0:
            douyin_url = douyin_url + '&' + parse.urlencode(params)
        douyin_url = douyin_url + "&_rticket=" + str(int(round(time.time() * 1000))) + "&ts=" + str(int(time.time()))
        return douyin_url

    def get_cookie_str(self, cookie:dict):
        ret_list = []
        for k, v in cookie.items():
            ret_list.append(f'{k}={v}')
        return '; '.join(ret_list)

    def device_register(self, proxies, cookies=False):
        clientudid = str(uuid.uuid4())
        udid = self.genImeiLuhn('12345' + self.get_random(9))
        mc = self.get_random_mac()
        uuid_ = udid
        openudid = self.get_random(16)
        serial = self.stringRandom(16)
        sim_number = self.get_iccid()
        cdid = str(uuid.uuid4())
        oaid = self.stringRandom(16)
        req_id = str(uuid.uuid4())
        sid = str(uuid.uuid4())
        a = random.randint(13, 13)
        b = random.randint(1, 9)
        c = random.randint(1, 9)
        UA = "com.ss.android.ugc.aweme/{}0{}0{} (Linux; U; Android 10; zh_CN; MI 8; Build/QKQ1.190828.002; Cronet/TTNetVersion:79ab7988 2020-02-03 QuicVersion:ab76b766 2020-01-20)".format(
            a, b, c)
        Device_Info = {
            'address_book_access': '2',
            'ac': 'wifi',
            'channel': 'wandou_{}'.format(random.randint(1, 99999)),
            'aid': '1128',
            'app_name': 'aweme',
            'version_code': '{}0{}0{}'.format(a, b, c),
            'version_name': '{}.{}.{}'.format(a, b, c),
            'device_platform': 'android',
            'ssmix': 'a',
            'device_type': 'MI 8',
            'device_brand': 'Xiaomi',
            'language': 'zh',
            'os_api': '29',
            'os_version': '10',
            'manifest_version_code': '{}0{}0{}'.format(a, b, c),
            'resolution': '1080*2029',
            'dpi': '440',
            'update_version_code': '{}{}{}9900'.format(a, b, c),
            'app_type': 'normal',
            'mcc_mnc': '46000',
        }

        data = {"magic_tag": "ss_app_log",
                "header": {"display_name": "抖音短视频",
                           "update_version_code": Device_Info['update_version_code'],
                           "manifest_version_code": Device_Info['manifest_version_code'],
                           "app_version_minor": "", "aid": 1128,
                           "channel": Device_Info['channel'], "appkey": "57bfa27c67e58e7d920028d3",
                           "package": "com.ss.android.ugc.aweme",
                           "app_version": Device_Info['version_name'], "version_code": Device_Info['version_code'],
                           "sdk_version": "2.10.1-rc.18-setIntervalThrowable",
                           "sdk_target_version": 29, "git_hash": "de5f3e3f", "os": "Android",
                           "os_version": Device_Info['os_version'], "os_api": Device_Info['os_api'],
                           "device_model": "MI 8",
                           "device_brand": "Xiaomi", "device_manufacturer": "Xiaomi",
                           "cpu_abi": "armeabi-v7a", "build_serial": serial,
                           "release_build": "61bcf69_20200414_230b06ac-7e00-11ea-b990-02420a000052",
                           "density_dpi": 480, "display_density": "mdpi", "resolution": "2029x1080",
                           "language": "zh", "mc": mc, "timezone": 8, "access": "wifi",

                           "not_request_sender": 0, "rom": "56481939456", "rom_version": "miui_V11_V11.0.8.0.QEACNXM",
                           "cdid": cdid,
                           "sig_hash": "aea615ab910015038f73c47e45d21466",
                           # "google_aid":"a25cfa22-29c9-4d4e-b2fb-7126c5528a46",
                           "openudid": openudid, "clientudid": cdid,
                           "serial_number": serial, "sim_serial_number": [],
                           "region": "CN", "tz_name": "Asia/Shanghai", "tz_offset": 28800,
                           "oaid_may_support": False, "req_id": req_id,
                           "custom": {"filter_warn": 0,
                                      "web_ua": "Mozilla/5.0 (Linux; Android 6.0.1; Nexus 5 Build/M4B30Z; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/44.0.2403.117 Mobile Safari\/537.36"},
                           "apk_first_install_time": 1603265630295, "is_system_app": 0, "sdk_flavor": "china"},
                "_gen_time": 1603266073118}
        params = {
            'cdid': cdid,
            'openudid': openudid,
            'uuid': uuid_,
            '_rticket': str(time.time() * 1000)[:13],
            'ts': str(time.time() * 1000)[:10],
            # 'ttdata'
        }

        params.update(Device_Info)
        p = self.url_encode(params)
        xgorgon = self.X_Gorgon(p, '', '')
        headers = {'User-Agent': UA,
                   'X-SS-STUB': self.md5(json.dumps(data)),
                   'X-Khronos': xgorgon['X-Khronos'],
                   'X-Gorgon': xgorgon['X-Gorgon'],
                   # 'Content-Type': 'application/json; charset=utf-8'
                   }
        url = 'https://log.snssdk.com/service/2/device_register/?' + p
        # de_data = gzip.compress(bytes(json.dumps(data), encoding="utf8"))
        res = requests.post(url=url, data=json.dumps(data), headers=headers, proxies=proxies, timeout=10)
        resp = res.json()
        resp = {'device_id': str(resp['device_id']), 'iid': str(resp['install_id']), 'uuid': uuid_,
                'openudid': openudid, }
        if resp['device_id'] == '0':
            return
        param_check = {'build_serial': serial, 'timezone': '8.0',
                       'carrier': '中国移动', 'mcc_mnc': Device_Info['mcc_mnc'],
                       'sim_region': 'cn', 'sim_serial_number': sim_number,
                       'device_id': resp['device_id'], 'ac': 'wifi', 'channel': Device_Info['channel'],
                       'aid': '1128', 'app_name': 'aweme', 'version_code': Device_Info['version_code'],
                       'version_name': Device_Info['version_name'],
                       'device_platform': 'android', 'ssmix': 'a', 'device_type': Device_Info['device_type'],
                       'device_brand': Device_Info['device_brand'], 'language': 'zh', 'os_api': Device_Info['os_api'],
                       'os_version': Device_Info['os_version'],
                       'uuid': uuid_, 'openudid': openudid,
                       'manifest_version_code': Device_Info['manifest_version_code'],
                       'resolution': Device_Info['resolution'], 'dpi': '440',
                       'update_version_code': Device_Info['update_version_code'],
                       '_rticket': str(time.time() * 1000)[:13],
                       'app_type': 'normal', 'ts': str(time.time() * 1000)[:10], 'cdid': cdid,
                       'host_abi': 'armeabi-v7a',
                       'oaid': oaid, 'req_id': req_id}
        p = self.url_encode(param_check)
        url_check = "https://ichannel.snssdk.com/service/2/app_alert_check/?" + p

        xgorgon = self.X_Gorgon(p, '', '')
        headers_check = {'User-Agent': UA,
                         'X-Khronos': xgorgon['X-Khronos'],
                         'X-Gorgon': xgorgon['X-Gorgon'],
                         'X-SS-REQ-TICKET': str(time.time() * 1000)[:13],
                         }
        r = requests.get(url=url_check, headers=headers_check, proxies=proxies, timeout=10)
        resp.update(Device_Info)
        if cookies:
            cookie = res.cookies.get_dict()
            resp.update({"UA": UA,
                         "mc": mc,
                         'oaid': oaid,
                         'cookies': cookie,
                         "cdid": cdid})
        return resp, UA

    def md5(self, str):
        m = hashlib.md5()
        b = str.encode(encoding='utf-8')
        m.update(b)
        str_md5 = m.hexdigest()
        return str_md5

    def get_iccid(self):
        m = random.randint(0, 9)
        ss = random.randint(10, 31)
        yy = random.randint(15, 20)
        g = random.randint(100, 500)
        iccid = '898600{m}{m}{ss}{yy}5103{g}'.format(m=m, ss=ss, yy=yy, g=g)
        # print(iccid)
        return iccid

    def genImeiLuhn(self, digits14):
        digit15 = 0
        for num in range(14):
            if num % 2 == 0:
                digit15 = digit15 + int(digits14[num])
            else:
                digit15 = digit15 + (int(digits14[num]) * 2) % 10 + (int(digits14[num]) * 2) / 10
        digit15 = int(digit15) % 10
        if digit15 == 0:
            digits14 = digits14 + str(digit15)
        else:
            digits14 = digits14 + str(10 - digit15)
        return digits14

    def get_random(self, len):
        return ''.join(str(random.choice(range(10))) for _ in range(len))

    def get_random_mac(self):
        """
        随机mac地址
        :return:
        """
        mac = [0x10, 0x2a, 0xb3,
               random.randint(0x00, 0x7f),
               random.randint(0x00, 0xff),
               random.randint(0x00, 0xff)]
        return ':'.join(map(lambda x: "%02x" % x, mac))

    def stringRandom(self, n):
        return ''.join(random.sample('abcdef' * 10 + string.digits * 10, n))

    def url_encode(self, data):
        param = parse.urlencode(data)
        param = param.replace("+", "%20")
        param = param.replace("%2A", "*")
        return param

    def hex_string(self, num):
        tmp_string = hex(num)[2:]
        if len(tmp_string) < 2:
            tmp_string = '0' + tmp_string
        return tmp_string

    def reverse(self, num):
        tmp_string = self.hex_string(num)
        return int(tmp_string[1:] + tmp_string[:1], 16)

    def RBIT(self, num):
        result = ''
        tmp_string = bin(num)[2:]
        while len(tmp_string) < 8:
            tmp_string = '0' + tmp_string
        for i in range(0, 8):
            result = result + tmp_string[7 - i]
        return int(result, 2)

    def X_Gorgon(self, url, data, cookie):
        gorgon = ''
        url_md5 = md5(bytearray(url, 'utf-8')).hexdigest()
        gorgon += url_md5
        if data:
            data_md5 = md5(bytearray(data, 'utf-8')).hexdigest()
            gorgon += data_md5
        else:
            gorgon += '00000000000000000000000000000000'
        if cookie:
            cookie_md5 = md5(bytearray(cookie, 'utf-8')).hexdigest()
            gorgon += cookie_md5
        else:
            gorgon += '00000000000000000000000000000000'
        gorgon += '00000000000000000000000000000000'
        return self.calc_xg(gorgon)

    def calc_xg(self, data):
        ts = int(time.time())
        len = 0x14
        key = [0xDF, 0x77, 0xB9, 0x40, 0xb9, 0x9b, 0x84, 0x83, 0xd1, 0xb9, 0xcb, 0xd1, 0xf7, 0xc2, 0xb9, 0x85, 0xc3,
               0xd0,
               0xfb, 0xc3]
        param_list = []
        for i in range(0, 12, 4):
            temp = data[8 * i: 8 * (i + 1)]
            for j in range(4):
                H = int(temp[j * 2:(j + 1) * 2], 16)
                param_list.append(H)
        param_list.extend([0x0, 0x6, 0xB, 0x1C])
        H = int(hex(ts), 16)
        param_list.append((H & 0xFF000000) >> 24)
        param_list.append((H & 0x00FF0000) >> 16)
        param_list.append((H & 0x0000FF00) >> 8)
        param_list.append((H & 0x000000FF) >> 0)
        eor_result_list = []
        for A, B in zip(param_list, key):
            eor_result_list.append(A ^ B)
        for i in range(len):
            C = self.reverse(eor_result_list[i])
            D = eor_result_list[(i + 1) % len]
            E = C ^ D
            F = self.RBIT(E)
            H = ((F ^ 0xFFFFFFFF) ^ len) & 0xFF
            eor_result_list[i] = H
        result = ''
        for param in eor_result_list:
            result += self.hex_string(param)
        xgorgon = '0408b0d30000' + result
        return {'X-Gorgon': xgorgon, 'X-Khronos': str(ts)}



