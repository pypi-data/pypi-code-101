import re

import demjson
from lxml import etree
import execjs
import requests


def resolve(direct_url, referer=None):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36',
    }
    resp = requests.get(direct_url, headers=headers)
    tree = etree.HTML(resp.text)
    post_id = tree.xpath('//div[@id="respond"]//p[@class="form-submit"]//input[@id="comment_post_ID"]/@value')[0]
    data = {
        'action': 'muvipro_player_content',
        'tab': 'player1',
        'post_id': post_id
    }
    resp1 = requests.post('http://194.163.152.200/wp-admin/admin-ajax.php', headers=headers, data=data,
                          verify=False)
    refer_url = re.findall(r'src="(.*?)"', resp1.text, re.S)[0]
    if 'https://s6.vidomo.xyz/' not in refer_url:
        print('无法播放')
    else:
        headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36',
            'referer': 'http://194.163.152.200/',
        }
        return requests.get(refer_url, headers=headers, stream=True)

        # if resp2.status_code == 200:
        #     eval_string = execjs.eval(re.search(r"eval\((.*)\)", resp2.text).group(1))
        #
        #     cxt = execjs.compile(r'''
        #                      String.prototype.decodeEscapeSequence = function() {
        #                          return this.replace(/\\x([0-9A-Fa-f]{2})/g, function() {
        #                             return String.fromCharCode(parseInt(arguments[1], 16));
        #                          });
        #                      };''')
        #
        #     eval_tostring = cxt.eval(r"'{}'.decodeEscapeSequence()".format(eval_string))  # 进制转换字符串
        #     play_url = re.compile('/mp4","(.*?)"', re.S).findall(eval_tostring)[0]