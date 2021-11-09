from typing import Tuple, Optional
from math import ceil
import random
import pygame as pg
from pygame import Surface, Rect

from pymeet.app.game.server.scene.render.base import GroundRenderer
from pymeet.app.game.server.scene.render.sheet import sheet
from pymeet.app.game.server.scene.render.conversion.position import unit_to_pixel


class RandomTileBuffer:
    def __init__(self, screen_dimension: Tuple[int, int]):
        self._screen_dimension: Tuple[int, int] = screen_dimension
        self._n_tiles_exceed: Tuple[int, int] = (1, 1)

        self._is_generated: bool = False
        self._center: Optional[Tuple[int, int]] = None
        self._surface: Optional[Surface] = None
        self._dimension: Optional[Tuple[float, float]] = None
        self._margin: Optional[Tuple[float, float]] = None
        self._one_tile_dimension: Optional[Tuple[float, float]] = None
        self._n_cols: Optional[int] = None
        self._n_rows: Optional[int] = None

    @property
    def center(self) -> Tuple[int, int]:
        if not self._is_generated:
            self._generate_initial_surface()
        return self._center

    @property
    def center_in_pixel(self) -> Tuple[float, float]:
        j_center, i_center = self.center
        return j_center*self.one_tile_dimension[0], i_center*self.one_tile_dimension[1]

    def _shift_x(self, sign):
        dest = [0, 0, *self._dimension]
        otd = self.one_tile_dimension
        area = [sign*otd[0], 0, self._dimension[0] - sign*otd[0], self.dimension[1]]
        buffer = Surface(self._dimension, pg.SRCALPHA).convert_alpha()
        buffer.blit(self._surface, dest, Rect(area))
        self._surface = buffer
        self._center = (self._center[0] + sign, self._center[1])

        x_padding = int((self._n_cols - 1) / 2)
        y_padding = int((self._n_rows - 1) / 2)

        j = self._center[0] + sign * x_padding
        if sign == +1:
            x = self.one_tile_dimension[0] * (self._n_cols - 1)
        elif sign == -1:
            x = 0
        else:
            raise NotImplementedError()

        for i in range(-y_padding, y_padding + 1):
            y = self.one_tile_dimension[1] * (i + y_padding)
            self._render_tile_at(self.surface, (x, y), self._center[1] + i, j)

    def _shift_y(self, sign):
        dest = [0, 0, *self._dimension]
        otd = self.one_tile_dimension
        area = [0, sign*otd[1], self._dimension[0], self.dimension[1]-sign*otd[1]]
        buffer = Surface(self._dimension, pg.SRCALPHA).convert_alpha()
        buffer.blit(self._surface, dest, Rect(area))
        self._surface = buffer
        self._center = (self._center[0], self._center[1]+sign)

        y_padding = int((self._n_rows-1) / 2)
        x_padding = int((self._n_cols-1) / 2)

        i = self._center[1] + sign*y_padding
        if sign == +1:
            y = self.one_tile_dimension[1] * (self._n_rows - 1)
        elif sign == -1:
            y = 0
        else:
            raise NotImplementedError()

        for j in range(-x_padding, x_padding+1):
            x = self.one_tile_dimension[0] * (j + x_padding)
            self._render_tile_at(self.surface, (x, y), i, self._center[0] + j)

    def shift_to_left(self):
        self._shift_x(+1)

    def shift_to_right(self):
        self._shift_x(-1)

    def shift_up(self):
        self._shift_y(+1)

    def shift_down(self):
        self._shift_y(-1)

    @property
    def one_tile_dimension(self) -> Tuple[float, float]:
        if self._one_tile_dimension is None:
            self._one_tile_dimension = sheet.get_dimension('background-1')
        return self._one_tile_dimension

    @property
    def margin(self):
        if not self._is_generated:
            self._generate_initial_surface()
        return self._margin

    @property
    def dimension(self):
        if not self._is_generated:
            self._generate_initial_surface()
        return self._dimension

    @property
    def surface(self) -> Surface:
        if not self._is_generated:
            self._generate_initial_surface()
        return self._surface

    @staticmethod
    def _render_tile_at(surface: Surface, target: Tuple[float, float], i: int, j: int):
        seed = ((i + j)*(i + j + 1)/2) + i
        random.seed(seed)
        m = random.choices([1, 2, 3, 4, 5, 6], weights=[25, 25, 12, 3, 3, 12], k=1)[0]
        sheet.render(f'background-{m}', surface, target)

    def _generate_initial_surface(self):
        assert not self._is_generated

        width, height = self._screen_dimension
        tile_width, tile_height = self.one_tile_dimension
        self._n_cols = ceil((width / 2 - tile_width / 2) / tile_width) * 2 + self._n_tiles_exceed[0]*2 + 1
        self._n_rows = ceil((height / 2 - tile_height / 2) / tile_height) * 2 + self._n_tiles_exceed[1]*2 + 1

        self._dimension = self._n_cols * tile_width, self._n_rows * tile_height
        self._margin = (self._dimension[0] - width) / 2, (self._dimension[1] - height) / 2
        surface = Surface(self._dimension, pg.SRCALPHA).convert_alpha()

        y_padding = int((self._n_rows - 1) / 2)
        x_padding = int((self._n_cols - 1) / 2)
        for i in range(-y_padding, y_padding+1):
            y = self.one_tile_dimension[1] * (i + y_padding)
            for j in range(-x_padding, x_padding+1):
                x = self.one_tile_dimension[0] * (j + x_padding)
                self._render_tile_at(surface, (x, y), i, j)

        self._surface = surface
        self._center = (0, 0)
        self._is_generated = True


class RandomTileGroundRenderer(GroundRenderer):
    def __init__(self, dimension: Tuple[int, int], screen_center: Tuple[float, float]):
        self._dimension: Tuple[int, int] = dimension
        self._screen_center: Tuple[float, float] = screen_center

        self._tile: RandomTileBuffer = RandomTileBuffer(self._dimension)

    def _adjust_buffer_to_position(self, x: float, y: float):
        x_center, y_center = self._tile.center_in_pixel
        dx, dy = x - x_center, y - y_center

        if self._tile.one_tile_dimension[0]/2 < dx:
            self._tile.shift_to_left()
        elif dx < -self._tile.one_tile_dimension[0]/2:
            self._tile.shift_to_right()

        if self._tile.one_tile_dimension[1]/2 < dy:
            self._tile.shift_up()
        elif dy < -self._tile.one_tile_dimension[1]/2:
            self._tile.shift_down()

    def render_ground(self, screen: Surface, character_position: Tuple[float, float]):
        screen.fill('grey')
        x, y = unit_to_pixel(character_position)

        self._adjust_buffer_to_position(x, y)

        area_x = self._tile.margin[0]+x-self._tile.center_in_pixel[0]
        area_y = self._tile.margin[1]+y-self._tile.center_in_pixel[1]
        area = pg.Rect(area_x, area_y, *self._tile.dimension)
        screen.blit(self._tile.surface, [0, 0, *self._dimension], area)
        print(self._tile.center)
