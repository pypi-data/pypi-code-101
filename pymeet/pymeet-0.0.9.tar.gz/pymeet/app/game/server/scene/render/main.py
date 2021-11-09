from typing import Tuple
from pygame import Surface

from pymeet.core import usecase

from .base import Renderer, CharacterRenderer, GroundRenderer
from .sheet import sheet
from .character.main import MainCharacterRenderer
from .ground.random import RandomTileGroundRenderer


class GameServerSceneRenderer(Renderer):
    def __init__(self, dimension: Tuple[int, int]):
        self._dimension: Tuple[int, int] = dimension
        sheet.scale(0.25)

        self._screen_center = (self._dimension[0]/2, self._dimension[1]/2)
        self._main_character_renderer: CharacterRenderer = MainCharacterRenderer(self._screen_center)
        self._ground_renderer: GroundRenderer = RandomTileGroundRenderer(
            dimension=self._dimension,
            screen_center=self._screen_center,
        )
        self._tmp_walk_count = 0

    def render(self, screen: Surface):
        main_character = usecase.character.view_from_id('000')
        self._ground_renderer.render_ground(screen, main_character.position.get_tuple())
        self._main_character_renderer.render_character(screen, main_character)
