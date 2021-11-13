from fuzzywuzzy import fuzz
from datetime import datetime


def word_match_score(
    a,
    b
):
    score = fuzz.ratio(a, b)
    diff_len = abs(len(a)-len(b)) + 1
    diff_len = 1 if diff_len == 0 else diff_len
    return score//diff_len


def string_match(
    source=None,
    sample=None,
    threshold=99
):
    source_split = source.split()
    sample_split = sample.split()
    score = sum(
        word_match_score(a, b) for a, b in zip(source_split, sample_split)
    )
    score = score//max(len(source_split), len(sample_split))
    verified = (score >= threshold)
    return verified, score, threshold


def string_to_date(
    date_string
):
    date_time_obj = datetime.strptime(date_string, '%d.%m.%Y').date()

    return date_time_obj


if __name__ == "__main__":

    date_string = '14.08.1992'
    print(
        string_to_date(
            date_string
        )
    )
