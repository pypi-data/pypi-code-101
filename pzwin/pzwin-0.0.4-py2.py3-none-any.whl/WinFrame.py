from __future__ import annotations
from enum import IntEnum
from collections.abc import Callable

import os
import sys
import pygame
import pgzrun
import pgzero.game
from pygame.rect import Rect

from pgzero.actor import Actor
from pgzero.constants import mouse
from pgzero.constants import keys

from pzwin.Constants import *
from pzwin.WinEvent import *
from pzwin.WinBase import WinBase
from pzwin.Button import Button
from pzwin.Label import Label
from pzwin.Edit import Edit
from pzwin.Panel import Panel

#import pyautogui


class WinFrame(WinBase):
    def __init__(self, parent: WinBase | None, rect: Rect):
        super().__init__(parent, rect)
        self._onMouseMove = self.onMouseMove
        self._onMouseDown = self.onMouseDown
        self._onMouseUp = self.onMouseUp
        self._onMouseDrag = self.onMouseDrag
        self._onKeyPress = self.onKeyPress
        self._onClose: Callable[[WinBase], bool] | None = self.deskTopClose
        self._onCreate: Callable[[WinBase], bool] | None = None

        self._iconBtn: Button = self.addButton(Rect(0, 0, DefaultParams.FRAME_TITLE_HEIGHT, DefaultParams.FRAME_TITLE_HEIGHT))\
            .setOffPicture('defaultIcon.png')\
            .setOverPicture('defaultIcon.png')\
            .setDownPicture('defaultIcon.png')
        self.addToFrameComponentSet(self._iconBtn)

        # _captionLabel宽度减32是为了扣除左边的图标，再减32是为了扣除右边的关闭按钮
        self._captionLabel: Label = self.addLabel(Rect(DefaultParams.FRAME_TITLE_HEIGHT, 0, self._rect.width - 2 * DefaultParams.FRAME_TITLE_HEIGHT, DefaultParams.FRAME_TITLE_HEIGHT))\
            .setText(self._caption)\
            .setTextUpColor(DefaultColor.TEXT.value)\
            .setTextOverColor(DefaultColor.TEXT.value)\
            .setTextDownColor(DefaultColor.TEXT.value)\
            .setTextSize(12)
        self.addToFrameComponentSet(self._captionLabel)

        # 参考Windows窗口的按钮，大小似乎只有32点阵宽高
        self.__closeBtn: Button = self.addButton(Rect(rect.width - DefaultParams.FRAME_TITLE_HEIGHT, 0, DefaultParams.FRAME_TITLE_HEIGHT, DefaultParams.FRAME_TITLE_HEIGHT))\
            .setOffPicture('cross_up.png')\
            .setOverPicture('cross_over.png')\
            .setDownPicture('cross_down.png')\
            .setClickCallBack(self._onClose)
        self.addToFrameComponentSet(self.__closeBtn)

        self._clientRect: Rect = Rect(
            0, DefaultParams.FRAME_TITLE_HEIGHT, rect.width, rect.height - DefaultParams.FRAME_TITLE_HEIGHT)
        self._clientSurface: pygame.Surface = pygame.Surface(
            (rect.width, rect.height - DefaultParams.FRAME_TITLE_HEIGHT))

        if parent == None:
            self._isDesktop: bool = True
        else:
            self._isDesktop: bool = False
        self.FormCreated()

    # 每个自定义回调函数的派生类都要实现该方法，并确保调用父类的该方法，以减少内存引用数量
    def clearCallBack(self):
        super().clearCallBack()
        self._onClose: Callable[[WinBase], bool] | None = None
        self.__closeBtn.setClickCallBack(None)
        self._onCreate: Callable[[WinBase], bool] | None = None

    def draw(self):
        if self._isShow == False:
            return
        # 第一步应该先擦除屏幕，一般来说只需要最底层的deskTop窗体实例调用该函数即可
        self.wipeOff()

        # 接着依次绘制窗体和窗体上的组件、边框等，先绘制自己的，再调用子窗体的方法来绘制处于上层的子窗体
        self.drawForm()

        # 再根据输入焦点画键盘输入的光标
        self.drawCursor()

        # 所有都画完后，将surface贴到父窗体的clientSurface上，如果是deskTop窗体，它的父窗体clientSurface就是pgzero.game.screen
        # if self._isDesktop:

        parentSurface = self.getParentSurface()
        parentSurface.blit(self._surface, self._pos)

        # 最后画处于最上层的鼠标
        self.drawMousePointer()

    def drawForm(self):
        # 对于桌面来说，建议使用全屏模式，这里注释掉是为了方便调式
        if self._isDesktop:
            pgzero.game.screen = pygame.display.set_mode(
                self._rect.size, pygame.NOFRAME)  # |pygame.FULLSCREEN|pygame.SCALED)
            pass

        for childWin in self._zBuffer:
            if childWin == self:
                continue
            childWin.drawForm()

        self._surface.blit(self._clientSurface,
                           (self._clientRect.left, self._clientRect.top))

        self.drawBorder()

        # 所有都画完后，将surface贴到父窗体的surface上
        if self._isDesktop == False:
            parentSurface = self.getParentSurface()
            parentSurface.blit(self._surface, self._pos)
            #self.getParentSurface().blit(self._surface, self._pos)

    def drawBorder(self):
        if self._borderVisible:
            pygame.draw.rect(self._surface, self._borderColor, Rect(
                0, 0, self._rect.width, self._rect.height), self._borderThickness)
            pygame.draw.line(self._surface, self._borderColor, (0, DefaultParams.FRAME_TITLE_HEIGHT),
                             (self._rect.width, DefaultParams.FRAME_TITLE_HEIGHT))

    def drawMousePointer(self):
        if self._isDesktop:
            # convert to screen rect
            desktopRect: Rect = Rect(
                WinBase.g_desktopPos[0], WinBase.g_desktopPos[1], self._rect.width, self._rect.height)
            if desktopRect.collidepoint(WinBase.g_mouseCtrl.position) == False:
                return
            pass
        if self._absoluteRect.collidepoint(self._mousePos):
            parentSurface = self.getParentSurface()
            parentSurface.blit(self._mousePointer, self._mousePos)

    def drawCursor(self):
        pass

    def update(self):
        for childWin in self._zBuffer:
            if childWin == self:
                continue
            childWin.update()
        # 这里可以进行update计算

    def eventProcessor(self, winEvent: WinEvent) -> bool:
        if super().eventProcessor(winEvent) == False:
            match winEvent.type:
                case WinEventType.WET_FORM:
                    match winEvent.subType:
                        case FormSubEvent.FORM_CREATE:
                            if self._isDesktop:
                                WinBase.moveDesktopAbs(
                                    WinBase.g_desktopPos[0], WinBase.g_desktopPos[1]-32)
                            if self._onCreate != None:
                                return self._onCreate()
            return False
        return True

    # 鼠标类事件处理要返回False，因为需要桌面窗体来绘制定制鼠标
    def onMouseMove(self, pos) -> bool:
        self._mousePos = pos
        return False

    def onMouseDown(self, pos, buttons) -> bool:
        self._mousePos = pos
        return False

    def onMouseUp(self, pos, button) -> bool:
        self._mousePos = pos
        return False

    def onMouseDrag(self, delta, buttons) -> bool:
        if self._isDesktop == False:
            if self._captionLabel.convertToAbsoluteRect().collidepoint(self._mousePos):
                self._rect.left += delta[0]
                self._rect.top += delta[1]
                self._pos = (self._rect.left, self._rect.top)
                self.adjustAbsolutePosition()
            self._mousePos = (
                self._mousePos[0] + delta[0], self._mousePos[1] + delta[1])
        else:
            if self._captionLabel.convertToAbsoluteRect().collidepoint(self._mousePos):
                WinBase.g_desktopPos = (
                    WinBase.g_desktopPos[0] + delta[0], WinBase.g_desktopPos[1] + delta[1])
                WinBase.moveDesktopAbs(
                    WinBase.g_desktopPos[0], WinBase.g_desktopPos[1])
            else:
                self._mousePos = (
                    self._mousePos[0] + delta[0], self._mousePos[1] + delta[1])
        return False

    def onKeyPress(self, key: keys) -> bool:
        return False

    def onShonw(self):
        pass

    def FormCreated(self):
        winEvent = WinEvent(WinEventType.WET_FORM,
                            FormSubEvent.FORM_CREATE, {})
        WinBase.pumpEvent(self, winEvent)

    def onClose(self):
        pass

    @property
    def onClose(self):
        return self._onClose

    @onClose.setter
    def onClose(self, fn):
        if fn == None and self._isDesktop:
            fn = self.deskTopClose
        self._onClose = fn
        self.__closeBtn.onClick = fn

    def deskTopClose(self) -> bool:
        if self._isDesktop:
            sys.exit()

    def setCloseCallBack(self, fn: Callable[[WinBase], bool] | None) -> WinBase:
        self.onClose = fn
        return self

    def setCreateCallBack(self, fn: Callable[[WinBase], bool] | None) -> WinBase:
        self._onCreate = fn
        return self

    def setCaption(self, text: str) -> WinBase:
        self.caption = text
        self._captionLabel.setText(text)
        return self

    def setIcon(self, iconPath: str) -> WinBase:
        return self

    def addButton(self, rect: Rect) -> Button:
        return Button(self, rect)

    def addLabel(self, rect: Rect) -> Label:
        return Label(self, rect)

    def addEdit(self, rect: Rect) -> Edit:
        return Edit(self, rect)
