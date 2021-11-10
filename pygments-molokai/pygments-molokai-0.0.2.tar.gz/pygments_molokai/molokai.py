# -*- coding: utf-8 -*-
"""
    Molokai Colorscheme
    ~~~~~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter
"""
from pygments.style import Style
from pygments.token import Token, Generic, Comment, Keyword, String, Number, Operator, Name

class MolokaiStyle(Style):

    background_color = '#1B1D1E'
    styles = {
        Token:              '#F8F8F2 bg:#1B1D1E',
        Number:             '#AE81FF',
        String:             '#E6DB74',
        Name.Constant:      '#AE81FF bold',
        Generic.Inserted:   'bg:#13354A',
        Generic.Deleted:    '#960050 bg:#1E0010',
        Generic.Error:      '#E6DB74 bg:#1E0010',
        Generic.Traceback:  '#F92672 bg:#232526 bold',
        Name.Exception:     '#A6E22E bold',
        Number.Float:       '#AE81FF',
        Name.Function:      '#A6E22E',
        Name.Attribute:     '#A6E22E',
        Name.Variable:      'noinherit #FD971F',
        Name.Label:         'noinherit #E6DB74',
        Operator.Word:      '#F92672',
        Comment.Preproc:    '#A6E22E',
        Name.Entity:        '#66D9EF italic',
        Keyword:            '#F92672 bold',
        Name.Tag:           '#F92672 bold',
        Generic.Heading:    '#ef5939',
        Generic.Subheading: '#ef5939',
        Keyword.Type:       'noinherit #66D9EF',
        Generic.Emph:       '#808080 underline',
        Comment:            '#7E8E91',
        Generic.Output:     '#465457',
    }
