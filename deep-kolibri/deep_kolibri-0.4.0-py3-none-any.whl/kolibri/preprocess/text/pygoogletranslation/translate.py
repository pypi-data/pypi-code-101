
import os
import json, re
import requests
import time
from kolibri.preprocess.text.pygoogletranslation import utils, urls
from kolibri.preprocess.text.pygoogletranslation.constants import (
    LANGCODES, LANGUAGES, RPCIDS
)
from kolibri.preprocess.text.pygoogletranslation.models import Translated, Detected
from urllib.parse import quote, urlencode

class Translator:

    def __init__(self, host=urls.TRANSLATE, proxies=None, timeout=None,
                retry=3, sleep=5, retry_messgae=False):
        self.host = host if 'http' in host else 'https://' + host
        self.rpcids = RPCIDS
        self.transurl = urls.TRANSLATEURL
        if proxies is not None:
            self.proxies = proxies
        else:
            self.proxies = None
        
        if timeout is not None:
            self.timeout = timeout

        self.retry = retry
        self.retry_messgae = retry_messgae
        self.sleep = sleep
        self.nb_requests=0
    def translate(self, text, src='auto', dest='en'):

        if src != 'auto':
            if src.lower() in LANGCODES:
                src = LANGCODES[src]
            elif src.lower() in LANGUAGES:
                src = src
            else:
                raise ValueError('invalid source language')

        if dest != 'en':
            if dest.lower() in LANGCODES:
                dest = LANGCODES[src.lower()]
            elif dest.lower() in LANGUAGES:
                dest = dest
            else:
                raise ValueError('invalid destination language')
        to_translate=text
        if not isinstance(to_translate, list):
            to_translate=[to_translate]
        data = self._translate(to_translate, src=src, dest=dest)


        resutlts= self.extract_translation(data, dest)
        if not isinstance(text, list):
            if resutlts:
                return resutlts[0]
            else:
                print(text)
                return None
        return resutlts

    def extract_translation(self, translation_data, target_lang):
        result_list = []
        for _data in translation_data:
            source = _data[1][4][0]
            try:
                translated = utils.format_translation(_data)
            except IndexError:
                translated = [source]
            src='und'
            if len(_data)>2:
                src = _data[2]
            dest = target_lang
            # put final values into a new Translated object
            result = Translated(src=src, dest=dest, origin=source,
                                    text=translated)
            result_list.append(result)
        return result_list
    def detect(self, text, **kwargs):
        """Detect language of the input text
        """
        if isinstance(text, list):
            result = []
            for item in text:
                lang = self.detect(item)
                result.append(lang)
            return result

        data = self._translate(text, 'auto', 'en')

        # actual source language that will be recognized by Google Translator when the
        # src passed is equal to auto.
        src = ''
        confidence = 0.0
        try:
            src = data[0][0][2][3][5][0][0][3]
            # confidence = data[8][-2][0]
        except Exception:  # pragma: nocover
            pass
        result = Detected(lang=src, confidence=confidence)

        return result

    def parse(self, data: str) -> str:
        matches = re.findall(r"\n\d+\n", data)
        return data[data.index(matches[0]) + len(matches[0]):data.index(matches[1])]

    def run_request(self, text, src, dest):
        try:
            response = requests.post(
                url="https://translate.google.com/_/TranslateWebserverUi/data/batchexecute?" +
                    urlencode({
                        "rpcids": "MkEWBc",
                        "rt": 'c'
                    }),
                headers={
                    "content-type": "application/x-www-form-urlencoded;charset=UTF-8"
                },
                data=urlencode({
                    "f.req": json.dumps(
                        [[[
                            "MkEWBc",
                            str([
                                [
                                    text,
                                    src,
                                    dest,
                                    True
                                ],
                                [None]
                            ]),
                            None,
                            "generic"
                        ]]]
                    )
                }, quote_via=quote)
            )
            return response
        except:
            return None

    def _translate(self, texts, src, dest):
        """ Generate Token for each Translation and post requset to
        google web api translation and return an response

        If the status code is 200 the request is considered as an success
        else other status code are consider as translation failure.

        """

        translated_list = []
        for text in texts:
            response=self.run_request(text, src, dest)
            if response.status_code == 200:
                pass
            elif response.status_code == 429:
                _format_data = self.retry_request(text, src, dest)
            else:
                raise Exception('Unexpected status code {} from {}'.format(response.status_code, self.transurl))

            translation_data = json.loads(self.parse(response.text))
            if translation_data[0][2] is not None:
                translated_list.append(json.loads(translation_data[0][2]))
        return translated_list

    def retry_request(self, text, src, dest):
        """ 
        For bulk translation some times translation might failed
        beacuse of too many attempts. for such a case before hitting
        translation api wait for some time and retrying again
        """
        retry = self.retry
        sleep = self.sleep
        response = self.run_request(text, src, dest)
        for i in range(0, retry):
            if response.status_code == 200:
                return response
            elif response.status_code == 429:
                if self.retry_messgae:
                    print('retrying translation after {}s'.format(sleep))
                time.sleep(sleep)
                sleep = i * sleep
            else:
                raise Exception('Unexpected status code {} from {}'.format(response.status_code, self.transurl))

        raise Exception('Unexpected status code {} from {} after retried {} loop with {}s delay'.format(response.status_code, self.transurl, retry, self.sleep))
