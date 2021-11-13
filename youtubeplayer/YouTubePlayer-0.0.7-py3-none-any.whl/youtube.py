# -*- coding: utf-8 -*-
from urllib.parse import urlparse, parse_qs
import json
import re
import os
from pathlib import PureWindowsPath, PurePosixPath
import itertools
from time import sleep

import requests
from bs4 import BeautifulSoup
import pandas as pd

from idebug import *
from ipylib.ipath import *

from youtubeplayer.Lib import *
from youtubeplayer.database import *
from youtubeplayer.y2mate import *


__all__ = [
    'YoutubePlaylistDB',
    'YouTubePlayList',
    'YouTubeMusicDownLoader',
    'YouTubeMusicPlayer'
]

class YoutubePlaylistDB:

    mdb = {
        'L-Bachata':'https://www.youtube.com/watch?v=QFs3PIZb3js&list=PLP9YOa5MTwu06to2NmlacATe-zEXHUOTw&ab_channel=RomeoSantosVEVO'
    }
    @classmethod
    def find(self, keyword):
        p = re.compile(keyword, flags=re.I)
        for k,v in self.mdb.items():
            if p.search(k) is not None:
                return v

class YouTubePlayList(BaseQWorker):

    @funcIdentity
    def __init__(self):
        super().__init__()
        self.model = Collection('YouTubePlayList')
        self.finished.connect(self.done)
    @funcIdentity
    def fetch(self, keyword):
        # 검색어에 해당하는 플레이리스트의 정보를 수집(DB저장 포함)한다.
        url = YoutubePlaylistDB.find(keyword)
        if url is None:
            logger.info(f"{self} | '{keyword}'에 해당하는 플레이리스트가 존재하지 않는다")
        else:
            r = requests.get(url)
            # dbg.dict(r)
            # SectionGubun('HTML파싱')
            soup = BeautifulSoup(r.text, 'html.parser')
            # print(soup.prettify())

            s = soup.find('script', string=re.compile('var ytInitialData'))
            # print(s.prettify())

            txt = s.get_text().strip()
            txt = re.sub('^var ytInitialData = ', repl='', string=txt)
            txt = re.sub(';$', repl='', string=txt)
            txt = re.sub('\s+', repl=' ', string=txt)
            # print(txt)

            d = json.loads(txt)
            # 핵심정보
            d = d['contents']['twoColumnWatchNextResults']['playlist']['playlist']
            # print('len(d):', len(d))
            # print('d.keys:', list(d.keys()))
            logger.debug(f'{self} | {len(d)}')
            logger.debug(f'{self} | {list(d.keys())}')
            self._contentsPlaylist = d

            SectionGubun('JSON_Normalize',2)
            # print('self.Contents:', type(self.Contents), len(self.Contents))
            logger.debug(f'{self} | Contents--> {[type(self.Contents), len(self.Contents)]}')
            data = []
            for e in self.Contents:
                data.append(e['playlistPanelVideoRenderer'])
            df = pd.json_normalize(data)
            # print(df)
            # df.info()
            logger.debug(f'{self} | Normalized DataFrame-->\n{df}')


            for c in sorted(df.columns):
                SectionGubun(f'col: {c}',2)
                # print(df[c])
                # logger.debug(f'{self} | df[{c}]-->\n{df[c]}')
                if c == 'videoId':
                    self._videoIds = list(df[c])
                elif c == 'title.simpleText':
                    pp.pprint(list(df[c]))
                elif c == 'title.accessibility.accessibilityData.label':
                    pp.pprint(list(df[c]))

            _nameMap = {'videoId':'vid','title.simpleText':'smpl_title','title.accessibility.accessibilityData.label':'full_title'}
            df = df.rename(columns=_nameMap)
            df = df.reindex(columns=list(_nameMap.values()))
            logger.debug(f'{self} | Meaningful DataFrame-->\n{df}')

            # DB저장
            for d in df.to_dict('records'):
                f = {'_id':d['vid']}
                self.model.update_one(f, {'$set':d}, True)
            self.finished.emit()
    @funcIdentity
    def Done(self):
        pass

    @property
    def PlayListId(self): return self._contentsPlaylist['playlistId']
    @property
    def PlayListTitle(self): return self._contentsPlaylist['title']
    @property
    def Contents(self): return self._contentsPlaylist['contents']
    @property
    def VideoIds(self): return self._videoIds
    @property
    def DownloadTarget(self):
        return self.model.distinct('vid', {'downloaded':{'$in':[None,False]}})

    @funcIdentity
    def mark_downloaded(self, vid):
        self.model.update_one({'vid':vid}, {'$set':{'downloaded':True}})
    @funcIdentity
    def view(self):
        pretty_title('플레이리스트')
        pp.pprint(self.model.distinct('full_title'))
    @funcIdentity
    def get_title(self, vid):
        try: return self.model.distinct('full_title',{'vid':vid})[0]
        except Exception as e: return None

class MusicFileHandler(BaseQWorker):

    @funcIdentity
    def __init__(self):
        super().__init__()
    @property
    def dl_path(self):
        return self._dl_path
    @funcIdentity
    def set_dlpath(self, path=None):
        if path is None:
            if os.name == 'nt': path = 'C:/Users/innovata/Music'
            elif os.name == 'posix': path = '/Users/sambong/Music'

        p = clean_path(path)
        self._dl_path = p
        # 해당 경로가 존재하지 않으면 강제로 생성한다
        if not os.path.exists(p): os.makedirs(p)
        return self

class YouTubeMusicDownLoader(BaseQWorker):

    @funcIdentity
    def __init__(self, PlayList, vid):
        super().__init__()
        self.playlist = PlayList # YouTubePlayList
        self.vid = vid
        self.fhandler = MusicFileHandler()
        self.y2mate = Y2MateBrowser()
        # 다운로드경로 자동셋팅
        self.set_dlpath(None)

    @funcIdentity
    def run(self):
        title = self.playlist.get_title(self.vid)
        PartGubun(f'스레드 시작--> {title}')
        try:
            url = f'https://youtu.be/{self.vid}?list={self.playlist.PlayListId}'
            # print(self.playlist.PlayListTitle, self.vid, url)
            logger.info(f'{self} | {[self.playlist.PlayListTitle, title, url]}')

            self.y2mate.finished.connect(self.close)
            self.y2mate.get_mp3(url)
        except Exception as e:
            logger.error(f'{self} | {e}')
            raise
        self.started.emit()
    @funcIdentity
    def close(self):
        self.playlist.mark_downloaded(self.vid)
        self.finished.emit()

    @funcIdentity
    def set_dlpath(self, path):
        self.fhandler.set_dlpath(path)
        self.y2mate.set_dlpath(self.fhandler.dl_path)

class YouTubeMusicPlayer(BaseQWorker):

    @funcIdentity
    def __init__(self):
        super().__init__()
        self.playlist = YouTubePlayList()
        self.downloaderMDB = WorkerThreadManager()
    @funcIdentity
    def run(self):
        self.started.emit()
    @funcIdentity
    def close(self):
        self.finished.emit()

    @funcIdentity
    def view_playlist(self):
        self.playlist.view()
    @funcIdentity
    def set_dlpath(self, path=None):
        self._dlpath = path

    @funcIdentity
    def download_playlist(self, keyword):
        # 플레이리스트 1개의 모든 음악을 다운로드한다

        self.playlist.fetch(keyword)

        targets = self.playlist.DownloadTarget
        logger.info(f'{self} | Target VideoIds({len(targets)})-->\n{targets}')
        for videoId in targets:
            downloader = YouTubeMusicDownLoader(self.playlist, videoId)
            downloader.set_dlpath(self._dlpath)
            worker = WorkerGenerator(downloader)
            self.downloaderMDB.add(videoId, worker)
            worker.start()
            # break

    """"개발중""""
    @funcIdentity
    def download_one(self, url):
        self.y2mate.set_dlpath(p)
        # url: 유투브 비디오 URL
        self.y2mate.get_mp3(url)
        logger.info(f'{self} | Done.')
