"""A conversion module for googletrans"""
import json
import re

def format_querystringlang():
    querystring = {
        "client":"te",
    }
    return querystring

def format_querystring(token, text, src='auto', dest='en'):
    params = {
        'client': 'webapp',
        'sl': src,
        'tl': dest,
        'hl': dest,
        'dt': ['at', 'bd', 'ex', 'ld', 'md', 'qca', 'rw', 'rm', 'ss', 't'],
        'ie': 'UTF-8',
        'oe': 'UTF-8',
        'otf': 1,
        'ssel': 0,
        'tsel': 0,
        'tk': token,
        'q': text,
    }

    return params

def format_param(rpcids):
    params = {
        'rpcids': rpcids,
        'bl': 'boq_translate-webserver_20201207.13_p0', 
        'soc-app': 1, 
        'soc-platform': 1, 
        'soc-device': 1, 
        'rt': 'c'
    }
    return params

def format_data(rpcids, text, src, dest):

    param = json.dumps([[str(text).strip(), src, dest, True], [1]])
    rpc = json.dumps([[[rpcids, param, None, "generic"]]])
    return {'f.req': rpc}


def format_translation(data):

    try:
        if len(data) > 1 and len(data[1]) > 0 and len(data[1][0]) > 0 and len(data[1][0][0]) > 5:
            translated = [x[0] for x in data[1][0][0][5] if x is not None]
            #inserting space between sentences and fixing trailing spaces
            translated=' '.join(['\n' if x=="" else x for x in translated])
            translated='\n'.join([t.strip() for t in translated.split('\n')])


    except:
        translated = None

    return translated

def legacy_format_json(original):
    # save state
    states = []
    text = original

    # save position for double-quoted texts
    for i, pos in enumerate(re.finditer('"', text)):
        # pos.start() is a double-quote
        p = pos.start() + 1
        if i % 2 == 0:
            nxt = text.find('"', p)
            states.append((p, text[p:nxt]))

    # replace all wiered characters in text
    while text.find(',,') > -1:
        text = text.replace(',,', ',null,')
    while text.find('[,') > -1:
        text = text.replace('[,', '[null,')

    # recover state
    for i, pos in enumerate(re.finditer('"', text)):
        p = pos.start() + 1
        if i % 2 == 0:
            j = int(i / 2)
            nxt = text.find('"', p)
            # replacing a portion of a string
            # use slicing to extract those parts of the original string to be kept
            text = text[:p] + states[j][1] + text[nxt:]

    converted = json.loads(text)
    return converted


def get_items(dict_object):
    for key in dict_object:
        yield key, dict_object[key]


def format_json(original):
    try:
        converted = json.loads(original)
    except ValueError:
        converted = legacy_format_json(original)

    return converted
