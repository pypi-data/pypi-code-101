from .segments import change_vowels, disattach_letters
from .phoneme import phonetic_change
from .yamin import yamin_jungum

from multiprocessing import Pool, cpu_count
from tqdm import tqdm

import re
import random
from functools import partial


def split_sentence(text):
    return re.split('(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)


class NoiseGenerator(object):
    def __init__(self, num_cores=None):
        self.rng = random.Random()
        self.pooler = Pool(processes=num_cores if num_cores else cpu_count())
        self.functions = {
            'disattach-letters': disattach_letters,
            'change-vowels': change_vowels,
            'palatalization': partial(phonetic_change, func='palatalization'),
            'linking': partial(phonetic_change, func='linking'),
            'liquidization': partial(phonetic_change, func='liquidization'),
            'nasalization': partial(phonetic_change, func='nasalization'),
            'assimilation': partial(phonetic_change, func='assimilation'),
            'yamin-jungum': yamin_jungum,
        }

        self.delis = {
            'total': ('', ''),
            'sentence': (split_sentence,' '),
            'newline': (lambda s: s.split('\n'),'\n')
        }

    def generate(self, text, methods='disattach-letters', prob=1., delimeter='newline') -> str:
        assert delimeter in self.delis, 'Not Defined Delimeter!'
        if isinstance(methods, str):
            methods = methods.split(',')
            if 'all' in methods:
                methods = list(self.functions.keys())

        candiates = [self.functions[f] for f in methods if self.functions]
        if not candiates:
            raise KeyError(f"There are no funtions available(Functions:{','.join(list(self.functions.keys()))})")

        def _generate(t):
            return self.rng.choice(candiates)(t, prob=prob)

        text = self.delis[delimeter][0](text)
        text = self.run_multiprocessing(_generate, text)
        return self.delis[delimeter][1].join(text)

    def run_multiprocessing(self, func, argument_list):
        return [r for r in tqdm(self.pooler.imap(
            func=func, iterable=argument_list), total=len(argument_list))]

