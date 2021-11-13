# -*- coding: utf-8 -*-
from urllib.parse import urlparse, parse_qs
import json
import re
import os
from pathlib import PureWindowsPath, PurePosixPath

import requests
from bs4 import BeautifulSoup
import pandas as pd
from PyQt5.QtCore import *

from idebug import *
from ipylib.ipath import *

from youtubeplayer.Lib import *


__all__ = [
    'Y2MateBrowser',
]


class Y2MateBrowser(BaseQWorker):
    searched = pyqtSignal()
    converted = pyqtSignal()
    ajax_done = pyqtSignal()

    @funcIdentity
    def __init__(self):
        super().__init__()

    @property
    def dl_path(self):
        return self._dl_path
    @property
    def filename(self):
        return self._title

    def set_dlpath(self, p):
        self._dl_path = clean_path(p)
    def set_filename(self, s):
        s = '' if s is None else s
        # [Windows|MacOS] 에서 지원하지 않는 파일명에 대한 청소
        s = re.sub('[\s]+', repl=' ', string=s)
        s = re.sub('[:\|\?\*"\<\>/]+', repl='#', string=s)
        # print('title:', s)
        self._title = s

    @funcIdentity
    def search(self, url):
        # url: 유투브 영상 URL
        # PartGubun('search')
        o = urlparse('https://suggestqueries.google.com/complete/search?jsonp=jQuery340004144273343421623_1635056106020&q=https%3A%2F%2Fyoutu.be%2Fc9h5VloOhCc%3Flist%3DTLPQMjQxMDIwMjEgBM7O0V7Bvg&hl=en&ds=yt&client=youtube&_=1635056106021')
        # print(o)
        qs = parse_qs(o.query)
        # pp.pprint(qs)
        o = o._replace(query='')
        # print(o)

        # 입력받은 유투브URL을 qs객체에 업데이트
        self.yt_url = url
        yt = urlparse(self.yt_url)
        # print(yt)
        param = {k:v[0] for k,v in qs.items()}
        param['q'] = self.yt_url
        # pp.pprint(param)
        # print('geturl:', o.geturl())
        r = requests.get(o.geturl(), param)
        # dbg.dict(r)
        # print(r.text, type(r.text))
        self.searched.emit()

    @funcIdentity
    def ajax(self):
        # PartGubun('Ajax')
        url = 'https://www.y2mate.com/mates/en105/analyze/ajax'
        qs = parse_qs('url=https%3A%2F%2Fyoutu.be%2FagnV2YjuzSM%3Flist%3DPLP9YOa5MTwu06to2NmlacATe-zEXHUOTw&q_auto=0&ajax=1')
        # print(qs)
        data = {k:v[0] for k,v in qs.items()}
        data['url'] = self.yt_url
        r = requests.post(url, data)
        # dbg.dict(r)

        # SectionGubun('Response-Data')
        d = json.loads(r.text)
        # pp.pprint(d)

        # SectionGubun('HTML파싱')
        soup = BeautifulSoup(d['result'], 'html.parser')
        # print(soup.prettify())

        s = soup.find('div', class_='caption text-left').b.get_text().strip()
        # print('title:', s)
        self.set_filename(s)

        # print(soup.input.attrs)
        self.data_id = soup.input.attrs['data-id']

        # SectionGubun('KData 추출')
        s = soup.find('script', attrs={'type':'text/javascript'})
        # print(s.get_text())
        li = s.get_text().split(';')
        li = [e.strip() for e in li if len(e.strip()) > 0]
        d = {}
        for e in li:
            m = re.search('var\s([a-z_]+)\s=\s"(.+)"', e)
            d.update({m[1]:m[2]})
        # pp.pprint(d)
        self.KData = d
        self.ajax_done.emit()

    @funcIdentity
    def fetch_img(self):
        # PartGubun('이미지 저장')
        self.imgDL = Downloader(self.dl_path)
        url = f'https://i.ytimg.com/vi/{self.data_id}/0.jpg'
        filename = f"{self.filename}.jpg"
        self.imgDL.get(url, filename)
        logger.info(f'{self} | File Path--> {self.imgDL.fpath}')

    @funcIdentity
    def xc(self):
        # PartGubun('xc')
        r = requests.get('https://habeglee.net/s9np/xc')
        # dbg.dict(r)
        d = json.loads(r.text)
        # pp.pprint(d)

    @funcIdentity
    def convert(self):
        # PartGubun('convert')
        qs = parse_qs('type=youtube&_id=5e9b86ec7527f838068b4591&v_id=agnV2YjuzSM&ajax=1&token=&ftype=mp3&fquality=128')
        qs['_id'] = self.KData['k__id']
        qs['v_id'] = self.KData['k_data_vid']
        r = requests.post('https://www.y2mate.com/mates/convert', data=qs)
        # dbg.dict(r)
        d = json.loads(r.text)

        # SectionGubun('HTML파싱')
        soup = BeautifulSoup(d['result'], 'html.parser')
        # print(soup.prettify())
        href = soup.find('a').attrs['href']
        # print('href:', href)
        # o = urlparse(href)
        # print(o)
        self.mp3_url = href
        self.converted.emit()

    @funcIdentity
    def download(self):
        # PartGubun('MP3파일 다운로드')
        self.DL = Downloader(self.dl_path)
        self.DL.finished.connect(self.Done)
        filename = f"{self.filename}.mp3"
        self.DL.get(self.mp3_url, filename)

    @funcIdentity
    def get_mp3(self, url):
        self.searched.connect(self.ajax)
        self.ajax_done.connect(self.fetch_img)
        self.ajax_done.connect(self.convert)
        self.converted.connect(self.download)
        self.search(url)

    @funcIdentity
    def Done(self):
        logger.info(f'{self} | File Path--> {self.DL.fpath}')
        self.finished.emit()
