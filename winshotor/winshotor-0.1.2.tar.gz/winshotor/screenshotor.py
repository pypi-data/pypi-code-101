#对后台窗口截图
import win32gui, win32ui, win32con
from ctypes import windll
from ctypes.wintypes import *
import numpy as np

class WindowsNotFindError(Exception):
    def __init__(self, hwnd):
        super(WindowsNotFindError, self).__init__("\n\n[Error]: Can not find window with {hwnd: %s}"%str(hwnd))
#
# def IsEmptyString(string):
#     for s in string:
#         if s not in ['\t', '\n', ' ']:
#             return False
#     return True

class WinInfo:  # ReadOnly
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.title = self.GetTitle(hwnd)
        self.name = self.title
        self.left, self.top, self.width, self.height = self.get_window_rect(hwnd)
        self.right, self.bottom = self.left + self.width, self.top + self.height
        self.cx, self.cy = .5 * (self.left + self.right), .5 * (self.top + self.bottom)

        self.l, self.t, self.r, self.b = self.left, self.top, self.right, self.bottom
        self.w, self.h = self.width, self.height

    @staticmethod
    def GetTitle(hwnd):
        return win32gui.GetWindowText(hwnd)

    @property
    def visiable(self):
        return win32gui.IsWindowVisible(self.hwnd)

    @property
    def enabled(self):
        return win32gui.IsWindowEnabled(self.hwnd)


    @staticmethod
    def get_window_rect(hwnd):
        try:
            f = ctypes.windll.dwmapi.DwmGetWindowAttribute
        except WindowsError:
            f = None
        if f:
            rect = ctypes.wintypes.RECT()
            DWMWA_EXTENDED_FRAME_BOUNDS = 9
            f(ctypes.wintypes.HWND(hwnd),
              ctypes.wintypes.DWORD(DWMWA_EXTENDED_FRAME_BOUNDS),
              ctypes.byref(rect),
              ctypes.sizeof(rect)
              )
            return rect.left, rect.top, rect.right - rect.left, rect.bottom - rect.top
        else:
            raise WindowsNotFindError(hwnd)

    def __eq__(self, other):
        return bool(other) and isinstance(other, WinInfo) and self.hwnd == other.hwnd and self.left == other.left and self.top == other.top and self.right == other.right and self.bottom == other.bottom and self.title == other.title

    def __str__(self):
        return "hwnd<{}> title<{}> rect<l:{} t:{} w:{} h:{}>".format(self.hwnd, self.title, self.left, self.top, self.width, self.right)

class WinInfor:  # 窗口信息获取者
    def __init__(self):
        self.hwnds = None

    def Update(self, include_unvisiable=False, include_disabled=False, include_zero_rect=False, include_empty_title=False):
        self.hwnds = self.Enum(include_unvisiable, include_disabled, include_zero_rect, include_empty_title)

    def Enum(self, include_unvisiable=False, include_disabled=False, include_zero_rect=False, include_empty_title=False):
        hwnds = []
        def get_all_hwnd(hwnd, mouse):
            if win32gui.IsWindow(hwnd) and (include_disabled or win32gui.IsWindowEnabled(hwnd)) and (include_unvisiable or win32gui.IsWindowVisible(hwnd)) and (include_empty_title or len(WinInfo.GetTitle(hwnd))):
                if not include_zero_rect:
                    rect = WinInfo.get_window_rect(hwnd)
                    if rect[2] * rect[3] == 0:
                        return
                hwnds.append(hwnd)

        win32gui.EnumWindows(get_all_hwnd, 0)
        return hwnds

    def GetWinInfos(self):
        if self.hwnds is None: raise Exception("\n\n[Error]:Before you finding, you must call .UpdateRecord() once more.")
        if not self.hwnds: return
        infos = []
        for hwnd in self.hwnds:
            infos += [WinInfo(hwnd)]
        return infos


class WinShotor:
    def __init__(self, hwnd):
        self.hwnd = hwnd
        self.hwndDC = win32gui.GetWindowDC(hwnd)
        self.mfcDC = win32ui.CreateDCFromHandle(self.hwndDC)
        self.dc = self.mfcDC.CreateCompatibleDC()
        self.bitmap = win32ui.CreateBitmap()

        self.win_info = None

    @staticmethod
    def __is_not_minium(info):
        return bool(info) and info.l >= 0 and info.r >= 0 and info.t >= 0 and info.b >= 0 and info.w >= 0 and info.h >= 0

    def SnapShot(self):
        wininfo = WinInfo(self.hwnd)
        if not self.__is_not_minium(wininfo):
            print("[MaybeFailed]: Please do not minimize the window. This screenshot maybe failed.")

        if self.win_info != wininfo:  # 触发eq
            self.win_info = wininfo
            self.bitmap.CreateCompatibleBitmap(self.mfcDC, wininfo.width, wininfo.height)
            self.dc.SelectObject(self.bitmap)
        self.dc.BitBlt((0, 0), (self.win_info.width, self.win_info.height), self.mfcDC, (0, 0), win32con.SRCCOPY)

        return self.BitmapToNp(self.bitmap, self.win_info.width, self.win_info.height)


    @staticmethod
    def BitmapToNp(bitmap, w, h):
        # 获得数据流
        bits = bitmap.GetBitmapBits(True)
        # 转换为numpy对象
        img = np.frombuffer(bits, dtype='uint8')
        img.shape = (h, w, 4)  # RGB+Alpha 4个颜色通道

        return img


if __name__ == '__main__':
    import time
    import cv2
    wb = WinInfor()
    wb.Update()
    infos = wb.GetWinInfos()

    for i in range(len(infos)):
        print(i, infos[i])
    _id = int(input("输入Id: "))
    ws = WinShotor(infos[_id].hwnd)

    a = time.time()
    for i in range(100):
        img = ws.SnapShot()
    print("100张截图耗时: ", time.time() - a)

    cv2.imshow('pic', img)
    cv2.waitKey(0)
    #imageio.imsave("screenshot.png", img)
