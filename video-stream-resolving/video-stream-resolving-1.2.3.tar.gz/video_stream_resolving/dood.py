import re

import requests
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS = 'ALL'


def resolve(embed_url, referer=None):
    """
    :param embed_url: This params only accept url which host is dood.to, doodstream.com or dood.watch
    :param referer:
    :return:
    """
    # TODO: dood 应是封禁了 python requests 的指纹， 最好的办法还是用无头浏览器

    video_id = embed_url.split("/")[-1]

    # headers = {
    #     'authority': 'dood.to',
    #     'accept': '*/*',
    #     'x-requested-with': 'XMLHttpRequest',
    #     'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Mobile Safari/537.36',
    #     'sec-fetch-site': 'same-origin',
    #     'sec-fetch-mode': 'navigate',
    #     'sec-fetch-dest': 'iframe',
    #     'referer': 'https://dood.to/d/$id',
    #     'accept-language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7'
    # }
    headers = {
        "Accept": "*/*",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
    }
    response = requests.get(f"https://dood.to/e/{video_id}", headers=headers, proxies={"https": "http://localhost:8866"}, verify=False)
    video_base_url = re.search(r"(?<=\')/pass_md5.*(?=\')", response.text)

    request_code = """
let https = require('https')
let options = {
  hostname: 'dood.to',
  port: 443,
  path: '/e/5xl5c8djmc4z',
  method: 'GET'
}

let req = https.request(options, res => {
  console.log(`状态码: ${res.statusCode}`)

  res.on('data', d => {
    process.stdout.write(d)
  })
})

req.on('error', error => {
  console.error(error)
})

req.end()
    """
