""" Text cleaning

- [x] HTML emojies to -> unicode emojies/emoticons
- [x] U+XX html codes -> unicode chars
- [ ] unicode to ascii
- [ ] remove diacritics
"""
import numpy as np
import pandas as pd
from proai.constants import DATA_DIR
from proai.make import make_df


def build_html_translation_dict(html_numbers=None, html_names=None, html_emojies=None):
    if isinstance(html_numbers, pd.Series):
        html_numbers = html_numbers.to_dict()
    if isinstance(html_names, pd.Series):
        html_names = html_names.to_dict()

    html_dict = {f'&#{i};': chr(i) for i in range(256)}
    html_dict.update({f'&#{i:03d};': chr(i) for i in range(256)})

    if html_emojies is None or not len(html_emojies):
        html_emojies = {}
    elif isinstance(html_emojies, pd.Series):
        html_emojies = html_emojies.str.replace('U+', '', regex=False).str.split()
        html_emojies = html_emojies.to_dict()
    elif isinstance(html_emojies, dict):
        html_emojies = dict([
            (k, str(v).replace('U+', '')) for (k, v) in html_emojies.items() if k and v])

    html_codes = []
    for codes in html_emojies:

        html_code = ''
        for c in codes:
            try:
                i = int(c, base=16)
                html_code + f'&#{i};'
            except ValueError:
                pass
        html_codes.append(html_code)
    html_dict.update(zip(html_codes, html_emojies.values()))
    html_dict.update(html_numbers)
    html_dict.update(html_names)
    for k in ('', None, np.nan):
        if k in html_dict:
            del html_dict[k]
    return html_dict


DF_EMOJIES = make_df(DATA_DIR / 'emojies.csv').dropna()
DF_ASCII = make_df(DATA_DIR / 'ascii_extended.csv').dropna()
HTML_NUMBER_SYMBOLS = pd.Series(DF_ASCII['symbol'].values,
                                index=DF_ASCII['html_number'].values)
HTML_NAME_SYMBOLS = pd.Series(DF_ASCII['symbol'].values,
                              index=DF_ASCII['html_name'].values)
HTML_EMOJI_SYMBOLS = pd.Series(DF_EMOJIES['cldr_short_name'].values,
                               index=DF_EMOJIES['browser'])
HTML_DICT = build_html_translation_dict(
    html_numbers=HTML_NUMBER_SYMBOLS,
    html_names=HTML_NAME_SYMBOLS,
    html_emojies=HTML_EMOJI_SYMBOLS
)  # compose_html_dict()
# HTML_BYTES_DICT = dict(
#     [(h.encode(), c.encode()) for (h, c) in HTML_DICT.items()]
# )
