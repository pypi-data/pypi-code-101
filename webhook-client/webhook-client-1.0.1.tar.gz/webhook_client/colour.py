import colorsys
import random

from typing import (
    Any,
    Optional,
    Tuple,
    Type,
    TypeVar,
    Union,
)

__all__ = (
    'Colour',
    'Color',
)

CT = TypeVar('CT', bound='Colour')


class Colour:
    __slots__ = ('value',)

    def __init__(self, value: int):
        if not isinstance(value, int):
            raise TypeError(f'Expected int parameter, received {value.__class__.__name__} instead.')

        self.value: int = value

    def _get_byte(self, byte: int) -> int:
        return (self.value >> (8 * byte)) & 0xff

    def __eq__(self, other: Any) -> bool:
        return isinstance(other, Colour) and self.value == other.value

    def __ne__(self, other: Any) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return f'#{self.value:0>6x}'

    def __int__(self) -> int:
        return self.value

    def __repr__(self) -> str:
        return f'<Colour value={self.value}>'

    def __hash__(self) -> int:
        return hash(self.value)

    @property
    def r(self) -> int:
        """:class:`int`: Returns the red component of the colour."""
        return self._get_byte(2)

    @property
    def g(self) -> int:
        """:class:`int`: Returns the green component of the colour."""
        return self._get_byte(1)

    @property
    def b(self) -> int:
        """:class:`int`: Returns the blue component of the colour."""
        return self._get_byte(0)

    def to_rgb(self) -> Tuple[int, int, int]:
        """Tuple[:class:`int`, :class:`int`, :class:`int`]: Returns an (r, g, b) tuple representing the colour."""
        return (self.r, self.g, self.b)

    @classmethod
    def from_rgb(cls: Type[CT], r: int, g: int, b: int) -> CT:
        """Constructs a :class:`Colour` from an RGB tuple."""
        return cls((r << 16) + (g << 8) + b)

    @classmethod
    def from_hsv(cls: Type[CT], h: float, s: float, v: float) -> CT:
        """Constructs a :class:`Colour` from an HSV tuple."""
        rgb = colorsys.hsv_to_rgb(h, s, v)
        return cls.from_rgb(*(int(x * 255) for x in rgb))

    @classmethod
    def default(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0``."""
        return cls(0)

    @classmethod
    def random(cls: Type[CT], *, seed: Optional[Union[int, str, float, bytes, bytearray]] = None) -> CT:
        """ Return a random colour. """
        rand = random if seed is None else random.Random(seed)
        return cls.from_hsv(rand.random(), 1, 1)

    @classmethod
    def teal(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0x1abc9c``."""
        return cls(0x1abc9c)

    @classmethod
    def dark_teal(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0x11806a``."""
        return cls(0x11806a)

    @classmethod
    def brand_green(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0x57F287``.

        .. versionadded:: 2.0
        """
        return cls(0x57F287)

    @classmethod
    def green(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0x2ecc71``."""
        return cls(0x2ecc71)

    @classmethod
    def dark_green(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0x1f8b4c``."""
        return cls(0x1f8b4c)

    @classmethod
    def blue(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0x3498db``."""
        return cls(0x3498db)

    @classmethod
    def dark_blue(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0x206694``."""
        return cls(0x206694)

    @classmethod
    def purple(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0x9b59b6``."""
        return cls(0x9b59b6)

    @classmethod
    def dark_purple(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0x71368a``."""
        return cls(0x71368a)

    @classmethod
    def magenta(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0xe91e63``."""
        return cls(0xe91e63)

    @classmethod
    def dark_magenta(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0xad1457``."""
        return cls(0xad1457)

    @classmethod
    def gold(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0xf1c40f``."""
        return cls(0xf1c40f)

    @classmethod
    def dark_gold(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0xc27c0e``."""
        return cls(0xc27c0e)

    @classmethod
    def orange(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0xe67e22``."""
        return cls(0xe67e22)

    @classmethod
    def dark_orange(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0xa84300``."""
        return cls(0xa84300)

    @classmethod
    def brand_red(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0xED4245``.

        .. versionadded:: 2.0
        """
        return cls(0xED4245)

    @classmethod
    def red(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0xe74c3c``."""
        return cls(0xe74c3c)

    @classmethod
    def dark_red(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0x992d22``."""
        return cls(0x992d22)

    @classmethod
    def lighter_grey(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0x95a5a6``."""
        return cls(0x95a5a6)

    lighter_gray = lighter_grey

    @classmethod
    def dark_grey(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0x607d8b``."""
        return cls(0x607d8b)

    dark_gray = dark_grey

    @classmethod
    def light_grey(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0x979c9f``."""
        return cls(0x979c9f)

    light_gray = light_grey

    @classmethod
    def darker_grey(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0x546e7a``."""
        return cls(0x546e7a)

    darker_gray = darker_grey

    @classmethod
    def og_blurple(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0x7289da``."""
        return cls(0x7289da)

    @classmethod
    def blurple(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0x5865F2``."""
        return cls(0x5865F2)

    @classmethod
    def greyple(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0x99aab5``."""
        return cls(0x99aab5)

    @classmethod
    def dark_theme(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0x36393F``.
        This will appear transparent on Discord's dark theme.

        .. versionadded:: 1.5
        """
        return cls(0x36393F)

    @classmethod
    def fuchsia(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0xEB459E``.

        .. versionadded:: 2.0
        """
        return cls(0xEB459E)

    @classmethod
    def yellow(cls: Type[CT]) -> CT:
        """A factory method that returns a :class:`Colour` with a value of ``0xFEE75C``.

        .. versionadded:: 2.0
        """
        return cls(0xFEE75C)


Color = Colour