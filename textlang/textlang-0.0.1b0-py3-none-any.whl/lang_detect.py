from dataclasses import dataclass
import pycld2 as cld2
import numpy as np


@dataclass
class LangDetect:
    method: str

    def __init__(self, method="vote"):
        self.method = method

    def __call__(self, sentence):
        if self.method == "vote":
            return self.vote([sentence])
        else:
            return self.detect(sentence)

    @staticmethod
    def detect(first_line):
        try:
            isReliable, textBytesFound, details = cld2.detect(
                first_line
            )
            return details[0][0]
        except:
            return "Unknown"

    @staticmethod
    def vote(lines):
        results = [LangDetect.detect(line) for line in lines]
        results = [r for r in results if not r in ["Unknown"]]
        lang, counts = np.unique(results, return_counts=True)
        try:
            idx = np.argmax(counts)
        except ValueError:
            return "Unknown", 1.0
        lang, confidence = lang[idx], counts[idx]/sum(counts)
        return lang, confidence
