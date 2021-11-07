from functools import partial
from itertools import chain, cycle
from logging import getLogger
from os import environ, path
from pprint import pformat
from string import whitespace
from typing import Dict, Union, Optional, Iterator, Sequence

from PIL import Image, ImageDraw

from dcspy import FONT, lcd_sdk, LcdInfo

try:
    from typing_extensions import TypedDict
except ImportError:
    from typing import TypedDict

BIOS_VALUE = TypedDict('BIOS_VALUE', {'class': str, 'args': Dict[str, int], 'value': Union[int, str], 'max_value': int}, total=False)
LOG = getLogger(__name__)


class Aircraft:
    def __init__(self, lcd_type: LcdInfo) -> None:
        """
        Create common aircraft.

        :param lcd_type: LCD type
        """
        self.lcd = lcd_type
        self.bios_data: Dict[str, BIOS_VALUE] = {}
        self.cycle_buttons: Dict[str, Iterator[int]] = {}
        self._debug_img = cycle(range(10))

    def button_request(self, button: int, request: str = '\n') -> str:
        """
        Prepare aircraft specific DCS-BIOS request for button pressed.

        For G13/G15/G510: 1-4
        For G19 9-15: LEFT = 9, RIGHT = 10, OK = 11, CANCEL = 12, UP = 13, DOWN = 14, MENU = 15

        If button is out of scope new line is return.

        :param button: possible values 1-4
        :param request: valid DCS-BIOS command as string
        :return: ready to send DCS-BIOS request
        """
        LOG.debug(f'{self.__class__.__name__} Button: {button}')
        LOG.debug(f'Request: {request.replace(whitespace[2], " ")}')
        return request

    @staticmethod
    def update_display(image: Image.Image) -> None:
        """Update display."""
        lcd_sdk.update_display(image)

    def prepare_image(self) -> Optional[Image.Image]:
        """
        Prepare image to be send to correct type of LCD.

        :return: image instance ready display on LCD
        """
        img_for_lcd = {1: partial(Image.new, mode='1', size=(self.lcd.width, self.lcd.height), color=self.lcd.bg),
                       2: partial(Image.new, mode='RGBA', size=(self.lcd.width, self.lcd.height), color=self.lcd.bg)}
        try:
            img = img_for_lcd[self.lcd.type]()
            getattr(self, f'draw_for_lcd_type_{self.lcd.type}')(img)
            img.save(path.join(environ.get('TEMP', ''), f'{self.__class__.__name__}_{next(self._debug_img)}.png'), 'PNG')
            return img
        except KeyError as err:
            LOG.debug(f'Wrong LCD type: {self.lcd} or key: {err}')
            return None

    def set_bios(self, selector: str, value: str) -> None:
        """
        Set value for DCS-BIOS selector.

        :param selector:
        :param value:
        """
        self.bios_data[selector]['value'] = value
        LOG.debug(f'{self.__class__.__name__} {selector} value: "{value}"')
        lcd_image = self.prepare_image()
        self.update_display(lcd_image)

    def get_bios(self, selector: str) -> Union[str, int]:
        """
        Get value for DCS-BIOS selector.

        :param selector:
        """
        try:
            return self.bios_data[selector]['value']
        except KeyError:
            return ''

    def draw_for_lcd_type_1(self, img: Image.Image) -> None:
        """Prepare image for Aircraft for Mono LCD."""
        raise NotImplementedError

    def draw_for_lcd_type_2(self, img: Image.Image) -> None:
        """Prepare image for Aircraft for Color LCD."""
        raise NotImplementedError

    def get_next_value_for_button(self, btn_name: str) -> int:
        """
        Get next int value (cycle fore and back) for button name.

        :param btn_name: BIOS button name
        """
        curr_val = int(self.get_bios(btn_name))
        max_val = self.bios_data[btn_name]['max_value']
        if not self.cycle_buttons[btn_name]:
            full_seed = list(range(max_val + 1)) + list(range(max_val - 1, 0, -1)) + list(range(max_val + 1))
            seed = full_seed[curr_val + 1:2 * max_val + curr_val + 1]
            LOG.debug(f'{self.__class__.__name__} {btn_name} full_seed: {full_seed} seed: {seed} curr_val: {curr_val}')
            self.cycle_buttons[btn_name] = cycle(chain(seed))
        return next(self.cycle_buttons[btn_name])

    def __repr__(self):
        return f'{super().__repr__()} with: {pformat(self.__dict__)}'


class FA18Chornet(Aircraft):
    def __init__(self, lcd_type: LcdInfo) -> None:
        """
        Create F/A-18C Hornet.

        :param lcd_type: LCD type
        """
        super().__init__(lcd_type)
        self.bios_data: Dict[str, BIOS_VALUE] = {
            'UFC_SCRATCHPAD_STRING_1_DISPLAY': {'class': 'StringBuffer', 'args': {'address': 0x744e, 'max_length': 2}, 'value': str()},
            'UFC_SCRATCHPAD_STRING_2_DISPLAY': {'class': 'StringBuffer', 'args': {'address': 0x7450, 'max_length': 2}, 'value': str()},
            'UFC_SCRATCHPAD_NUMBER_DISPLAY': {'class': 'StringBuffer', 'args': {'address': 0x7446, 'max_length': 8}, 'value': str()},
            'UFC_OPTION_DISPLAY_1': {'class': 'StringBuffer', 'args': {'address': 0x7432, 'max_length': 4}, 'value': str()},
            'UFC_OPTION_DISPLAY_2': {'class': 'StringBuffer', 'args': {'address': 0x7436, 'max_length': 4}, 'value': str()},
            'UFC_OPTION_DISPLAY_3': {'class': 'StringBuffer', 'args': {'address': 0x743a, 'max_length': 4}, 'value': str()},
            'UFC_OPTION_DISPLAY_4': {'class': 'StringBuffer', 'args': {'address': 0x743e, 'max_length': 4}, 'value': str()},
            'UFC_OPTION_DISPLAY_5': {'class': 'StringBuffer', 'args': {'address': 0x7442, 'max_length': 4}, 'value': str()},
            'UFC_COMM1_DISPLAY': {'class': 'StringBuffer', 'args': {'address': 0x7424, 'max_length': 2}, 'value': str()},
            'UFC_COMM2_DISPLAY': {'class': 'StringBuffer', 'args': {'address': 0x7426, 'max_length': 2}, 'value': str()},
            'UFC_OPTION_CUEING_1': {'class': 'StringBuffer', 'args': {'address': 0x7428, 'max_length': 1}, 'value': str()},
            'UFC_OPTION_CUEING_2': {'class': 'StringBuffer', 'args': {'address': 0x742a, 'max_length': 1}, 'value': str()},
            'UFC_OPTION_CUEING_3': {'class': 'StringBuffer', 'args': {'address': 0x742c, 'max_length': 1}, 'value': str()},
            'UFC_OPTION_CUEING_4': {'class': 'StringBuffer', 'args': {'address': 0x742e, 'max_length': 1}, 'value': str()},
            'UFC_OPTION_CUEING_5': {'class': 'StringBuffer', 'args': {'address': 0x7430, 'max_length': 1}, 'value': str()},
            'IFEI_FUEL_DOWN': {'class': 'StringBuffer', 'args': {'address': 0x748a, 'max_length': 6}, 'value': str()},
            'IFEI_FUEL_UP': {'class': 'StringBuffer', 'args': {'address': 0x7490, 'max_length': 6}, 'value': str()}}

    def _draw_common_data(self, draw: ImageDraw, scale: int) -> ImageDraw:
        scratch_1 = self.get_bios("UFC_SCRATCHPAD_STRING_1_DISPLAY")
        scratch_2 = self.get_bios("UFC_SCRATCHPAD_STRING_2_DISPLAY")
        scratch_num = self.get_bios("UFC_SCRATCHPAD_NUMBER_DISPLAY")
        draw.text(xy=(0, 0), fill=self.lcd.fg, font=FONT[16 * scale],
                  text=f'{scratch_1}{scratch_2}{scratch_num}')
        draw.line(xy=(0, 20 * scale, 115 * scale, 20 * scale), fill=self.lcd.fg, width=1)

        draw.rectangle(xy=(0, 29 * scale, 20 * scale, 42 * scale), fill=self.lcd.bg, outline=self.lcd.fg)
        draw.text(xy=(2 * scale, 29 * scale), text=self.get_bios('UFC_COMM1_DISPLAY'), fill=self.lcd.fg, font=FONT[16 * scale])

        offset_comm2 = 44 * scale
        draw.rectangle(xy=(139 * scale - offset_comm2, 29 * scale, 159 * scale - offset_comm2, 42 * scale), fill=self.lcd.bg, outline=self.lcd.fg)
        draw.text(xy=(140 * scale - offset_comm2, 29 * scale), text=self.get_bios('UFC_COMM2_DISPLAY'), fill=self.lcd.fg, font=FONT[16 * scale])

        for i in range(1, 6):
            offset = (i - 1) * 8 * scale
            draw.text(xy=(120 * scale, offset), fill=self.lcd.fg, font=FONT[11 * scale],
                      text=f'{i}{self.get_bios(f"UFC_OPTION_CUEING_{i}")}{self.get_bios(f"UFC_OPTION_DISPLAY_{i}")}')

        draw.text(xy=(36 * scale, 29 * scale), text=self.get_bios('IFEI_FUEL_UP'), fill=self.lcd.fg, font=FONT[16 * scale])
        return draw

    def draw_for_lcd_type_1(self, img: Image.Image) -> None:
        """Prepare image for F/A-18C Hornet for Mono LCD."""
        self._draw_common_data(draw=ImageDraw.Draw(img), scale=1)

    def draw_for_lcd_type_2(self, img: Image.Image) -> None:
        """Prepare image for F/A-18C Hornet for Color LCD."""
        draw = self._draw_common_data(draw=ImageDraw.Draw(img), scale=2)
        draw.text(xy=(72, 100), text=self.get_bios('IFEI_FUEL_DOWN'), fill=self.lcd.fg, font=FONT[32])

    def set_bios(self, selector: str, value: str) -> None:
        """
        Set new data.

        :param selector:
        :param value:
        """
        if selector in ('UFC_SCRATCHPAD_STRING_1_DISPLAY', 'UFC_SCRATCHPAD_STRING_2_DISPLAY',
                        'UFC_COMM1_DISPLAY', 'UFC_COMM2_DISPLAY'):
            value = value.replace('`', '1').replace('~', '2')
        super().set_bios(selector, value)

    def button_request(self, button: int, request: str = '\n') -> str:
        """
        Prepare F/A-18 Hornet specific DCS-BIOS request for button pressed.

        For G13/G15/G510: 1-4
        For G19 9-15: LEFT = 9, RIGHT = 10, OK = 11, CANCEL = 12, UP = 13, DOWN = 14, MENU = 15
        If button is out of scope new line is return.
        :param button: possible values 1-4
        :param request: valid DCS-BIOS command as string
        :return: ready to send DCS-BIOS request
        """
        action = {1: 'UFC_COMM1_CHANNEL_SELECT DEC\n',
                  2: 'UFC_COMM1_CHANNEL_SELECT INC\n',
                  3: 'UFC_COMM2_CHANNEL_SELECT DEC\n',
                  4: 'UFC_COMM2_CHANNEL_SELECT INC\n',
                  9: 'UFC_COMM1_CHANNEL_SELECT DEC\n',
                  10: 'UFC_COMM1_CHANNEL_SELECT INC\n',
                  14: 'UFC_COMM2_CHANNEL_SELECT DEC\n',
                  13: 'UFC_COMM2_CHANNEL_SELECT INC\n',
                  15: 'IFEI_DWN_BTN 1\nIFEI_DWN_BTN 0\n',
                  12: 'IFEI_UP_BTN 1\nIFEI_UP_BTN 0\n'}
        return super().button_request(button, action.get(button, '\n'))


class F16C50(Aircraft):
    def __init__(self, lcd_type: LcdInfo) -> None:
        """
        Create F-16C Viper.

        :param lcd_type: LCD type
        """
        super().__init__(lcd_type)
        self.bios_data: Dict[str, BIOS_VALUE] = {
            'DED_LINE_1': {'class': 'StringBuffer', 'args': {'address': 0x4500, 'max_length': 25}, 'value': str()},
            'DED_LINE_2': {'class': 'StringBuffer', 'args': {'address': 0x451a, 'max_length': 25}, 'value': str()},
            'DED_LINE_3': {'class': 'StringBuffer', 'args': {'address': 0x4534, 'max_length': 25}, 'value': str()},
            'DED_LINE_4': {'class': 'StringBuffer', 'args': {'address': 0x454e, 'max_length': 25}, 'value': str()},
            'DED_LINE_5': {'class': 'StringBuffer', 'args': {'address': 0x4568, 'max_length': 25}, 'value': str()},
            'IFF_MASTER_KNB': {'class': 'IntegerBuffer', 'args': {'address': 0x444a, 'mask': 0x700, 'shift_by': 0x8}, 'value': int(), 'max_value': 4},
            'IFF_ENABLE_SW': {'class': 'IntegerBuffer', 'args': {'address': 0x444e, 'mask': 0x3, 'shift_by': 0x0}, 'value': int(), 'max_value': 2},
            'IFF_M4_CODE_SW': {'class': 'IntegerBuffer', 'args': {'address': 0x444a, 'mask': 0x1800, 'shift_by': 0xb}, 'value': int(), 'max_value': 2},
            'IFF_M4_REPLY_SW': {'class': 'IntegerBuffer', 'args': {'address': 0x444a, 'mask': 0x6000, 'shift_by': 0xd}, 'value': int(), 'max_value': 2}}
        self.cycle_buttons = {'IFF_MASTER_KNB': '', 'IFF_ENABLE_SW': '', 'IFF_M4_CODE_SW': '', 'IFF_M4_REPLY_SW': ''}  # type: ignore

    def draw_for_lcd_type_1(self, img: Image.Image) -> None:
        """Prepare image for F-16C Viper for Mono LCD."""
        draw = ImageDraw.Draw(img)
        for i in range(1, 6):
            offset = (i - 1) * 8
            # replace 'o' to degree sign and 'a' with up-down arrow 2195 or black diamond 2666
            text = str(self.get_bios(f'DED_LINE_{i}')).replace('o', '\u00b0').replace('a', '\u2666')
            draw.text(xy=(0, offset), text=text, fill=self.lcd.fg, font=FONT[11])

    def draw_for_lcd_type_2(self, img: Image.Image) -> None:
        """Prepare image for F-16C Viper for Color LCD."""
        draw = ImageDraw.Draw(img)
        for i in range(1, 6):
            offset = (i - 1) * 16
            # replace 'o' to degree sign and 'a' with up-down arrow 2195 or black diamond 2666
            text = str(self.get_bios(f'DED_LINE_{i}')).replace('o', '\u00b0').replace('a', '\u2666')
            draw.text(xy=(0, offset), text=text, fill=self.lcd.fg, font=FONT[22])

    def button_request(self, button: int, request: str = '\n') -> str:
        """
        Prepare F-16C Viper specific DCS-BIOS request for button pressed.

        For G13/G15/G510: 1-4
        For G19 9-15: LEFT = 9, RIGHT = 10, OK = 11, CANCEL = 12, UP = 13, DOWN = 14, MENU = 15
        :param button: possible values 1-4
        :param request: valid DCS-BIOS command as string
        :return: ready to send DCS-BIOS request
        """
        button_map = {1: 'IFF_MASTER_KNB', 2: 'IFF_ENABLE_SW', 3: 'IFF_M4_CODE_SW', 4: 'IFF_M4_REPLY_SW',
                      9: 'IFF_MASTER_KNB', 10: 'IFF_ENABLE_SW', 14: 'IFF_M4_CODE_SW', 13: 'IFF_M4_REPLY_SW'}
        button_bios_name = button_map[button]
        setting = self.get_next_value_for_button(button_bios_name)
        return super().button_request(button, f'{button_bios_name} {setting}\n')


class Ka50(Aircraft):
    def __init__(self, lcd_type: LcdInfo) -> None:
        """
        Create Ka-50 Black Shark.

        :param lcd_type: LCD type
        """
        super().__init__(lcd_type)
        self.bios_data: Dict[str, BIOS_VALUE] = {
            'PVI_LINE1_APOSTROPHE1': {'class': 'StringBuffer', 'args': {'address': 0x1934, 'max_length': 1}, 'value': str()},
            'PVI_LINE1_APOSTROPHE2': {'class': 'StringBuffer', 'args': {'address': 0x1936, 'max_length': 1}, 'value': str()},
            'PVI_LINE1_POINT': {'class': 'StringBuffer', 'args': {'address': 0x1930, 'max_length': 1}, 'value': str()},
            'PVI_LINE1_SIGN': {'class': 'StringBuffer', 'args': {'address': 0x1920, 'max_length': 1}, 'value': str()},
            'PVI_LINE1_TEXT': {'class': 'StringBuffer', 'args': {'address': 0x1924, 'max_length': 6}, 'value': str()},
            'PVI_LINE2_APOSTROPHE1': {'class': 'StringBuffer', 'args': {'address': 0x1938, 'max_length': 1}, 'value': str()},
            'PVI_LINE2_APOSTROPHE2': {'class': 'StringBuffer', 'args': {'address': 0x193a, 'max_length': 1}, 'value': str()},
            'PVI_LINE2_POINT': {'class': 'StringBuffer', 'args': {'address': 0x1932, 'max_length': 1}, 'value': str()},
            'PVI_LINE2_SIGN': {'class': 'StringBuffer', 'args': {'address': 0x1922, 'max_length': 1}, 'value': str()},
            'PVI_LINE2_TEXT': {'class': 'StringBuffer', 'args': {'address': 0x192a, 'max_length': 6}, 'value': str()},
            'AP_ALT_HOLD_LED': {'class': 'IntegerBuffer', 'args': {'address': 0x1936, 'mask': 0x8000, 'shift_by': 0xf}, 'value': int()},
            'AP_BANK_HOLD_LED': {'class': 'IntegerBuffer', 'args': {'address': 0x1936, 'mask': 0x200, 'shift_by': 0x9}, 'value': int()},
            'AP_FD_LED': {'class': 'IntegerBuffer', 'args': {'address': 0x1938, 'mask': 0x200, 'shift_by': 0x9}, 'value': int()},
            'AP_HDG_HOLD_LED': {'class': 'IntegerBuffer', 'args': {'address': 0x1936, 'mask': 0x800, 'shift_by': 0xb}, 'value': int()},
            'AP_PITCH_HOLD_LED': {'class': 'IntegerBuffer', 'args': {'address': 0x1936, 'mask': 0x2000, 'shift_by': 0xd}, 'value': int()}}

    def button_request(self, button: int, request: str = '\n') -> str:
        """
        Prepare Ka-50 Black Shark specific DCS-BIOS request for button pressed.

        For G13/G15/G510: 1-4
        For G19 9-15: LEFT = 9, RIGHT = 10, OK = 11, CANCEL = 12, UP = 13, DOWN = 14, MENU = 15
        If button is out of scope new line is return.
        :param button: possible values 1-4
        :param request: valid DCS-BIOS command as string
        :return: ready to send DCS-BIOS request
        """
        action = {1: 'PVI_WAYPOINTS_BTN 1\nPVI_WAYPOINTS_BTN 0\n',
                  2: 'PVI_FIXPOINTS_BTN 1\nPVI_FIXPOINTS_BTN 0\n',
                  3: 'PVI_AIRFIELDS_BTN 1\nPVI_AIRFIELDS_BTN 0\n',
                  4: 'PVI_TARGETS_BTN 1\nPVI_TARGETS_BTN 0\n',
                  9: 'PVI_WAYPOINTS_BTN 1\nPVI_WAYPOINTS_BTN 0\n',
                  10: 'PVI_FIXPOINTS_BTN 1\nPVI_FIXPOINTS_BTN 0\n',
                  14: 'PVI_AIRFIELDS_BTN 1\nPVI_AIRFIELDS_BTN 0\n',
                  13: 'PVI_TARGETS_BTN 1\nPVI_TARGETS_BTN 0\n'}
        return super().button_request(button, action.get(button, '\n'))

    def _auto_pilot_switch_1(self, draw_obj: ImageDraw) -> None:
        """
        Draw rectangle and add text for autopilot channels in correct coordinates.

        :param draw_obj: ImageDraw object form PIL
        """
        for c_rect, c_text, ap_channel, turn_on in (((111, 1, 124, 18), (114, 3), 'B', self.get_bios('AP_BANK_HOLD_LED')),
                                                    ((128, 1, 141, 18), (130, 3), 'P', self.get_bios('AP_PITCH_HOLD_LED')),
                                                    ((145, 1, 158, 18), (147, 3), 'F', self.get_bios('AP_FD_LED')),
                                                    ((111, 22, 124, 39), (114, 24), 'H', self.get_bios('AP_HDG_HOLD_LED')),
                                                    ((128, 22, 141, 39), (130, 24), 'A', self.get_bios('AP_ALT_HOLD_LED'))):
            if turn_on:
                draw_obj.rectangle(c_rect, fill=self.lcd.fg, outline=self.lcd.fg)
                draw_obj.text(xy=c_text, text=ap_channel, fill=self.lcd.bg, font=FONT[16])
            else:
                draw_obj.rectangle(xy=c_rect, fill=self.lcd.bg, outline=self.lcd.fg)
                draw_obj.text(xy=c_text, text=ap_channel, fill=self.lcd.fg, font=FONT[16])

    def _auto_pilot_switch_2(self, draw_obj: ImageDraw) -> None:
        """
        Draw rectangle and add text for autopilot channels in correct coordinates.

        :param draw_obj: ImageDraw object form PIL
        """
        for c_rect, c_text, ap_channel, turn_on in (((222, 2, 248, 36), (228, 6), 'B', self.get_bios('AP_BANK_HOLD_LED')),
                                                    ((256, 2, 282, 36), (260, 6), 'P', self.get_bios('AP_PITCH_HOLD_LED')),
                                                    ((290, 2, 316, 36), (294, 6), 'F', self.get_bios('AP_FD_LED')),
                                                    ((222, 44, 248, 78), (228, 48), 'H', self.get_bios('AP_HDG_HOLD_LED')),
                                                    ((256, 44, 282, 78), (260, 48), 'A', self.get_bios('AP_ALT_HOLD_LED'))):
            if turn_on:
                draw_obj.rectangle(c_rect, fill=self.lcd.fg, outline=self.lcd.fg)
                draw_obj.text(xy=c_text, text=ap_channel, fill=self.lcd.bg, font=FONT[32])
            else:
                draw_obj.rectangle(xy=c_rect, fill=self.lcd.bg, outline=self.lcd.fg)
                draw_obj.text(xy=c_text, text=ap_channel, fill=self.lcd.fg, font=FONT[32])

    def draw_for_lcd_type_1(self, img: Image.Image) -> None:
        """Prepare image for Ka-50 Black Shark for Mono LCD."""
        draw = ImageDraw.Draw(img)
        for rect_xy in [(0, 1, 85, 18), (0, 22, 85, 39), (88, 1, 103, 18), (88, 22, 103, 39)]:
            draw.rectangle(xy=rect_xy, fill=self.lcd.bg, outline=self.lcd.fg)
        line1, line2 = self._generate_pvi_lines()
        draw.text(xy=(2, 3), text=line1, fill=self.lcd.fg, font=FONT[16])
        draw.text(xy=(2, 24), text=line2, fill=self.lcd.fg, font=FONT[16])
        self._auto_pilot_switch_1(draw)

    def draw_for_lcd_type_2(self, img: Image.Image) -> None:
        """Prepare image for Ka-50 Black Shark for Mono LCD."""
        draw = ImageDraw.Draw(img)
        for rect_xy in [(0, 2, 170, 36), (0, 44, 170, 78), (176, 2, 206, 36), (176, 44, 203, 78)]:
            draw.rectangle(xy=rect_xy, fill=self.lcd.bg, outline=self.lcd.fg)
        line1, line2 = self._generate_pvi_lines()
        draw.text(xy=(4, 6), text=line1, fill=self.lcd.fg, font=FONT[32])
        draw.text(xy=(4, 48), text=line2, fill=self.lcd.fg, font=FONT[32])
        self._auto_pilot_switch_2(draw)

    def _generate_pvi_lines(self) -> Sequence[str]:
        text1, text2 = '', ''
        line1_text = str(self.get_bios('PVI_LINE1_TEXT'))
        line2_text = str(self.get_bios('PVI_LINE2_TEXT'))
        if line1_text:
            l1_apostr1 = self.get_bios("PVI_LINE1_APOSTROPHE1")
            l1_apostr2 = self.get_bios("PVI_LINE1_APOSTROPHE2")
            text1 = f'{line1_text[-6:-3]}{l1_apostr1}{line1_text[-3:-1]}{l1_apostr2}{line1_text[-1]}'
        if line2_text:
            l2_apostr1 = self.get_bios("PVI_LINE2_APOSTROPHE1")
            l2_apostr2 = self.get_bios("PVI_LINE2_APOSTROPHE2")
            text2 = f'{line2_text[-6:-3]}{l2_apostr1}{line2_text[-3:-1]}{l2_apostr2}{line2_text[-1]}'
        line1 = f'{self.get_bios("PVI_LINE1_SIGN")}{text1} {self.get_bios("PVI_LINE1_POINT")}'
        line2 = f'{self.get_bios("PVI_LINE2_SIGN")}{text2} {self.get_bios("PVI_LINE2_POINT")}'
        return line1, line2


class A10C(Aircraft):
    def __init__(self, lcd_type: LcdInfo) -> None:
        """
        Create A-10C Warthog or A-10C II Tank Killer.

        :param lcd_type: LCD type
        """
        super().__init__(lcd_type)
        self.bios_data: Dict[str, BIOS_VALUE] = {
            'VHFAM_FREQ1': {'class': 'StringBuffer', 'args': {'address': 0x1190, 'max_length': 2}, 'value': str()},
            'VHFAM_FREQ2': {'class': 'IntegerBuffer', 'args': {'address': 0x118e, 'mask': 0xf0, 'shift_by': 0x4}, 'value': int()},
            'VHFAM_FREQ3': {'class': 'IntegerBuffer', 'args': {'address': 0x118e, 'mask': 0xf00, 'shift_by': 0x8}, 'value': int()},
            'VHFAM_FREQ4': {'class': 'StringBuffer', 'args': {'address': 0x1192, 'max_length': 2}, 'value': str()},
            'VHFFM_FREQ1': {'class': 'StringBuffer', 'args': {'address': 0x119a, 'max_length': 2}, 'value': str()},
            'VHFFM_FREQ2': {'class': 'IntegerBuffer', 'args': {'address': 0x119c, 'mask': 0xf, 'shift_by': 0x0}, 'value': int()},
            'VHFFM_FREQ3': {'class': 'IntegerBuffer', 'args': {'address': 0x119c, 'mask': 0xf0, 'shift_by': 0x4}, 'value': int()},
            'VHFFM_FREQ4': {'class': 'StringBuffer', 'args': {'address': 0x119e, 'max_length': 2}, 'value': str()},
            'UHF_100MHZ_SEL': {'class': 'StringBuffer', 'args': {'address': 0x1178, 'max_length': 1}, 'value': str()},
            'UHF_10MHZ_SEL': {'class': 'IntegerBuffer', 'args': {'address': 0x1170, 'mask': 0x3c00, 'shift_by': 0xa}, 'value': int()},
            'UHF_1MHZ_SEL': {'class': 'IntegerBuffer', 'args': {'address': 0x1178, 'mask': 0xf00, 'shift_by': 0x8}, 'value': int()},
            'UHF_POINT1MHZ_SEL': {'class': 'IntegerBuffer', 'args': {'address': 0x1178, 'mask': 0xf000, 'shift_by': 0xc}, 'value': int()},
            'UHF_POINT25_SEL': {'class': 'StringBuffer', 'args': {'address': 0x117a, 'max_length': 2}, 'value': str()}}

    def _generate_freq_values(self) -> Sequence[str]:
        vhfam = f'{self.get_bios("VHFAM_FREQ1")}{self.get_bios("VHFAM_FREQ2")}.' \
                f'{self.get_bios("VHFAM_FREQ3")}{self.get_bios("VHFAM_FREQ4")}'
        vhffm = f'{self.get_bios("VHFFM_FREQ1")}{self.get_bios("VHFFM_FREQ2")}.' \
                f'{self.get_bios("VHFFM_FREQ3")}{self.get_bios("VHFFM_FREQ4")}'
        uhf = f'{self.get_bios("UHF_100MHZ_SEL")}{self.get_bios("UHF_10MHZ_SEL")}{self.get_bios("UHF_1MHZ_SEL")}.' \
              f'{self.get_bios("UHF_POINT1MHZ_SEL")}{self.get_bios("UHF_POINT25_SEL")}'
        return uhf, vhfam, vhffm

    def draw_for_lcd_type_1(self, img: Image.Image) -> None:
        """Prepare image for A-10C Warthog or A-10C II Tank Killer for Mono LCD."""
        draw = ImageDraw.Draw(img)
        uhf, vhfam, vhffm = self._generate_freq_values()
        for i, line in enumerate(['      *** RADIOS ***', f'VHF AM: {vhfam} MHz',
                                  f'VHF FM: {vhffm} MHz', f'   UHF: {uhf} MHz']):
            offset = i * 10
            draw.text(xy=(0, offset), text=line, fill=self.lcd.fg, font=FONT[11])

    def draw_for_lcd_type_2(self, img: Image.Image) -> None:
        """Prepare image for A-10C Warthog or A-10C II Tank Killer for Color LCD."""
        draw = ImageDraw.Draw(img)
        uhf, vhfam, vhffm = self._generate_freq_values()
        for i, line in enumerate(['      *** RADIOS ***', f'VHF AM: {vhfam} MHz',
                                  f'VHF FM: {vhffm} MHz', f'   UHF: {uhf} MHz']):
            offset = i * 20
            draw.text(xy=(0, offset), text=line, fill=self.lcd.fg, font=FONT[22])


class A10C2(A10C):
    pass


class F14B(Aircraft):
    def __init__(self, lcd_type: LcdInfo) -> None:
        """
        Create F-14B Tomcat.

        :param lcd_type: LCD type
        """
        super().__init__(lcd_type)
        self.bios_data: Dict[str, BIOS_VALUE] = {
            'RIO_CAP_CLEAR': {'class': 'IntegerBuffer', 'args': {'address': 0x12c4, 'mask': 0x4000, 'shift_by': 0xe}, 'value': int()},
            'RIO_CAP_SW': {'class': 'IntegerBuffer', 'args': {'address': 0x12c4, 'mask': 0x2000, 'shift_by': 0xd}, 'value': int()},
            'RIO_CAP_NE': {'class': 'IntegerBuffer', 'args': {'address': 0x12c4, 'mask': 0x1000, 'shift_by': 0xc}, 'value': int()},
            'RIO_CAP_ENTER': {'class': 'IntegerBuffer', 'args': {'address': 0x12c4, 'mask': 0x8000, 'shift_by': 0xf}, 'value': int()}}

    def button_request(self, button: int, request: str = '\n') -> str:
        """
        Prepare F-14 Tomcat specific DCS-BIOS request for button pressed.

        For G13/G15/G510: 1-4
        For G19 9-15: LEFT = 9, RIGHT = 10, OK = 11, CANCEL = 12, UP = 13, DOWN = 14, MENU = 15
        If button is out of scope new line is return.
        :param button: possible values 1-4
        :param request: valid DCS-BIOS command as string
        :return: ready to send DCS-BIOS request
        """
        action = {1: 'RIO_CAP_CLEAR 1\nRIO_CAP_CLEAR 0\n',
                  2: 'RIO_CAP_SW 1\nRIO_CAP_SW 0\n',
                  3: 'RIO_CAP_NE 1\nRIO_CAP_NE 0\n',
                  4: 'RIO_CAP_ENTER 1\nRIO_CAP_ENTER 0\n',
                  9: 'RIO_CAP_CLEAR 1\nRIO_CAP_CLEAR 0\n',
                  10: 'RIO_CAP_SW 1\nRIO_CAP_SW 0\n',
                  14: 'RIO_CAP_NE 1\nRIO_CAP_NE 0\n',
                  13: 'RIO_CAP_ENTER 1\nRIO_CAP_ENTER 0\n'}
        return super().button_request(button, action.get(button, '\n'))

    def draw_for_lcd_type_1(self, img: Image.Image) -> None:
        """Prepare image for F-14B Tomcat for Mono LCD."""
        draw = ImageDraw.Draw(img)
        draw.text(xy=(2, 3), text='F-14B Tomcat', fill=self.lcd.fg, font=FONT[16])

    def draw_for_lcd_type_2(self, img: Image.Image) -> None:
        """Prepare image for F-14B Tomcat for Color LCD."""
        draw = ImageDraw.Draw(img)
        draw.text(xy=(2, 3), text='F-14B Tomcat', fill=self.lcd.fg, font=FONT[32])


class AV8BNA(Aircraft):
    def __init__(self, lcd_type: LcdInfo) -> None:
        """
        Create AV-8B Night Attack.

        :param lcd_type: LCD type
        """
        super().__init__(lcd_type)
        self.bios_data: Dict[str, BIOS_VALUE] = {
            'UFC_SCRATCHPAD': {'class': 'StringBuffer', 'args': {'address': 0x7984, 'max_length': 12}, 'value': str()},
            'UFC_COMM1_DISPLAY': {'class': 'StringBuffer', 'args': {'address': 0x7954, 'max_length': 2}, 'value': str()},
            'UFC_COMM2_DISPLAY': {'class': 'StringBuffer', 'args': {'address': 0x7956, 'max_length': 2}, 'value': str()},
            'AV8BNA_ODU_1_SELECT': {'class': 'StringBuffer', 'args': {'address': 0x7966, 'max_length': 1}, 'value': str()},
            'AV8BNA_ODU_1_Text': {'class': 'StringBuffer', 'args': {'address': 0x7968, 'max_length': 4}, 'value': str()},
            'AV8BNA_ODU_2_SELECT': {'class': 'StringBuffer', 'args': {'address': 0x796c, 'max_length': 1}, 'value': str()},
            'AV8BNA_ODU_2_Text': {'class': 'StringBuffer', 'args': {'address': 0x796e, 'max_length': 4}, 'value': str()},
            'AV8BNA_ODU_3_SELECT': {'class': 'StringBuffer', 'args': {'address': 0x7972, 'max_length': 1}, 'value': str()},
            'AV8BNA_ODU_3_Text': {'class': 'StringBuffer', 'args': {'address': 0x7974, 'max_length': 4}, 'value': str()},
            'AV8BNA_ODU_4_SELECT': {'class': 'StringBuffer', 'args': {'address': 0x7978, 'max_length': 1}, 'value': str()},
            'AV8BNA_ODU_4_Text': {'class': 'StringBuffer', 'args': {'address': 0x797a, 'max_length': 4}, 'value': str()},
            'AV8BNA_ODU_5_SELECT': {'class': 'StringBuffer', 'args': {'address': 0x797e, 'max_length': 1}, 'value': str()},
            'AV8BNA_ODU_5_Text': {'class': 'StringBuffer', 'args': {'address': 0x7980, 'max_length': 4}, 'value': str()}}

    def _draw_common_data(self, draw: ImageDraw, scale: int) -> ImageDraw:
        draw.text(xy=(50 * scale, 0), fill=self.lcd.fg, font=FONT[16 * scale], text=f'{self.get_bios("UFC_SCRATCHPAD")}')
        draw.line(xy=(50 * scale, 20 * scale, 160 * scale, 20 * scale), fill=self.lcd.fg, width=1)

        draw.rectangle(xy=(50 * scale, 29 * scale, 70 * scale, 42 * scale), fill=self.lcd.bg, outline=self.lcd.fg)
        draw.text(xy=(52 * scale, 29 * scale), text=self.get_bios('UFC_COMM1_DISPLAY'), fill=self.lcd.fg, font=FONT[16 * scale])

        draw.rectangle(xy=(139 * scale, 29 * scale, 159 * scale, 42 * scale), fill=self.lcd.bg, outline=self.lcd.fg)
        draw.text(xy=(140 * scale, 29 * scale), text=self.get_bios('UFC_COMM2_DISPLAY'), fill=self.lcd.fg, font=FONT[16 * scale])

        for i in range(1, 6):
            offset = (i - 1) * 8 * scale
            draw.text(xy=(0 * scale, offset), fill=self.lcd.fg, font=FONT[11 * scale],
                      text=f'{i}{self.get_bios(f"AV8BNA_ODU_{i}_SELECT")}{self.get_bios(f"AV8BNA_ODU_{i}_Text")}')
        return draw

    def draw_for_lcd_type_1(self, img: Image.Image) -> None:
        """Prepare image for AV-8B N/A for Mono LCD."""
        self._draw_common_data(draw=ImageDraw.Draw(img), scale=1)

    def draw_for_lcd_type_2(self, img: Image.Image) -> None:
        """Prepare image for AV-8B N/A for Color LCD."""
        self._draw_common_data(draw=ImageDraw.Draw(img), scale=2)

    def button_request(self, button: int, request: str = '\n') -> str:
        """
        Prepare AV-8B N/A specific DCS-BIOS request for button pressed.

        For G13/G15/G510: 1-4
        For G19 9-15: LEFT = 9, RIGHT = 10, OK = 11, CANCEL = 12, UP = 13, DOWN = 14, MENU = 15
        :param button: possible values 1-4
        :param request: valid DCS-BIOS command as string
        :return: ready to send DCS-BIOS request
        """
        action = {1: 'UFC_COM1_SEL -3200\n',
                  2: 'UFC_COM1_SEL 3200\n',
                  3: 'UFC_COM2_SEL -3200\n',
                  4: 'UFC_COM2_SEL 3200\n',
                  9: 'UFC_COM1_SEL -3200\n',
                  10: 'UFC_COM1_SEL 3200\n',
                  14: 'UFC_COM2_SEL -3200\n',
                  13: 'UFC_COM2_SEL 3200\n'}
        return super().button_request(button, action.get(button, '\n'))
