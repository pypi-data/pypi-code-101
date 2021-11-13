# -*- coding: utf-8 -*-
from time import sleep

import requests
import pandas as pd
from PyQt5.QtCore import *

from idebug import *
from ipylib.ipath import *


__all__ = [
    'BaseQWorker',
    'WorkerGenerator',
    'WorkerThreadManager',
    'Downloader',
]


class BaseQWorker(QObject):
    # 용어정의
    # - 객체 생성: __init__() --> None
    # - 객체 종료/파괴: 파이썬이 알아서 해준다
    # - 작업시작: start/run() --> started.emit [작업(시작시퀀스)완료]
    # - 작업종료: close/stop/quit/exit() --> closed/stopped/finished
    # - 작업중지: pause() --> paused.emit
    # 서브작업완료의 경우 보다 상세한 시그널명을 사용하라

    # PyQt5의 정해진 규칙
    # thread.start() --> thread.started.emit()
    # thread.quit() --> thread.finished.emit()

    # worker.__init__() --> None
    # worker.start() --> worker.started.emit()
    # worker.started --> worker.run()
    # worker.run() --> None
    # worker.close() --> object.finished.emit()

    finished = pyqtSignal()
    closed = pyqtSignal() # finished 로 통일하라
    stopped = pyqtSignal() # finished 로 통일하라
    started = pyqtSignal() # 가끔 필요한 경우도 있다
    completed = pyqtSignal() # started 로 통일하라
    """이하 기본함수들은 '복붙'해서 사용해야 로깅이 정확하게 된다"""

    # @funcIdentity
    def __init__(self):
        super().__init__()
    @funcIdentity
    def run(self):
        self.started.emit()
    @funcIdentity
    def close(self):
        self.finished.emit()
    """삭제예정"""
    @funcIdentity
    def done(self):
        self.completed.emit()

class WorkerGenerator(BaseQWorker):
    # 2021-11-09 14:33:10,743 | ERROR | [85352/MainProcess][89280/MainThread] |
    # worker.stop[48] | <kiwoomtrader.Lib.worker.WorkerGenerator object at 0x09D13220> |
    # wrapped C/C++ object of type QThread has been deleted
    # 2021-11-09 14:33:10,743 | ERROR | [85352/MainProcess][89280/MainThread] |
    # trader.manage_target[342] | <kiwoomtrader.trader.TraderManager object at 0x09CF8B68> |
    # wrapped C/C++ object of type QThread has been deleted

    # 'WorkerThreadManager'에게 자신을 지워달라고 알려쥼
    stopped = pyqtSignal(str)

    # @funcIdentity
    def __init__(self, qobject, func='run', *args, **kwargs):
        super().__init__()
        try:
            self.func = func
            self._args = args
            self._kwargs = kwargs

            self.worker = qobject(*self._args, **self._kwargs) if callable(qobject) else qobject
            self.name = self.worker.__class__.__name__

            self.thread = QThread()
            self.worker.moveToThread(self.thread)
            self.thread.started.connect(getattr(self.worker, self.func))
            self.worker.finished.connect(self.thread.quit)
            self.thread.finished.connect(self.stop)
            # self.worker.finished.connect(self.worker.deleteLater)
            # self.thread.finished.connect(self.thread.deleteLater)
            self.finished.connect(self.thread.deleteLater)
            self.finished.connect(self.worker.deleteLater)
        except Exception as e:
            logger.error(f'{self} | {e}')
            raise
    @funcIdentity
    def start(self):
        self.thread.start()
        logger.debug(f'{self} | {self.name}.thread.isRunning--> {self.thread.isRunning()}')
        self.started.emit()
    @funcIdentity
    def stop(self):
        try:
            if self.thread.isRunning(): self.thread.quit()
            while self.thread.isRunning(): sleep(0.1)
            logger.debug(f'{self} | {self.name}.thread.isRunning--> {self.thread.isRunning()}')
            self.finished.emit()
            if hasattr(self, 'wid'): self.stopped.emit(self.wid)
        except Exception as e:
            logger.error(f'{self} | {e}')
            raise
    @property
    def is_runinng(self):
        logger.debug(f'{self} | {self.name}.thread.isRunning--> {self.thread.isRunning()}')
        return self.thread.isRunning()

class WorkerThreadManager(BaseQWorker):
    # 개별 스레드로 동작하는 워커스레드를 관리하는 객체
    # self.wid = Worker(QThread)
    # WorkerGenerator 특성과 연계해서 잘 생각해야한다.

    def __init__(self):
        super().__init__()
    @funcIdentity
    def add(self, wid, worker):
        wid = str(wid)
        worker.wid = wid
        worker.stopped.connect(self.remove)
        setattr(self, wid, worker)
    def get(self, wid):
        wid = str(wid)
        if hasattr(self, wid): return getattr(self, wid)
        else: logger.warning(f"{self} | wid({wid})는 등록되어있지 않다")
    @funcIdentity
    @pyqtSlot(str)
    def remove(self, wid):
        wid = str(wid)
        if hasattr(self, wid): delattr(self, wid)
        if len(self.wids) == 0: self.ManagementState()
    @funcIdentity
    def start(self, wid):
        self.get(wid).start()
    @funcIdentity
    def stop(self, wid):
        self.get(wid).stop()
        return self

    @property
    def dic(self):
        return self.__dict__.copy()
    @property
    def wids(self):
        return list(self.__dict__)

    @funcIdentity
    def ManagementState(self):
        data = []
        for wid, worker in self.__dict__.items():
            data.append({'wid':wid, 'state':worker.is_runinng, 'worker':worker})
        df = pd.DataFrame(data)
        logger.info(f'{self} | 워커스레드 등록현황-->\n{df}')

class Downloader(BaseQWorker):

    @funcIdentity
    def __init__(self, path=None):
        super().__init__()
        # 시스템 기본 다운로드 경로를 강제설정한다
        self.path = 'C:/Users/innovata/Downloads' if path is None else path

    def get(self, url, filename, **kw):
        r = requests.get(url, **kw)
        # dbg.dict(r)
        self.fpath = clean_path(f"{self.path}/{filename}")
        with open(self.fpath, 'wb') as fd:
            for chunk in r.iter_content(chunk_size=128):
                fd.write(chunk)
        fd.close()
        self.finished.emit()
