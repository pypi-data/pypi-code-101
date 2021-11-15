#!/usr/bin/env python
# -*- coding: utf-8 -*-

import html as py_html
import json


def tag(name, content='', attrs=None, escape=False, close=True, upper=False):
    """
    General function for generating a tag.
    
    :param name: str, tag name, e.g., h1, a, ... .
    :param content: str, tag content.
    :param attrs: dict, tag attributes, e.g., class, id, ... .
    :param escape: bool, escape special characters (<, >, and &) in tag content.
    :param close: bool, create tag with the corresponding closing tag.
    :param upper: bool, using upper case tag name instead of lower case tag name.
    :return: str, content string was wrapped with the corresponding tag and all attrs.
    """
    
    name = name.upper() if upper else name
    content = py_html.escape(content) if escape else content
    attrs = attrs if attrs and isinstance(attrs, dict) else {}
    attrs = ' '.join([f'{k}="{v}"' for k, v in attrs.items()])
    attrs = f' {attrs}' if attrs else ''
    opening = f'<{name}{attrs}>'
    closing = f'</{name}>' if close else ''
    return f'{opening}{content}{closing}'


def join(items):
    if isinstance(items, str):
        return items
    elif isinstance(items, dict):
        return json.dumps(items)
    elif isinstance(items, (list, tuple)):
        return '\n    '.join([str(x) for x in items])
    else:
        raise TypeError(f'Expect str, dict, list or tuple for function join(), but {type(items)} found.')


_HTML = """<!DOCTYPE html>
<html lang="{language}">
<head>
    {meta}
    {styles}
    {links}
    <title>{title}</title>
</head>
<body>
    {content}
    {scripts}
</body>
</html>
"""
_BS5 = """<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    {meta}
    {styles}
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css" rel="stylesheet"
          integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC" crossorigin="anonymous">
    {links}
    <title>{title}</title>
  </head>
  <body>
    {content}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-MrcW6ZMFYlzcLA8Nl+NtUVF0sA7MsXsP1UyJoMp4YLEuNSfAP+JcXn/tWtIaxVXM" crossorigin="anonymous">
    </script>
    {scripts}
  </body>
</html>
"""
TEMPLATES = {'': _HTML, 'bs5': _BS5, 'BS5': _BS5}


def html(content='', title='Title', language='en', meta=None, styles='', links=None, scripts=None, template=''):
    template = TEMPLATES.get(template, _HTML)
    meta, styles, links, scripts = [join(x) if x else '' for x in (meta, styles, links, scripts)]
    styles = tag('style', styles) if styles else ''
    s = template.format(language=language, meta=meta, styles=styles, links=links, title=title, content=content,
                        scripts=scripts)
    return s


def a(content='', attrs=None, escape=False, upper=False):
    return tag('a', content=content, attrs=attrs, escape=escape, upper=upper)


def b(content='', attrs=None, escape=False, upper=False):
    return tag('b', content=content, attrs=attrs, escape=escape, upper=upper)


def button(content='', attrs=None, escape=False, upper=False):
    return tag('button', content=content, attrs=attrs, escape=escape, upper=upper)


def div(content='', attrs=None, escape=False, upper=False):
    return tag('div', content=content, attrs=attrs, escape=escape, upper=upper)


def dt(content='', attrs=None, escape=False, upper=False):
    return tag('dt', content=content, attrs=attrs, escape=escape, upper=upper)


def dl(content='', attrs=None, escape=False, upper=False):
    return tag('dl', content=content, attrs=attrs, escape=escape, upper=upper)


def em(content='', attrs=None, escape=False, upper=False):
    return tag('em', content=content, attrs=attrs, escape=escape, upper=upper)


def embed(content='', attrs=None, escape=False, upper=False):
    return tag('embed', content=content, attrs=attrs, escape=escape, upper=upper)


def figure(content='', attrs=None, escape=False, upper=False):
    return tag('figure', content=content, attrs=attrs, escape=escape, upper=upper)


def form(content='', attrs=None, escape=False, upper=False):
    return tag('form', content=content, attrs=attrs, escape=escape, upper=upper)


def h1(content='', attrs=None, escape=False, upper=False):
    return tag('h1', content=content, attrs=attrs, escape=escape, upper=upper)


def h2(content='', attrs=None, escape=False,  upper=False):
    return tag('h2', content=content, attrs=attrs, escape=escape, upper=upper)


def h3(content='', attrs=None, escape=False, upper=False):
    return tag('h3', content=content, attrs=attrs, escape=escape, upper=upper)


def h4(content='', attrs=None, escape=False, upper=False):
    return tag('h4', content=content, attrs=attrs, escape=escape, upper=upper)


def h5(content='', attrs=None, escape=False, upper=False):
    return tag('h5', content=content, attrs=attrs, escape=escape, upper=upper)


def h6(content='', attrs=None, escape=False, upper=False):
    return tag('h6', content=content, attrs=attrs, escape=escape, upper=upper)


def img(attrs=None, upper=False):
    return tag('img', attrs=attrs, close=False, upper=upper)


def ul(content='', attrs=None, escape=False, upper=False):
    return tag('ul', content=content, attrs=attrs, escape=escape, upper=upper)


def ol(content='', attrs=None, escape=False, upper=False):
    return tag('ol', content=content, attrs=attrs, escape=escape, upper=upper)


def li(content='', attrs=None, escape=False, upper=False):
    return tag('li', content=content, attrs=attrs, escape=escape, upper=upper)


def p(content='', attrs=None, escape=False, upper=False):
    return tag('p', content=content, attrs=attrs, escape=escape, upper=upper)


def pre(content='', attrs=None, escape=False, upper=False):
    return tag('pre', content=content, attrs=attrs, escape=escape, upper=upper)


def br(content='', attrs=None, upper=False):
    return tag('br', content=content, attrs=attrs, upper=upper, close=False)


def hr(content='', attrs=None, upper=False):
    return tag('hr', content=content, attrs=attrs, upper=upper, close=False)


if __name__ == '__main__':
    pass
