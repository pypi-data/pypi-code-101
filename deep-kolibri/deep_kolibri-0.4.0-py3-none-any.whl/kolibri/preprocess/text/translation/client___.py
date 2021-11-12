"""
HackerNews module.
"""
import logging
import time
import math, random
import asyncio, requests, re
from operator import itemgetter
from kolibri.preprocess.text.translation.constants import (
    LANGCODES, LANGUAGES, SPECIAL_CASES, GOOGLE_DEFAULT_SERVICE_URLS,
    DEFAULT_RAISE_EXCEPTION, DUMMY_DATA, TRANSLATE
)
import httpx
from httpx import Timeout

from kolibri.preprocess.text.translation import utils
from kolibri.preprocess.text.translation.models import Translated
from kolibri.preprocess.text.translation.apis import translate as translate2
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Translator:
    """ Get the top posts trending on HackerNews. """
    _ua = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 14_1_4) "
        "AppleWebKit/605.1.15 (KHTML, like Gecko) "
        "Mobile/16D57"
    )

    def __init__(self, timeout: Timeout = None,
                 http2=True):

        self.client = httpx.AsyncClient(http2=http2)

        self.client.headers.update({
            'User-Agent': self._ua,
        })

        if timeout is not None:
            self.client.timeout = 1000#timeout

        self.service_url = "translate.googleapis.com"

        self.service_url = random.choice(GOOGLE_DEFAULT_SERVICE_URLS)
        self.raise_exception = DEFAULT_RAISE_EXCEPTION
        self._session = requests.session()
        self._session.headers.update({"user-agent": self._ua})
        self.__class__._tkk = ""
        self._re_tkk = re.compile(r"tkk=\'(.+?)\'", re.DOTALL)


    def _calc_token(self, text):

        if (
                not self.__class__._tkk
                or int(self.__class__._tkk.split(".")[0]) < int(time.time() / 3600) - 18000
        ):
            logger.debug("generating new tkk")
            # just calling it to simulate human behaviour (as far as possible)
            self._session.get(
                "https://" + self.service_url+"/translate_a/l?client=t&alpha=true&hl=en&cb=callback"
            )

            r = self._session.get(
                "https://" + self.service_url+"/translate_a/element.js?cb=googleTranslateElementInit"

            )
            self.__class__._tkk = self._re_tkk.search(r.text)[1]

        def xor_rot(a, b):
            size_b = len(b)
            c = 0
            while c < size_b - 2:
                d = b[c + 2]
                d = ord(d[0]) - 87 if "a" <= d else int(d)
                d = (a % 0x100000000) >> d if "+" == b[c + 1] else a << d
                a = a + d & 4294967295 if "+" == b[c] else a ^ d
                c += 3
            return a

        a = []
        for i in text:
            val = ord(i)
            if val < 0x10000:
                a += [val]
            else:
                a += [
                    math.floor((val - 0x10000) / 0x400 + 0xD800),
                    math.floor((val - 0x10000) % 0x400 + 0xDC00),
                ]
        b = self.__class__._tkk if self.__class__._tkk != "0" else ""
        d = b.split(".")
        b = int(d[0]) if len(d) > 1 else 0
        e = []
        g = 0
        size = len(text)
        while g < size:
            l = a[g]
            if l < 128:
                e.append(l)
            else:
                if l < 2048:
                    e.append(l >> 6 | 192)
                else:
                    if (
                            (l & 64512) == 55296
                            and g + 1 < size
                            and a[g + 1] & 64512 == 56320
                    ):
                        g += 1
                        l = 65536 + ((l & 1023) << 10) + (a[g] & 1023)
                        e.append(l >> 18 | 240)
                        e.append(l >> 12 & 63 | 128)
                    else:
                        e.append(l >> 12 | 224)
                    e.append(l >> 6 & 63 | 128)
                e.append(l & 63 | 128)
            g += 1
        a = b
        for i, value in enumerate(e):
            a += value
            a = xor_rot(a, "+-a^+6")
        a = xor_rot(a, "+-3^+b+-f")
        a ^= int(d[1]) if len(d) > 1 else 0
        if a < 0:
            a = (a & 2147483647) + 2147483648
        a %= 1000000
        return "{}.{}".format(a, a ^ b)

    @staticmethod
    async def fetch(client, url, params):
        """
        Return async response object for HackerNews item.
        :param item_id: json id for HackerNews item
        :param client: httpx.AsyncClient method
        :return: httpx.AsyncClient response object
        """

        return await client.get(url,
                             params=params)

    async def _translate(self, texts, dest, src, override):
        """
        Return a list of responses from the given list of HackerNews item id's.
        """
        _list = [
            (TRANSLATE.format(host=self.service_url),
            self._prepare_request_params(text, dest, src, override)) for text in texts
        ]
        logger.debug(_list)
        async with httpx.AsyncClient() as client:
            logger.debug(client)
            self.responses = await asyncio.gather(
                *[self.fetch(client, p[0], p[1]) for p in _list])

    def _prepare_request_params(self, text, dest, src, override):
        self.service_url = random.choice(GOOGLE_DEFAULT_SERVICE_URLS)
        token = self._calc_token(text)
        params = utils.build_params(query=text, src=src, dest=dest,
                                    token=token, override=override)

        return params

    def _parse_extra_data(self, data):
        response_parts_name_mapping = {
            0: 'translation',
            1: 'all-translations',
            2: 'original-language',
            5: 'possible-translations',
            6: 'confidence',
            7: 'possible-mistakes',
            8: 'language',
            11: 'synonyms',
            12: 'definitions',
            13: 'examples',
            14: 'see-also',
        }

        extra = {}

        for index, category in response_parts_name_mapping.items():
            extra[category] = data[index] if (
                    index < len(data) and data[index]) else None

        return extra

    def translate(self, texts, dest, src = 'auto',  **kwargs):
        """
        A helper class to create async coroutines.
        :param coro: a valid coroutine
        :return: result set from the async function
        """
        dest = dest.lower().split('_', 1)[0]
        src = src.lower().split('_', 1)[0]

        if src != 'auto' and src not in LANGUAGES:
            if src in SPECIAL_CASES:
                src = SPECIAL_CASES[src]
            elif src in LANGCODES:
                src = LANGCODES[src]
            else:
                raise ValueError('invalid source language')

        if dest not in LANGUAGES:
            if dest in SPECIAL_CASES:
                dest = SPECIAL_CASES[dest]
            elif dest in LANGCODES:
                dest = LANGCODES[dest]
            else:
                raise ValueError('invalid destination language')

        coro = self._translate(texts, dest, src, kwargs)

        logger.debug(coro)
        asyncio.run(coro)

        self.extract(texts, dest)

        return self.results

    def extract(self, texts, dest):
        """
        Extract the response JSON and append to a list
        """
        self.results=[]
        for i, r in enumerate(self.responses):
            if r.status_code == 200:
                data = utils.format_json(r.text)

                # this code will be updated when the format is changed.
                translated = ''.join([d[0] if d[0] else '' for d in data[0]])

                extra_data = self._parse_extra_data(data)

                # actual source language that will be recognized by Google Translator when the
                # src passed is equal to auto.
                src=''
                try:
                    src = data[2]
                except Exception:  # pragma: nocover
                    pass

                # put final values into a new Translated object
                result = Translated(src=src,
                                    text=translated,
                                    origin=texts[i],
                                    extra_data=extra_data,
                                    response=r)
            else:

                result=translate2(text=texts[i], dest=dest, src='auto')
            self.results.append(result)


