from enum import IntEnum
from collections.abc import Callable

import os
import sys
import pygame
import pgzero.game
from pygame.rect import Rect

from pgzero.actor import Actor
from pgzero.constants import mouse
from pgzero.constants import keys

from pzwin.Constants import *
from pzwin.WinEvent import *
from pzwin.WinBase import WinBase
from pzwin.Label import Label


class Edit(Label):

    def __init__(self, parent: WinBase, rect: Rect):
        super().__init__(parent, rect)

        self._text: str = 'text'
        self._editFocusOnBgColor: Color = DefaultColor.EDIT_FOCUS_ON_BG.value
        self._editFocusOffBgColor: Color = DefaultColor.EDIT_FOCUS_OFF_BG.value
        self._editFocusOnBdColor: Color = DefaultColor.EDIT_FOCUS_ON_BD.value
        self._editFocusOffBdColor: Color = DefaultColor.EDIT_FOCUS_OFF_BD.value
        self._editFocusOnTextColor: Color = DefaultColor.EDIT_FOCUS_ON_TEXT.value
        self._editFocusOffTextColor: Color = DefaultColor.EDIT_FOCUS_OFF_TEXT.value
        self._editCursorColor: Color = DefaultColor.EDIT_CURSOR.value

        self.setBorderVisible(True)
        self._onMouseUp = self.onMouseUp
        self._onKeyPress = self.onKeyPress
        self._onCharPress = self.onCharPress
        self._textRect: Rect = Rect(DefaultParams.EDIT_TEXT_EDGE, DefaultParams.EDIT_TEXT_EDGE,
                                    rect.width - 2 * DefaultParams.EDIT_TEXT_EDGE, rect.height - 2 * DefaultParams.EDIT_TEXT_EDGE)
        self._textSurface: pygame.Surface = pygame.Surface(self._textRect.size)

        self.buildEditSurface()

    def drawForm(self):
        if self._isFocusOn:
            self._surface.fill(self._editFocusOnBgColor)
        else:
            self._surface.fill(self._editFocusOffBgColor)
        self._surface.blit(self._textSurface, self._textRect)
        self.drawBorder()

        # 所有都画完后，将surface贴到父窗体的surface上
        parentSurface = self.getParentSurface()
        parentSurface.blit(self._surface, dest=self._pos)

    def buildEditSurface(self):
        if self._fontName not in self._fontEntity:
            currentPath = os.path.split(os.path.realpath(__file__))[0]
            self._fontEntity[self._fontName] = pygame.freetype.Font(
                os.path.join(currentPath, 'fonts', self._fontName), 20)

        targetX: int = 0
        targetY: int = 0

        if self._isFocusOn:
            self._textSurface.fill(self._editFocusOnBgColor)
            (textSurface, textRect) = self._fontEntity[self._fontName].render(
                self._text, fgcolor=self._editFocusOnTextColor, size=self._fontSize)

            if self._isHorizontalCenter:
                targetX = self._textRect.width // 2 - textRect.width // 2
            if self._isVerticalCenter:
                targetY = self._textRect.height // 2 - textRect.height // 2

            if textRect.width > self._textRect.width - DefaultParams.EDIT_CURSOR_THICKNESS - 1:
                self._textSurface.blit(textSurface, (self._textRect.width -
                                       textRect.width - DefaultParams.EDIT_CURSOR_THICKNESS - 1, targetY))
                curcorX = self._textRect.width - DefaultParams.EDIT_CURSOR_THICKNESS - 1
            else:
                self._textSurface.blit(textSurface, (0, targetY))
                curcorX = textRect.right + 1
            # 画Curcor
            pygame.draw.line(self._textSurface, self._editCursorColor, (curcorX, targetY),
                             (curcorX, textRect.bottom), DefaultParams.EDIT_CURSOR_THICKNESS)
        else:
            self._textSurface.fill(self._editFocusOffBgColor)
            (textSurface, textRect) = self._fontEntity[self._fontName].render(
                self._text, fgcolor=self._editFocusOffTextColor, size=self._fontSize)

            if self._isHorizontalCenter:
                targetX = self._textRect.width // 2 - textRect.width // 2
            if self._isVerticalCenter:
                targetY = self._textRect.height // 2 - textRect.height // 2

            if textRect.width > self._textRect.width:
                self._textSurface.blit(
                    textSurface, (self._textRect.width - textRect.width, targetY))
            else:
                self._textSurface.blit(textSurface, (0, targetY))

    def drawBorder(self):
        if self._borderVisible:
            if self._isFocusOn:
                pygame.draw.line(self._surface, self._editFocusOnBdColor, (0, self._rect.height - 1),
                                 (self._rect.width, self._rect.height - 1), self._borderThickness)
            else:
                pygame.draw.line(self._surface, self._editFocusOffBdColor, (0, self._rect.height - 1),
                                 (self._rect.width, self._rect.height - 1), self._borderThickness)

    def setFocusOn(self, isOn: bool):
        self._isFocusOn = isOn
        self.buildEditSurface()

    @property
    def text(self) -> str:
        return self._text

    @text.setter
    def text(self, value: str):
        self._text = value
        self.buildEditSurface()

    def onMouseUp(self, pos, button) -> bool:
        if button == mouse.LEFT and self._absoluteRect.collidepoint(pos):
            self.setFocusOn(True)
        else:
            self.setFocusOn(False)
        return False

    def onKeyPress(self, key: keys) -> bool:
        if self._isFocusOn:
            if key == keys.BACKSPACE:
                self.text = self.text[:-1]
            return True
        else:
            return False

    def onCharPress(self, unicode: str) -> bool:
        if self._isFocusOn:
            self.text += unicode
            return True
        return False
    # builder mode start here...
