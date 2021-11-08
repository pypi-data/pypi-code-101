from __future__ import annotations
from abc import abstractmethod, ABCMeta
from collections.abc import Callable

from enum import IntEnum
import os
import sys
import weakref
from queue import Queue
from ctypes import windll, Structure, wintypes, pointer
import platform

import pygame
import pygame.freetype
from pygame.color import Color
from pygame.rect import Rect

import pgzero.game
from pgzero.constants import mouse
from pgzero.constants import keys
from pgzero.constants import keymods
from pgzero.keyboard import keyboard

from pzwin.Constants import *
from pzwin.WinEvent import WinEvent

from pynput.mouse import Controller


class WinRect(Structure):
    _fields_ = [
        ("left", wintypes.LONG),
        ("top", wintypes.LONG),
        ("right", wintypes.LONG),
        ("bottom", wintypes.LONG),
    ]


class WinBase(metaclass=ABCMeta):
    g_pzwinDeskTop: WinBase | None = None
    g_isMouseDragStart: bool = False
    g_desktopPos: tuple[int, int] = (0, 0)
    g_desktopSize: tuple[int, int] = (0, 0)
    g_mouseCtrl: Controller = Controller()
    SWP_NOSIZE: int = 0x0001
    SWP_NOMOVE: int = 0x0002
    SWP_NOOWNERZORDER: int = 0x0200

    # 防抖动的计数参数，该值适合于60帧速率的pgzero事件循环函数update()，如果不是60帧的速率，可以适当调整该值
    ANTI_KEY_SHARKING_COUNT: int = 10
    keyCounter: int = 0
    lastKey: keys = keys.POWER  # 这里使用POWER键作为未按键的判断
    lastMod: keymods = pygame.KMOD_NONE
    lastChar: str = ''  # 记录可显示字符

    eventQueue: Queue = Queue()

    _pos: tuple[int, int]  # (left, top)
    _size: tuple[int, int]  # (width, height)
    _absolutePosition: tuple[int, int]  # (left, top)
    _isDesktop: bool = False
    _rect: Rect
    _absoluteRect: Rect
    _formBGColor: Color
    _surface: pygame.Surface | None
    _fontEntity: dict[str, pygame.freetype.Font] = {}
    _zBuffer: list[WinBase] = []
    _parent: WinBase | None
    _mousePointer: pygame.Surface | None
    _mousePos: tuple[int, int]
    _mousePointerAnchor: tuple[int, int]
    _isShow: bool
    _isFocusOn: bool
    _frameComponentSet: set[WinBase] = set()

    def __init__(self,  parent: WinBase | None, rect: Rect):

        self._size = (rect.width, rect.height)
        self._rect = rect
        self._formBGColor = DefaultColor.FORM_BACKGROUND.value
        self._surface: pygame.Surface | None = pygame.Surface(
            self._size)  # None
        self._clientRect: Rect = Rect(0, 0, rect.width, rect.height)
        self._clientSurface: pygame.Surface = pygame.Surface(
            (rect.width, rect.height))
        self._fontEntity: dict[str, pygame.freetype.Font] = {}
        self._zBuffer: list[WinBase] = []

        self._borderColor: Color = DefaultColor.BORDER.value
        self._borderThickness: int = 1
        self._textColor: Color = DefaultColor.TEXT.value
        self._fontName: str = DefaultFont.NAME
        self._fontSize: int = DefaultFont.SIZE
        self._caption: str = ''
        self._id: str = ''
        self._borderVisible: bool = False
        self._isHorizontalCenter: bool = False
        self._isVerticalCenter: bool = True
        self._isFocusOn = False

        if parent != None:  # 首个窗口（桌面）为None
            self._parent: WinBase | None = weakref.proxy(parent)
            self._parent.lastZBuffer = self
            parentAbsolutionPos: tuple[int,
                                       int] = self.getParentAbsolutePosition()
            self._absolutePosition: tuple[int, int] = (
                parentAbsolutionPos[0] + rect.left, parentAbsolutionPos[1] + rect.top + DefaultParams.FRAME_TITLE_HEIGHT)
            self._absoluteRect: Rect = self.convertToAbsoluteRect()
            self._isDesktop: bool = False
            self._pos = (rect.left, rect.top)
        else:
            self._parent: WinBase | None = None
            WinBase.g_pzwinDeskTop = self  # 此处导致桌面顶层窗体的引用计数+1，但对子窗体应该没有影响
            WinBase.g_desktopPos = (rect.left, rect.top)
            WinBase.g_desktopSize = (rect.width, rect.height)
            WinBase.moveDesktopAbs(rect.left, rect.top)
            self._isDesktop: bool = True
            self._pos = (0, 0)
            self._rect = Rect(0, 0, self._rect.width, self._rect.height)
            self._absolutePosition: tuple[int, int] = (0, 0)
            self._absoluteRect: Rect = Rect(
                0, 0, self._rect.width, self._rect.height)
            #self._absoluteRect:Rect = rect
            self._isShow = True

            self.keyCounter = 0
            self.lastKey = keys.POWER  # 这里使用POWER键作为未按键的判断

        self._onKeyPress: Callable[[WinBase, keys], bool] | None = None
        self._onCharPress: Callable[[WinBase, str], bool] | None = None
        self._onMouseMove: Callable[[
            WinBase, tuple[int, int]], bool] | None = None
        self._onMouseDown: Callable[[
            WinBase, tuple[int, int], mouse], bool] | None = None
        self._onMouseUp: Callable[[
            WinBase, tuple[int, int], mouse], bool] | None = None
        self._onMouseDrag: Callable[[
            WinBase, tuple[int, int], set[mouse]], bool] | None = None
        self._onMouseDrop: Callable[[WinBase], bool] | None = None
        self._onShow: Callable[[WinBase], bool] | None = None
        self._onHide: Callable[[WinBase], bool] | None = None

        self.loadMousePointer('mousepointer2.png')
        self._mousePointerAnchor: tuple[int, int] = (0, 0)  # 鼠标缺省焦点在左上角

        # 设置鼠标居中
        self._mousePos = (self._rect.width//2, self._rect.height//2)

    # 每个自定义回调函数的派生类都要实现该方法，并确保调用父类的该方法，以减少内存引用数量
    def clearCallBack(self):
        self._onKeyPress: Callable[[WinBase, keys], bool] | None = None
        self._onCharPress: Callable[[WinBase, str], bool] | None = None
        self._onMouseMove: Callable[[
            WinBase, tuple[int, int]], bool] | None = None
        self._onMouseDown: Callable[[
            WinBase, tuple[int, int], mouse], bool] | None = None
        self._onMouseUp: Callable[[
            WinBase, tuple[int, int], mouse], bool] | None = None
        self._onMouseDrag: Callable[[
            WinBase, tuple[int, int], set[mouse]], bool] | None = None
        self._onMouseDrop: Callable[[WinBase], bool] | None = None
        self._onShow: Callable[[WinBase], bool] | None = None
        self._onHide: Callable[[WinBase], bool] | None = None

    def adjustAbsolutePosition(self):
        if self._isDesktop == False:
            parentAbsolutionPos: tuple[int,
                                       int] = self.getParentAbsolutePosition()
            if self._parent.isFrameComponent(self):
                self._absolutePosition: tuple[int, int] = (
                    parentAbsolutionPos[0] + self._rect.left, parentAbsolutionPos[1] + self._rect.top)
            else:
                self._absolutePosition: tuple[int, int] = (
                    parentAbsolutionPos[0] + self._rect.left, parentAbsolutionPos[1] + self._rect.top + DefaultParams.FRAME_TITLE_HEIGHT)
            self._absoluteRect: Rect = self.convertToAbsoluteRect()
        else:
            self._absolutePosition: tuple[int, int] = (0, 0)
            self._absoluteRect: Rect = Rect(
                0, 0, self._rect.width, self._rect.height)
        for childWin in self._zBuffer:
            childWin.adjustAbsolutePosition()

    # 派生出来的组件、窗体，在其实例被del之前，应调用destory来释放内存引用计数
    def destroy(self):
        print('1------X', self._caption, self.__class__,
              sys.getrefcount(self))  # 保留打印，以确保能清除干净内存
        for childWin in reversed(self._zBuffer):
            childWin.clearCallBack()
            childWin.destroy()
            del childWin
        self.clearCallBack()
        self._frameComponentSet.clear()
        if self._isDesktop != True:
            try:
                self._parent._zBuffer.remove(self)
                print('2------X', self.__class__,
                      sys.getrefcount(self))  # 保留打印，以确保能清除干净内存
            except ReferenceError:
                print('none')
        print('3------X', self.__class__,
              sys.getrefcount(self))  # 保留打印，以确保能清除干净内存

    def __del__(self):
        print('1------>', self._caption, self.__class__,
              sys.getrefcount(self))  # 保留打印，以确保能清除干净内存

    # 定义zBuffer的只写属性
    def _zBufferAppend(self, child: WinBase):
        self._zBuffer.append(child)
    lastZBuffer = property(None, _zBufferAppend)

    @property
    def caption(self):
        return self._caption

    @caption.setter
    def caption(self, captionString: str):
        self._caption = captionString

    def show(self) -> WinBase:
        self._isShow = True
        if self._onShow != None:
            self._isShow = self._onShow()
        return self

    @property
    def onShow(self) -> Callable[[WinBase], bool] | None:
        return self._onShow

    @onShow.setter
    def onShow(self, fn: Callable[[WinBase], bool] | None):
        self._onShow = fn

    def hide(self) -> WinBase:
        self._isShow = False
        if self._onHide != None:
            self._isShow = self._onHide()
        return self

    @property
    def onHide(self) -> Callable[[WinBase], bool] | None:
        return self._onHide

    @onHide.setter
    def onHide(self, fn: Callable[[WinBase], bool] | None):
        self._onHide = fn

    # 对于窗体组件（窗体图标、标题栏、关闭按钮）返回窗体整个Surface，
    # 否则返回窗体的clientSurface，即非窗体组件只能被绘制在clientSurface中
    def getSurface(self, whoQuery: WinBase) -> pygame.Surface:
        if whoQuery in self._frameComponentSet:
            return self._surface
        else:
            return self._clientSurface
    # 获取父窗体的clientSurface

    def getParentSurface(self) -> pygame.Surface:
        if self._isDesktop == False:
            return self._parent.getSurface(self)
        else:
            return pgzero.game.screen

    def isFrameComponent(self, componentInst: WinBase):
        return componentInst in self._frameComponentSet

    def getAbsolutePosition(self) -> tuple[int, int]:
        return self._absolutePosition

    def getParentAbsolutePosition(self) -> tuple[int, int]:
        if self._isDesktop == False:
            return self._parent.getAbsolutePosition()
        else:
            return (0, 0)

    def convertToAbsoluteRect(self) -> Rect:
        absolutePos = self.getAbsolutePosition()
        # if self._parent.isFrameComponent(self):
        absoluteRect: Rect = Rect(
            absolutePos[0], absolutePos[1], self._rect.width, self._rect.height)
        # else:
        #    absoluteRect:Rect = Rect(absolutePos[0], absolutePos[1] + DefaultParams.FRAME_TITLE_HEIGHT, self._rect.width, self._rect.height)
        return absoluteRect

    def setSelfInFrameRect(self):
        self._absolutePosition = (
            self._absolutePosition[0], self._absolutePosition[1] - DefaultParams.FRAME_TITLE_HEIGHT)
        self._absoluteRect = self.convertToAbsoluteRect()

    def addToFrameComponentSet(self, componentInst: WinBase):
        if componentInst not in self._frameComponentSet:
            self._frameComponentSet.add(componentInst)
            componentInst.setSelfInFrameRect()

    def draw(self):
        if self._isShow == False:
            return
        # 第一步应该先擦除屏幕，一般来说只需要最底层的deskTop窗体实例调用该函数即可
        self.wipeOff()

        # 接着依次绘制窗体和窗体上的组件、边框等，先绘制自己的，再调用子窗体的方法来绘制处于上层的子窗体
        self.drawForm()

        # 再根据输入焦点画键盘输入的光标
        self.drawCursor()

        # 所有都画完后，将surface贴到父窗体的surface上，如果是deskTop窗体，它的父窗体surface就是pgzero.game.screen
        if self._isDesktop:
            parentSurface = self.getParentSurface()
            parentSurface.blit(self._surface, self._pos)
        # 最后画处于最上层的鼠标
        self.drawMousePointer()

    def wipeOff(self):
        self._surface.fill(self._formBGColor)
        self._clientSurface.fill(self._formBGColor)

    def drawForm(self):
        self._surface.fill(self._formBGColor)

    def drawText(self, s: str, pos, color, fontName: str, fontSize: int):
        if fontName not in self._fontEntity:
            currentPath = os.path.split(os.path.realpath(__file__))[0]
            self._fontEntity[fontName] = pygame.freetype.Font(
                os.path.join(currentPath, 'fonts', fontName), 20)
        fontRect: Rect = self._fontEntity[fontName].get_rect(s, size=fontSize)
        (targetX, targetY) = pos
        if self._isHorizontalCenter:
            targetX = self._rect.width // 2 - fontRect.width // 2
        if self._isVerticalCenter:
            targetY = self._rect.height // 2 - fontRect.height // 2
        self._fontEntity[fontName].render_to(
            self._surface, (targetX, targetY), s, color, size=fontSize)

    def drawBorder(self):
        if self._borderVisible:
            pygame.draw.rect(self._surface, self._borderColor, Rect(
                0, 0, self._rect.width, self._rect.height), self._borderThickness)

    @abstractmethod
    def drawMousePointer(self):
        # To do: 由于鼠标pos记录的是在桌面窗体内的位置，所以要计算鼠标在当前窗体中的位置。理论上只应在桌面窗体的重绘时来绘制鼠标，否则会有截断的情况
        # To do: 还要计算anchorPoint
        #self._mousePointer.pos = self._mousePos
        # mouseBlitPos:Rect =
        if self._isDesktop == False:
            return
        parentSurface = self.getParentSurface()
        parentSurface.blit(self._mousePointer, self._mousePos)

    @abstractmethod
    def drawCursor(self):
        pass

    # 返回True说明事件已被处理，不应该再向父窗体传递
    def eventLoop(self, recvWin: WinBase | None, winEvent: WinEvent) -> bool:
        if recvWin != None:
            if self == recvWin:
                return self.eventProcessor(winEvent)
            else:
                for chrldWin in reversed(self._zBuffer):
                    if chrldWin.eventLoop(recvWin, winEvent):
                        return True
            return False
        else:
            for childWin in reversed(self._zBuffer):
                if childWin.eventLoop(recvWin, winEvent):
                    return True
            return self.eventProcessor(winEvent)

    def eventProcessor(self, winEvent: WinEvent) -> bool:
        match winEvent.type:
            case WinEventType.WET_KEY:
                match winEvent.subType:
                    case KeySubEvent.KEY_PRESS:
                        if self._onKeyPress != None:
                            return self._onKeyPress(winEvent.params['key'])
                    case KeySubEvent.KEY_CHAR:
                        if self._onCharPress != None:
                            return self._onCharPress(winEvent.params['unicode'])
            case WinEventType.WET_MOUSE:
                match winEvent.subType:
                    case MouseSubEvent.MOUSE_MOVE:
                        if self._onMouseMove != None:
                            return self._onMouseMove(winEvent.params['pos'])
                    case MouseSubEvent.MOUSE_DOWN:
                        if self._onMouseDown != None:
                            return self._onMouseDown(winEvent.params['pos'], winEvent.params['button'])
                    case MouseSubEvent.MOUSE_UP:
                        if self._onMouseUp != None:
                            return self._onMouseUp(winEvent.params['pos'], winEvent.params['button'])
                    case MouseSubEvent.MOUSE_DRAG:
                        if self._onMouseDrag != None:
                            return self._onMouseDrag(winEvent.params['delta'], winEvent.params['buttons'])
                    case MouseSubEvent.MOUSE_DROP:
                        if self._onMouseDrop != None:
                            return self._onMouseDrop()
        return False

    def on_mouse_move(self, pos, rel, buttons: mouse):
        winEvent = WinEvent(WinEventType.WET_MOUSE, MouseSubEvent.MOUSE_MOVE, {
                            'pos': pos, 'delta': rel, 'buttons': buttons})
        WinBase.pumpEvent(None, winEvent)

    def on_mouse_down(self, pos, button):
        winEvent = WinEvent(WinEventType.WET_MOUSE, MouseSubEvent.MOUSE_DOWN, {
                            'pos': pos, 'button': button})
        WinBase.pumpEvent(None, winEvent)

    def on_mouse_up(self, pos, button):
        winEvent = WinEvent(WinEventType.WET_MOUSE, MouseSubEvent.MOUSE_UP, {
                            'pos': pos, 'button': button})
        WinBase.pumpEvent(None, winEvent)

    @classmethod
    def on_key_press(cls, key: keys, mod: keymods, unicode: str):
        winEvent = WinEvent(WinEventType.WET_KEY, KeySubEvent.KEY_PRESS, {
                            'key': key, 'mod': mod, 'unicode': unicode})
        WinBase.pumpEvent(None, winEvent)
        if unicode != '' and unicode.isprintable():
            winEvent = WinEvent(WinEventType.WET_KEY,
                                KeySubEvent.KEY_CHAR, {'unicode': unicode})
            WinBase.pumpEvent(None, winEvent)

    # keyDown()需要在pgzero的on_key_down()事件触发函数中被调用
    @classmethod
    def keyDown(cls, key: keys, mod: keymods, unicode: str):
        cls.lastKey = key
        cls.lastChar = unicode
        cls.lastMod = mod
        cls.on_key_press(cls.lastKey, mod, cls.lastChar)

    # keyUp()需要在pgzero的on_key_up()事件触发函数中被调用
    @classmethod
    def keyUp(cls, key: keys, mod: keymods):
        cls.lastKey = keys.POWER
        cls.lastChar = ''
        cls.lastMod = mod
        cls.keyCounter = 0

    # keyPressCheck()需要在pgzero的事件循环函数update()中被调用
    @classmethod
    def keyPressCheck(cls):
        if keyboard[cls.lastKey]:
            cls.keyCounter += 1
        if cls.keyCounter > cls.ANTI_KEY_SHARKING_COUNT:
            cls.on_key_press(cls.lastKey, cls.lastMod, cls.lastChar)

    @abstractmethod
    def onMouseMove(self, pos) -> bool:
        pass

    @abstractmethod
    def onMouseDown(self, pos, button: mouse) -> bool:
        pass

    @abstractmethod
    def onMouseUp(self, pos, button: mouse) -> bool:
        pass

    @abstractmethod
    def onKeyPress(self, key: keys) -> bool:
        pass

    @staticmethod
    def pumpEvent(recvWin: WinBase | None, winEvent: WinEvent):
        if not WinBase.eventQueue.full():
            WinBase.eventQueue.put({'winObj': recvWin, 'event': winEvent})

    @staticmethod
    def pumpMouseMoveEvent(pos: tuple[int, int]):
        winEvent = WinEvent(WinEventType.WET_MOUSE,
                            MouseSubEvent.MOUSE_MOVE, {'pos': pos})
        WinBase.pumpEvent(None, winEvent)

    @staticmethod
    def pumpMouseDragStartEvent(rel: tuple[int, int], buttons: set[mouse]):
        WinBase.g_isMouseDragStart = True
        winEvent = WinEvent(WinEventType.WET_MOUSE, MouseSubEvent.MOUSE_DRAG, {
                            'delta': rel, 'buttons': buttons})
        WinBase.pumpEvent(None, winEvent)

    @staticmethod
    def pumpMouseDownEvent(pos: tuple[int, int], button: mouse):
        winEvent = WinEvent(WinEventType.WET_MOUSE, MouseSubEvent.MOUSE_DOWN, {
                            'pos': pos, 'button': button})
        WinBase.pumpEvent(None, winEvent)

    @staticmethod
    def pumpMouseUpEvent(pos: tuple[int, int], button: mouse):
        if WinBase.g_isMouseDragStart:
            WinBase.g_isMouseDragStart = False
            winEvent = WinEvent(WinEventType.WET_MOUSE,
                                MouseSubEvent.MOUSE_DROP, {})
        else:
            winEvent = WinEvent(WinEventType.WET_MOUSE, MouseSubEvent.MOUSE_UP, {
                                'pos': pos, 'button': button})
        WinBase.pumpEvent(None, winEvent)

    @staticmethod
    def moveDesktopAbs(x: int, y: int, hwnd=None):
        systemPlatform: str = platform.system()
        if systemPlatform != 'Windows':
            return
        if hwnd is None:
            hwnd = pygame.display.get_wm_info()["window"]
        # | WinBase.SWP_NOOWNERZORDER | 0x0008 | 0x2000)
        windll.user32.SetWindowPos(hwnd, 0, x, y, 0, 0, WinBase.SWP_NOSIZE)
        #windll.user32.MoveWindow(hwnd, x, y, 800, 600, True)

    @staticmethod
    def getDesktopRect(hwnd=None) -> Rect:
        systemPlatform: str = platform.system()
        if systemPlatform != 'Windows':
            return Rect(0, 0, 0, 0)
        if hwnd is None:
            hwnd = pygame.display.get_wm_info()["window"]
        r = WinRect(0, 0, 0, 0)
        windll.user32.GetWindowRect(hwnd, pointer(r))
        return pygame.Rect(r.left, r.top, r.right - r.left, r.bottom - r.top)

    @staticmethod
    def moveDesktopRel(dx: int, dy: int, hwnd=None):
        systemPlatform: str = platform.system()
        if systemPlatform != 'Windows':
            return
        if hwnd is None:
            hwnd = pygame.display.get_wm_info()["window"]
        r = WinBase.getDesktopRect(hwnd)
        # | WinBase.SWP_NOOWNERZORDER)
        windll.user32.SetWindowPos(
            hwnd, 0, r.x + dx, r.y + dy, 0, 0, WinBase.SWP_NOSIZE)

    @classmethod
    def dispatch(cls):
        cls.keyPressCheck()

        while not cls.eventQueue.empty():
            queueElement = cls.eventQueue.get()
            if WinBase.g_pzwinDeskTop != None:
                WinBase.g_pzwinDeskTop.eventLoop(
                    queueElement['winObj'], queueElement['event'])

    @abstractmethod
    def update(self):
        pass

    # builder mode start here...
    def setBgColor(self, color: Color) -> WinBase:
        self._formBGColor = color
        return self

    def setBorderColor(self, color: Color) -> WinBase:
        self._borderColor = color
        return self

    def setBorderThickness(self, thickness: int) -> WinBase:
        if thickness >= 0:
            self._borderThickness = thickness
        return self

    def setTextColor(self, color: Color) -> WinBase:
        self._textColor = color
        return self

    def setCaption(self, text: str) -> WinBase:
        self.caption = text
        return self

    def setMouseMoveCallBack(self, fn: Callable[[WinBase, tuple], bool] | None) -> WinBase:
        self._onMouseMove = fn
        return self

    def setMouseDownCallBack(self, fn: Callable[[WinBase, tuple[int, int], mouse], bool] | None) -> WinBase:
        self._onMouseDown = fn
        return self

    def setMouseUpCallBack(self, fn: Callable[[WinBase, tuple[int, int], mouse], bool] | None) -> WinBase:
        self._onMouseUp = fn
        return self

    def setMouseDragCallBack(self, fn: Callable[[WinBase, tuple[int, int], set[mouse]], bool] | None) -> WinBase:
        self._onMouseDrag = fn
        return self

    def setMouseDropCallBack(self, fn: Callable[[WinBase], bool] | None) -> WinBase:
        self._onMouseDrop = fn
        return self

    def setKeyPressCallBack(self, fn: Callable[[WinBase, keys], bool] | None) -> WinBase:
        self._onKeyPress = fn
        return self

    def setCharPressCallBack(self, fn: Callable[[WinBase, str], bool] | None) -> WinBase:
        self._onCharPress = fn
        return self

    def setShowCallBack(self, fn: Callable[[WinBase], bool] | None) -> WinBase:
        self._onShow = fn
        return self

    def setHideCallBack(self, fn: Callable[[WinBase], bool] | None) -> WinBase:
        self._onHide = fn
        return self

    def setBorderVisible(self, isVisible: bool) -> WinBase:
        self._borderVisible = isVisible
        return self

    def setTextFont(self, fontName: str) -> WinBase:
        self._fontName = fontName
        return self

    def setTextSize(self, fontSize: int) -> WinBase:
        self._fontSize = fontSize
        return self

    def setTextHorizontalCenter(self, isHorizontalCenter: bool) -> WinBase:
        self._isHorizontalCenter = isHorizontalCenter
        return self

    def setTextVerticalCenter(self, isVerticalCenter: bool) -> WinBase:
        self._isVerticalCenter = isVerticalCenter
        return self

    def loadMousePointer(self, fileName: str) -> WinBase:
        currentPath = os.path.split(os.path.realpath(__file__))[0]
        currentPath = os.path.join(currentPath, 'images', fileName)
        if os.path.splitext(fileName)[1].lower() == '.png':
            self._mousePointer = pygame.image.load(currentPath).convert_alpha()
        else:
            self._mousePointer = pygame.image.load(currentPath).convert()
        return self

    def setMousePointerAnchor(self, anchorPoint: tuple[int, int] = (0, 0)) -> WinBase:
        self._mousePointerAnchor: tuple[int, int] = anchorPoint
        return self

    def switchDesktopFullscreenState(self) -> WinBase:
        pygame.display.toggle_fullscreen()
        return self

    def setSystemMouseVisibility(self, isVisible: bool) -> WinBase:
        pygame.mouse.set_visible(isVisible)
        return self
