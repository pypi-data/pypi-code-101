# -*- coding: utf-8 -*-
from meutils.pipe import *
from meutils.request_utils.crawler import Crawler
from docx import Document
from docx.oxml.ns import qn
from datetime import datetime, date, time, timedelta
from lxml import etree
import requests
import os
import shutil
from docxtpl import DocxTemplate

# 获取当前日期
nowTime = datetime.now()
now = nowTime.date()  # 2020-09-19
# 昨天
prevDayTime = nowTime + timedelta(days=-5)
prevDayDate = prevDayTime.date().strftime('%Y-%m-%d')

han_num = ["零", "一", "二", "三", "四", "五", "六", "七", "八", "九", "十",
           "十一", "十二", "十三", "十四", "十五", "十六", "十七", "十八", "十九", "二十",
           "二十一", "二十二", "二十三", "二十四", "二十五", "二十六", "二十七", "二十八", "二十九", "三十"]
filePath = "files_test/"
filename = "合规日报(" + prevDayTime.strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日') + ").docx"

data_sources = [
    {"category": "监管动态", "sources": [
        {"name": "证监会要闻", "url": "http://www.csrc.gov.cn/pub/newsite/zjhxwfb/xwdd/",
         "href_prefix_url": "http://www.csrc.gov.cn/pub/newsite/zjhxwfb/xwdd/"},
        {"name": "新闻发布会", "url": "http://www.csrc.gov.cn/pub/newsite/zjhxwfb/xwfbh/",
         "href_prefix_url": "http://www.csrc.gov.cn/pub/newsite/zjhxwfb/xwfbh/"},
        {"name": "机关部门最新更新", "url": "http://www.csrc.gov.cn/pub/newsite/zxgx/jigbsdt/",
         "href_prefix_url": "http://www.csrc.gov.cn/pub/"},
        {"name": "派出机构最新更新", "url": "http://www.csrc.gov.cn/pub/newsite/zxgx/pcjgdt/",
         "href_prefix_url": "http://www.csrc.gov.cn/pub/"},
        {"name": "机构部-证券公司“白名单”", "url": "http://www.csrc.gov.cn/pub/newsite/zqjjjgjgb/zqgsbmd/",
         "href_prefix_url": "http://www.csrc.gov.cn/pub/newsite/zqjjjgjgb/zqgsbmd/"},
    ]}
]


def calc_href(_href):
    if _href.startswith("./"):
        return _href.replace("./", "")
    elif _href.startswith("../../../"):
        return _href.replace("../../../", "")
    else:
        return _href


# 获取网页的标题列表
def get_titles(_url):
    crawler = Crawler(_url)
    _titles = []
    _lis = crawler.xpath('//*[@id="myul"]//li') or crawler.xpath('//*[@class="fl_list"]//li')
    for _li in _lis:
        time = _li.xpath("span//text()")[0].strip()
        # 如果发布时间不是昨天的，就放弃,继续下一次循环
        if prevDayDate != time:
            continue
        title = _li.xpath("a//text()")[0]
        _titles.append(title)
    # 获取title对应的文本内容
    return _titles


def get_contents(_url, _prefix_url):
    crawler = Crawler(_url)
    # 获取title对应的a网址连接
    _hrefs = []
    _lis = crawler.xpath('//*[@id="myul"]//li') or crawler.xpath('//*[@class="fl_list"]//li')
    for _li in _lis:
        time = _li.xpath("span//text()")[0].strip()
        # 如果发布时间不是昨天的，就放弃,继续下一次循环
        if prevDayDate != time:
            continue
        href = _li.xpath("a//@href")[0]
        _hrefs.append(href)
    _href_urls = list(map(lambda _href: _prefix_url + calc_href(_href), _hrefs))
    _contents = []
    _a_items = []
    # 获取href链接的网址内容
    for _hrefs_url in _href_urls:
        crawler = Crawler(_hrefs_url)
        _content = crawler.xpath("""//*[@class="Custom_UnionStyle"]//text()""") or crawler.xpath(
            """//*[@class="content"]//p//text()""")
        # 一些链接的内容也要添加进去
        _a_items_str = "".join(crawler.xpath("""//script//text()"""))
        _a_items_2 = "".join(list(map(lambda a: etree.tostring(a, encoding="utf-8").decode("utf-8"),
                                      crawler.xpath("""//*[@class="content"]//a"""))))
        print(_hrefs_url)
        print(crawler.xpath("""//*[@class="content"]//a"""))
        print(_a_items_2)
        _a_items = re.compile(r'<a\b[^>]*>.+?</a>').findall(_a_items_str)
        # 理由etree.HTML，将字符串解析成html
        # print("_a_items", "".join(_a_items) + _a_items_2)
        _a_items = etree.HTML("".join(_a_items) + _a_items_2)
        # _contents.append("".join(_content) + "\n".join(_a_items))  # 将内容列表合并成一个长字符串
        # _contents.append("".join(_content))
        # 如果链接的列表不为空，判断是不是pdf附件，如果是，要下载到附件中
        _content = "".join(_content)
        text_ele_need = []
        if _a_items:
            a_eles = _a_items.xpath("//a")
            for a_ele in a_eles:
                # print(etree.tostring(a_ele, encoding="utf-8").decode("utf-8"))
                text = a_ele.xpath("//text()")[0]
                path = calc_href(a_ele.xpath("@href")[0])
                if (text.endswith(".pdf") or text.endswith(".xlsx")
                    or text.endswith(".xls")) and text not in text_ele_need:
                    text_ele_need.append(text)
                    _content = _content + "\n" + text
                    # _contents.append("\n" + text)
                    # 下载pdf附件
                    pdf_download = _hrefs_url[0:_hrefs_url.rfind("/")] + "/" + path
                    response = requests.get(pdf_download)
                    if not os.path.exists(filePath + '/附件/'):
                        os.makedirs(filePath + '/附件/')
                    with open(filePath + '/附件/' + text, 'wb') as f:
                        f.write(response.content)
        _contents.append(_content + "\n")
    return _contents


if __name__ == "__main__":
    if os.path.exists(filePath):  # 如果文件存在
        # 强制删除文件，可使用以下两种方法。
        shutil.rmtree(filePath)
    if not os.path.exists(filePath):
        os.makedirs(filePath)

    print(prevDayDate)

    results = []
    # 写入内容
    for data_index, data_source in enumerate(data_sources):
        category = data_source["category"]
        sources = data_source["sources"]

        titles = []
        contents = []
        for source_index, source in enumerate(sources):
            name = source["name"]
            url = source["url"]
            href_prefix_url = source["href_prefix_url"]
            # 获取这个网址下的标题列表titles
            titles = titles + get_titles(url)
            contents = contents + get_contents(url, href_prefix_url)

        titles_new = []
        contents_new = []
        for title_index, title in enumerate(titles):
            titles_new.append(han_num[title_index + 1] + "、" + title)
        for content_index, content in enumerate(contents):
            content = "\n".join(filter(None, contents[content_index].split("\n"))) + "\n"
            content = "\u3000".join(filter(None, content.split("\u3000"))) + "\u3000"
            contents_new.append(content)
        print(titles_new)
        print(contents_new)
        result = {
            "category": "第" + han_num[data_index + 1] + "部分 " + category,
            "titles": titles_new,
            "contents": contents_new
        }
        results.append(result)

        # 设置要使用的模板
        doc = DocxTemplate('templates/tpl.docx')
        # 添加数据
        context = {'results': results, "date": prevDayTime.strftime('%Y{y}%m{m}%d{d}').format(y='年', m='月', d='日')}
        doc.render(context)
        # 保存文件
        doc.save(filePath + filename)
