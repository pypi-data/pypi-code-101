"""
All functions working directly on git blob objects
"""

import logging
import sys
from typing import Any, Dict, \
    Optional

import git
import lizard
import magic

from cocluremig.analyzer.commit.util import AVERAGE_NEUTRAL, AverageElement


def get_code_metrics_lizard(sha: git.objects.Blob) -> Dict[str, Any]:
    """
    applies lizard analyzer (http://lizard.ws) onto blob

    @param sha: the blob
    @return: lizard results
    """
    text = get_text_representation(sha)
    if text:
        return lizard.analyze_file.analyze_source_code(sha.path, text).__dict__
    return {}


def get_lizard_metrics_avarageable(sha: git.objects.Blob) -> Dict[str, AverageElement]:
    """
    applies lizard onto the blob and comutes average (mean) values of the results

    @param sha: the blob
    @return: average results per value
    """
    plain_lizard = get_code_metrics_lizard(sha)
    # {'nloc': 9, 'function_list': [<lizard.FunctionInfo object at 0x10bf7af10>],
    # 'filename': '../cpputest/tests/AllTests.cpp'}
    res = {}
    if not plain_lizard:
        return res
    res['nloc_file'] = AverageElement(plain_lizard['nloc'])
    if plain_lizard['function_list']:
        for function in plain_lizard['function_list']:
            function = function.__dict__
            # {'cyclomatic_complexity': 1, 'token_count': 22,
            # 'name': 'main', 'parameter_count': 2, 'nloc': 3,
            # 'long_name': 'main( int ac , const char ** av )',
            # 'start_line': 30}
            for key in ['cyclomatic_complexity',
                        'token_count', 'top_nesting_level',
                        'fan_in', 'fan_out', 'nloc']:
                res[key] = res.get(key, AVERAGE_NEUTRAL) \
                           + AverageElement(function[key])
            res['parameter_count'] = \
                res.get('parameter_count', AVERAGE_NEUTRAL) \
                + AverageElement(len('full_parameters'))
        res['nloc_function'] = res.pop('nloc')
    return res


def get_file_extension(sha: git.objects.Blob) -> str:
    """
    get file extension for blob in tree

    @param sha: the blob
    @return: a file extension
    """
    return str(sha.path).split("/")[-1].split(".")[-1]


def get_lines_of_text(sha: git.objects.Blob) -> Optional[int]:
    """
    Computes lines of text from blob
    Returns None if blob is not decodeable as text

    @param sha: the blob
    @return: the lines of text
    """
    text = get_text_representation(sha)
    if text is not None:
        return text.count("\n") + 1
    return None


def get_object_size(sha: git.objects.Blob) -> Optional[int]:
    """
    Gets blob size

    @param sha: the blob
    @return: the object size
    """
    return sys.getsizeof(sha.data_stream.read())


def _get_mixed_size_per_extension(sha: git.objects.Blob) -> Dict[str, AverageElement]:
    ext = get_file_extension(sha)
    size = get_lines_of_text(sha)
    if not size:
        size = get_object_size(sha)
    return {ext: AverageElement(size)}


def get_text_representation(sha: git.objects.Blob) -> Optional[str]:
    """
    decodes the blob into text
    returns None if object is not decodable
    decoding failures are printed with logging.error
    decoding problems (broken encoding) are printed with logging.warn and return text anyway

    @param sha: the object sha
    @return: the text
    """
    enc = _get_encoding(sha)
    try:
        # only decode non-binaries e.g."binary", "application/tarbinary"
        if enc.find("binary") < 0:
            return str(sha.data_stream.read().decode(enc))
    except LookupError as error:
        logging.error("Unable to decode Object")
        logging.error((error, sha.path, sha.hexsha))
        if enc in __ENCODING_REPLACEMENTS.keys():
            return str(sha.data_stream.read()
                       .decode(__ENCODING_REPLACEMENTS[enc],
                               errors="replace"))
        raise error
    except UnicodeDecodeError as error:
        logging.warning("Malformed Unicode BLObject")
        logging.warning((error, sha.path, sha.hexsha))
        return str(sha.data_stream.read().decode(enc, errors="replace"))
    return None


def _get_encoding(sha: git.objects.Blob) -> str:
    magician = magic.Magic(mime_encoding=True)
    return magician.from_buffer(sha.data_stream.read())


__ENCODING_REPLACEMENTS = {'unknown-8bit': 'utf-8'}
