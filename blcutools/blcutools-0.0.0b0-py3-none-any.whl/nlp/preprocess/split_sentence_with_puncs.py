# Copyright 2021 BLCU-Research.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ==============================================================================

import re
import unicodedata
from typing import List


class SplitSentenceWithPuncs:
    """Split text to Punctuation Clauses
    (1) The term of punctuation mark used in this article refers specifically to commas,
    semicolons, periods, question marks and exclamation marks. The word sequences separated
    by these punctuation marks are called punctuation clauses. In the tagged corpus,
    each punctuation clause occupies one line.
    (2) Whether or not dashes, deletions and colons separate punctuation clauses depends on
    the specific situation.
    (3) Quotation marks( single quotation marks, double quotation marks, parentheses )
    are not cutting punctuation clauses.
    (4) If the left side of the left parenthesis is a punctuation mark, the left and right
    parenthesis together with the enclosed components are regarded as a supplementary explanatory
    clause( see below for the concept of supplementary explanatory clauses ).
    If the left side of the left parenthesis is not a punctuation mark, the left and right parenthesis,
    together with the enclosed component, are regarded as a component within the punctuation clause,
    and the punctuation marks within the parenthesis are not regarded as a punctuation clause separators.
    (5) The right quotation mark / right quotation mark string ( quotation mark nesting can form
    the phenomenon of quotation mark string ) , if the left neighbor is not a punctuation mark,
    the punctuation marks inside quotation marks will not be used as punctuation clause separators,
    and the contents enclosed in quotation marks will be regarded as the components inside a
    punctuation clause; Otherwise, the contents closed by the quotation marks are regarded as
    a quotation, and punctuation marks in the quotation marks are regarded as punctuation clause
    separators ( see below ). However, sometimes it is due to omission that the left neighbor of
    aright quotation marks / right quotation marks string is not a punctuation mark and the
    punctuation mark should be filled in.
    """

    _split_puncs = ['。', '，', '！', '？', '；'] + ['.', ',', '!', '?', ';']
    _spec_puncs = ['。', '！', '？'] + ['.', '!', '?']
    _paired_puncs = [
        ['“', '”'], ['‘', '’'], ['「', '」'],
        ['（', '）'], ['(', ')'], ['《', '》'],
        ['{', '}'], ['[', ']'], ['『', '』']
    ]
    _right_quotation_marks = ['”', '’', '』', '」']

    @classmethod
    def _find_puncs_pos(cls, text):
        # Find the position of puncs, and not include the puncs like 1000,000. (2021.11.4 SmileTM)
        puncs = ''.join(cls._split_puncs)
        # pat = re.compile('[' + puncs + ']')
        pat = re.compile(f"(?<=\D)[{puncs}]|(?<=\d)[{puncs}](?=[^\d]+)")

        return [m.start() for m in pat.finditer(text)]

    @classmethod
    def _is_paired_puncs(cls, ch, left=True):
        for idx, pair in enumerate(cls._paired_puncs):
            if pair[0 if left else 1] == ch:
                return idx
        return -1

    @classmethod
    def _find_matched_puncs(cls, text):
        matched = []
        stack = []
        try:
            for pos, ch in enumerate(text):
                idx = cls._is_paired_puncs(ch)
                if idx >= 0:
                    stack.append((idx, pos))
                else:
                    idx = cls._is_paired_puncs(ch, False)
                    if idx >= 0:
                        if not stack:
                            raise ValueError('paired punctuations mismatching in text: \"{}\"'.format(text))
                        if idx == stack[len(stack) - 1][0]:
                            matched.append((stack[len(stack) - 1][1], pos))
                            stack.pop()
                        else:
                            raise ValueError('paired punctuations mismatching in text: \"{}\"'.format(text))
            if stack:
                raise ValueError('paired punctuations mismatching in text: \"{}\"'.format(text))
        except ValueError:
            pass

        return matched

    @classmethod
    def split(cls, text: str, merge_puncs_seq=True) -> List:
        """Split text with specified punctuations mark.
        :param text: str type of text to split
        :param merge_puncs_seq: optional. default True. merge punctuations sequence to previous one.
        :return: list of Punctuation Clauses
        """

        def _is_whitespace(char):
            """Checks whether `chars` is a whitespace character."""
            # \t, \n, and \r are technically control characters but we treat them
            # as whitespace since they are generally considered as such.
            if char == " " or char == "\t" or char == "\n" or char == "\r":
                return True
            cat = unicodedata.category(char)
            if cat == "Zs":
                return True
            return False

        def _is_punctuation(char):
            """Checks whether `chars` is a punctuation character."""
            cp = ord(char)
            # We treat all non-letter/number ASCII as punctuation.
            # Characters such as "^", "$", and "`" are not in the Unicode
            # Punctuation class but we treat them as punctuation anyways, for
            # consistency.
            if ((33 <= cp <= 47) or (58 <= cp <= 64) or
                (91 <= cp <= 96) or (123 <= cp <= 126)):
                return True
            cat = unicodedata.category(char)
            if cat.startswith("P"):
                return True
            return False

        def _in_span(pos, spans):
            for span in spans:
                if span[0] < pos < span[1]:
                    return True
            return False

        def _is_outermost_span(span, spans):
            for _span in spans:
                if span[0] > _span[0] and span[1] < _span[1]:
                    return False
            return True

        puncs_pos = cls._find_puncs_pos(text)
        matched_puncs = cls._find_matched_puncs(text)
        if matched_puncs:
            matched_puncs = [span for span in matched_puncs if _is_outermost_span(span, matched_puncs)]
            puncs_pos = [pos for pos in puncs_pos if not _in_span(pos, matched_puncs)]
            for span in matched_puncs:
                pos = span[1] - 1
                for pos in range(span[1] - 1, span[0], -1):
                    if text[pos] not in cls._right_quotation_marks:
                        break
                if (pos > span[0] + 1) and text[pos] in cls._spec_puncs:
                    if span[1] + 1 not in puncs_pos:
                        puncs_pos.append(span[1])
            puncs_pos = sorted(set(puncs_pos))

        puncs_pos = [pos for pos in puncs_pos if pos + 1 not in puncs_pos]  # merge single punctuation char
        puncs_pos.append(len(text))
        splits = []
        start = 0
        for pos in puncs_pos:
            if pos == start:
                continue
            pc = text[start:pos + 1]
            if merge_puncs_seq:
                if [ch for ch in pc if not (_is_whitespace(ch) or _is_punctuation(ch))]:
                    splits.append(pc)
                else:
                    # merge punctuations sequences
                    if splits:
                        splits[-1] = splits[-1] + pc
                    else:
                        splits.append(pc)
            else:
                splits.append(pc)
            start = pos + 1
        return splits


if __name__ == '__main__':
    from tqdm import tqdm

    sp = SplitSentenceWithPuncs()
    text = '太保鼎是中华人民共和国国家一级文物，64件禁止出国(境)展览的文物之一。铸造于西周初期。现藏天津博物馆。太保鼎相传在清道光或咸丰年间出土于山东寿张县梁山，同时出土的还有青铜尊、甗等。这些青铜器器型庄严厚重，纹饰华丽繁缛，是商周青铜器的典型代表，合称“梁山七器”。太保鼎先后由李宗岱、丁麐年、徐世昌等人收藏；徐世昌曾作《得鼎歌》对其倍加赞颂，并收入《水竹邨人集》中。1958年，徐世昌之孙媳张秉慧将太保鼎捐献国家，收藏于天津博物馆。太保鼎为方形鼎，通高57.6厘米，口径长35.8厘米，宽22.8厘米，重26公斤；四柱足，有二直耳，耳上铸有攀附状垂角双兽，器腹饰有饕餮纹和蕉叶纹，四角饰扉棱。太保鼎的四柱足装饰有扉棱，柱足中部装饰有圆盘，这在商周青铜器中独一无二。腹内有“大（太）保铸”三字，故而得名。此太保即辅佐周成王之召公奭。今天真的很舒服。。。。。。，，，...,,,啊'
    for _ in tqdm(range(1000000)):
        out = SplitSentenceWithPuncs.split(text)
