import json
from os.path import abspath
SEX_NOVEL_DOMAIN = "http://www.yulinzhanye4.com"
TOTAL_PAGE = 1329
with open('%s/../config/novel.json' % abspath(__file__), 'r', encoding='utf-8') as fp:
    NOVEL_CONFIG=json.load(fp)

NOVEL_PATH=NOVEL_CONFIG.get('novel_path')
