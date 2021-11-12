import time
import requests
from urllib.parse import quote, urlencode
import json
from kolibri.preprocess.text.pygoogletranslation.constants import LANGUAGES
import re


class LanguageException(Exception):
    def __init__(self, message: str = ''):
        super().__init__(message)


def parse(data: str) -> str:
    matches = re.findall(r"\n\d+\n", data)
    return data[data.index(matches[0]) + len(matches[0]):data.index(matches[1])]


class Translate:
    source: str
    translated: list
    src: str
    dest: str

    @staticmethod
    def translate(text: str, source_lang: str, target_lang: str):
        if target_lang not in LANGUAGES:
            raise LanguageException("please specify target language")

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
                                source_lang,
                                target_lang,
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

        translation_data = json.loads(parse(response.text))
        translation_data = json.loads(translation_data[0][2])

        output = Translate()
        output.source = translation_data[1][4][0]
        try:
            output.translated = translation_data[1][0][0][5][0][1]
        except IndexError:
            output.translated = [output.source]

        output.src = translation_data[2] if source_lang is LANGUAGES else source_lang
        output.dest = target_lang
        return output

    def __str__(self):
        return str(self.translated)


txt="""\n\n\n\n\n\nCher client,\n\nNous avons bien reçu votre inscription et nous vous remercions pour votre confiance.\n\nÀ présent, nous nous chargeons de tout, y compris de la résiliation de votre contrat chez votre fournisseur actuel.\n\nVous recevrez un e-mail de notre équipe inscription endéans les 5 jours ouvrés. Attention, pensez à vérifier dans votre dossier « Courrier indésirable »/ « Spam ».\n\nNous sommes à votre écoute\nNos collaborateurs se tiennent à votre disposition pour répondre à toutes vos questions. Si vous n’avez pas encore de numéro de client, veuillez garder votre numéro d’inscription 172902 à portée de main.\n
"""
s=time.time()

t = Translate.translate(txt, 'auto', 'en')

print(time.time()-s)

print(t)