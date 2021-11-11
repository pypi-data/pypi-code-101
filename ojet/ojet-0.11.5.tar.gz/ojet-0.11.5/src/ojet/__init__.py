__version__ = "0.11.5"

def genelem(name, etype=2, hyphen='é', defclass=lambda x: '',mparameters=[]):
    def constructor(self, *elements, **attributes):
        self.elements = list(elements)
        self.mparameters = mparameters
        self.attributes = dict()
        self.containers = dict()
        self.defclasses = dict()
        idefclass = attributes['defclass'] if 'defclass' in attributes else defclass
        if etype==3:
            for p in self.mparameters: 
                if p not in attributes: raise Exception(f'{p} is a mandatory attribute for class: {name.__name__}!')
            self.id=attributes['id']
            ko = attributes['jsparameters']['knockout']
            self.containers[self.id] = lambda  c: f'\n{ko}.applyBindings(new {c}_OjetClass(), document.getElementById("{c}_container"));'
            self.defclasses[self.id] = lambda c: f'''
                class {c}_OjetClass {{
                    constructor() {{
                    {idefclass(attributes['jsparameters']) if 'jsparameters' in attributes else ''}
                    }}
                }}
            '''
        for a in attributes.keys():
            if a[0] == '_': self.attributes[a[1:]] = attributes[a].replace(hyphen, '-')
        if 'father' in attributes.keys() and attributes['father']: attributes['father'].elements.append(self)
    def render(self):
        ret =[]
        for a in self.attributes: 
            if '"' in self.attributes[a]: ret.append(f" {a}='{self.attributes[a]}'")
            else: ret.append(f' {a}="{self.attributes[a]}"')
        attribs = ''.join(ret)
        if etype == 1: return f'<{name.__name__}{attribs}/>'
        else:
            ret = []
            for e in self.elements:
                try: ret.append(e.render())
                except: ret.append(e)
                if hasattr(e, 'containers'): self.containers.update(e.containers)
                if hasattr(e, 'defclasses'): self.defclasses.update(e.defclasses)
            elems = ''.join(ret)
            return f'<{name.__name__}{attribs}>{elems}</{name.__name__}>'
    def add(self, element):
        self.elements.append(element)
    name = type(name, (object,), dict(__init__= constructor, render=render,add=add))
    return name

def classtofunc(x):
    f = lambda *elements, **attributes: x(*elements, **attributes)
    return f

AREA = classtofunc(genelem('area', 1))
BASE = classtofunc(genelem('base', 1))
BR = classtofunc(genelem('br', 1))
COL = classtofunc(genelem('col', 1))
EMBED = classtofunc(genelem('embed', 1))
HR = classtofunc(genelem('hr', 1))
IMG = classtofunc(genelem('img', 1))
INPUT = classtofunc(genelem('input', 1))
LINK = classtofunc(genelem('link', 1))
META = classtofunc(genelem('meta', 1))
PARAM = classtofunc(genelem('param', 1))
SOURCE = classtofunc(genelem('source', 1))
TRACK = classtofunc(genelem('track', 1))
WBR = classtofunc(genelem('wbr', 1))

A = classtofunc(genelem('a', 2))
ABBR = classtofunc(genelem('abbr', 2))
ADDRESS = classtofunc(genelem('address', 2))
APPLET = classtofunc(genelem('applet', 2))
ARTICLE = classtofunc(genelem('article', 2))
ASIDE = classtofunc(genelem('aside', 2))
AUDIO = classtofunc(genelem('audio', 2))
B = classtofunc(genelem('b', 2))
BDO = classtofunc(genelem('bdo', 2))
BLOCKQUOTE = classtofunc(genelem('blockquote', 2))
BODY = classtofunc(genelem('body', 2))
BUTTON = classtofunc(genelem('button', 2))
CANVAS = classtofunc(genelem('canvas', 2))
CAPTION = classtofunc(genelem('caption', 2))
CITE = classtofunc(genelem('cite', 2))
CODE = classtofunc(genelem('code', 2))
COLGROUP = classtofunc(genelem('colgroup', 2))
COMMAND = classtofunc(genelem('command', 2))
DATALIST = classtofunc(genelem('datalist', 2))
DD = classtofunc(genelem('dd', 2))
DEL = classtofunc(genelem('del', 2))
DETAILS = classtofunc(genelem('details', 2))
DFN = classtofunc(genelem('dfn', 2))
DIV = classtofunc(genelem('div', 2))
DL = classtofunc(genelem('dl', 2))
DT = classtofunc(genelem('dt', 2))
EM = classtofunc(genelem('em', 2))
FIELDSET = classtofunc(genelem('fieldset', 2))
FIGCAPTION = classtofunc(genelem('figcaption', 2))
FIGURE = classtofunc(genelem('figure', 2))
FOOTER = classtofunc(genelem('footer', 2))
FORM = classtofunc(genelem('form', 2))
H1 = classtofunc(genelem('h1', 2))
H2 = classtofunc(genelem('h2', 2))
H3 = classtofunc(genelem('h3', 2))
H4 = classtofunc(genelem('h4', 2))
H5 = classtofunc(genelem('h5', 2))
H6 = classtofunc(genelem('h6', 2))
HEAD = classtofunc(genelem('head', 2))
HEADER = classtofunc(genelem('header', 2))
HTML = classtofunc(genelem('html', 2))
I = classtofunc(genelem('i', 2))
IFRAME = classtofunc(genelem('iframe', 2))
INS = classtofunc(genelem('ins', 2))
KBD = classtofunc(genelem('kbd', 2))
LABEL = classtofunc(genelem('label', 2))
LEGEND = classtofunc(genelem('legend', 2))
LI = classtofunc(genelem('li', 2))
MAP = classtofunc(genelem('map', 2))
MARK = classtofunc(genelem('mark', 2))
MENU = classtofunc(genelem('menu', 2))
MENUITEM = classtofunc(genelem('menuitem', 2))
METER = classtofunc(genelem('meter', 2))
NAV = classtofunc(genelem('nav', 2))
NOSCRIPT = classtofunc(genelem('noscript', 2))
OBJECT = classtofunc(genelem('object', 2))
OL = classtofunc(genelem('ol', 2))
OPTGROUP = classtofunc(genelem('optgroup', 2))
OPTION = classtofunc(genelem('option', 2))
OUTPUT = classtofunc(genelem('output', 2))
P = classtofunc(genelem('p', 2))
PRE = classtofunc(genelem('pre', 2))
PROGRESS = classtofunc(genelem('progress', 2))
Q = classtofunc(genelem('q', 2))
RP = classtofunc(genelem('rp', 2))
RT = classtofunc(genelem('rt', 2))
RUBY = classtofunc(genelem('ruby', 2))
S = classtofunc(genelem('s', 2))
SAMP = classtofunc(genelem('samp', 2))
SCRIPT = classtofunc(genelem('script', 2))
SECTION = classtofunc(genelem('section', 2))
SELECT = classtofunc(genelem('select', 2))
SMALL = classtofunc(genelem('small', 2))
SPAN = classtofunc(genelem('span', 2))
STRONG = classtofunc(genelem('strong', 2))
STYLE = classtofunc(genelem('style', 2))
SUB = classtofunc(genelem('sub', 2))
SUP = classtofunc(genelem('sup', 2))
TABLE = classtofunc(genelem('table', 2))
TBODY = classtofunc(genelem('tbody', 2))
TD = classtofunc(genelem('td', 2))
TEXTAREA = classtofunc(genelem('textarea', 2))
TFOOT = classtofunc(genelem('tfoot', 2))
TH = classtofunc(genelem('th', 2))
THEAD = classtofunc(genelem('thead', 2))
TIME = classtofunc(genelem('time', 2))
TITLE = classtofunc(genelem('title', 2))
TR = classtofunc(genelem('tr', 2))
U = classtofunc(genelem('u', 2))
UL = classtofunc(genelem('ul', 2))
VAR = classtofunc(genelem('var', 2))
VIDEO = classtofunc(genelem('video', 2))

TEMPLATE = classtofunc(genelem('template', 2))
OJBINDFOREACH = classtofunc(genelem('oj-bind-for-each', 2))
OJBINDTEXT = classtofunc(genelem('oj-bind-text', 2))
OJBUTTON = classtofunc(genelem('oj-button', 2))
OJBUTTONSETMANY = classtofunc(genelem('oj-buttonset-many', 2))
OJCHART = classtofunc(genelem('oj-chart', 2))
OJCHARTITEM = classtofunc(genelem('oj-chart-item', 2))
OJCHARTSERIES = classtofunc(genelem('oj-chart-series', 2))
OJCOLLAPSIBLE = classtofunc(genelem('oj-collapsible', 2))
OJINPUTTEXT = classtofunc(genelem('oj-input-text', 2))
OJLABEL = classtofunc(genelem('oj-label', 2))
OJLEDGAUGE = classtofunc(genelem('oj-led-gauge', 2))
OJMENU = classtofunc(genelem('oj-menu', 2))
OJMENUBUTTON = classtofunc(genelem('oj-menu-button', 2))
OJOPTION = classtofunc(genelem('oj-option', 2))
OJSELECTMANY = classtofunc(genelem('oj-select-many', 2))
OJTABLE = classtofunc(genelem('oj-table', 2))
OJTOOLBAR = classtofunc(genelem('oj-toolbar', 2))
OJTREEMAP = classtofunc(genelem('oj-treemap', 2))
OJTREEMAPNODE = classtofunc(genelem('oj-treemap-node', 2))
OJTREEVIEW = classtofunc(genelem('oj-tree-view', 2))


OJCONTAINER = lambda *elements, **attributes: DIV(genelem('span', 3, mparameters=['id', 'jsparameters'])(*elements, **attributes), _id=f'{attributes["id"]}_container', _class=f'{attributes["style"]}' if 'style' in attributes else '')
    
BASICTEMPLATE = TEMPLATE(OJCHARTITEM(**{"_value": "[[item.data.value]]","_group-id": "[[ [item.data.category] ]]","_series-id": "[[item.data.serie]]", "_hidden_categories": "{{hiddenCategories}}"}), **{"_slot": "itemTemplate", "_data-oj-as": "item"})         
BOXTEMPLATE = TEMPLATE(OJCHARTITEM(**{"_items": "[[item.data.outliers]]", "_q1": "[[item.data.q1]]", "_q2": "[[item.data.q2]]", "_q3": "[[item.data.q3]]", "_high": "[[item.data.high]]", "_low": "[[item.data.low]]","_group-id": "[[ [item.data.group] ]]","_series-id": "[[item.data.series]]", "_hidden_categories": "{{hiddenCategories}}"}), **{"_slot": "itemTemplate", "_data-oj-as": "item"})         
BUBBLETEMPLATE = TEMPLATE(OJCHARTITEM(**{"_x": "[[item.data.x]]", "_y": "[[item.data.y]]", "_z": "[[item.data.z]]", "_group-id": "[[ [item.data.group] ]]","_series-id": "[[item.data.series]]", "_hidden_categories": "{{hiddenCategories}}"}), **{"_slot": "itemTemplate", "_data-oj-as": "item"})         
RANGETEMPLATE = TEMPLATE(OJCHARTITEM(**{"_high": "[[item.data.high]]", "_low": "[[item.data.low]]","_group-id": "[[ [item.data.group] ]]","_series-id": "[[item.data.series]]", "_hidden_categories": "{{hiddenCategories}}"}), **{"_slot": "itemTemplate", "_data-oj-as": "item"})         
SCATTERTEMPLATE = TEMPLATE(OJCHARTITEM(**{"_x": "[[item.data.x]]", "_y": "[[item.data.y]]", "_group-id": "[[ [item.data.group] ]]","_series-id": "[[item.data.series]]", "_hidden_categories": "{{hiddenCategories}}"}), **{"_slot": "itemTemplate", "_data-oj-as": "item"})         

WEBDIS = SCRIPT('''
function createCORSRequest(method, url) {
    var xhr = new XMLHttpRequest();
    if ("withCredentials" in xhr) {
        xhr.open(method, url, true);
    } else if (typeof XDomainRequest != "undefined") {
        xhr = new XDomainRequest();
        xhr.open(method, url);
    } else {
        xhr = null;
    }
    return xhr;
}
function makeCorsRequest(url, onfinish, onerror) {
    var xhr = createCORSRequest('GET', url);
    if (!xhr) {
        throw 'Cannot create a cross domain request';
        return;
    }
    var noop = function () {};
    if (!onfinish) {
        onfinish = noop;
    }
    if (!onerror) {
        onerror = noop;
    }
    xhr.onloadend = function(x) {
        onfinish(JSON.parse(xhr.responseText));
    };
    xhr.onerror = onerror;
    xhr.send();
}
class Webdis {
    constructor(port=7379) {
        this.port = port;
        this.url = 'http://localhost:' + port;
        var url = this.url + '/PING';
        makeCorsRequest(url, function (response) {
            if (response.PING[1] !== 'PONG') throw 'Error connection to server Webdis!';
        });
    }
    set(key, value) {
        var url = this.url + '/SET/' + key + '/' + JSON.stringify(value);
        makeCorsRequest(url, function (response) {
            if (response.SET[1] !== 'OK') throw 'Error when setting a value into Webdis!';
        });
    }
    get(key, afterdone) {
        var url = this.url + '/GET/' + key;
        makeCorsRequest(url, function (response) {
            var r = response.GET;
            afterdone(r);
        });
    }
}
''')

class Ojet:

    def __init__(self, title=None):
        STYLEIMPORT = '''
            @import url('https://static.oracle.com/cdn/jet/11.1.0/default/css/redwood/oj-redwood-min.css');
            @import url('https://static.oracle.com/cdn/fnd/gallery/2107.3.0/images/iconfont/ojuxIconFont.min.css');
        '''
        LIBSANDLANG = '''
              var browserLang = window.navigator.language || window.navigator.userLanguage;
              requirejs.config({
                paths: {
                    'knockout': 'https://static.oracle.com/cdn/jet/11.1.0/3rdparty/knockout/knockout-3.5.1',
                    'jquery': 'https://static.oracle.com/cdn/jet/11.1.0/3rdparty/jquery/jquery-3.6.0.min',
                    'jqueryui-amd': 'https://static.oracle.com/cdn/jet/11.1.0/3rdparty/jquery/jqueryui-amd-1.12.1.min',
                    'hammerjs': 'https://static.oracle.com/cdn/jet/11.1.0/3rdparty/hammer/hammer-2.0.8.min',
                    'ojdnd': 'https://static.oracle.com/cdn/jet/11.1.0/3rdparty/dnd-polyfill/dnd-polyfill-1.0.2.min',
                    'ojs': 'https://static.oracle.com/cdn/jet/11.1.0/default/js/min',
                    'ojL10n': 'https://static.oracle.com/cdn/jet/11.1.0/default/js/ojL10n',
                    'ojtranslations': 'https://static.oracle.com/cdn/jet/11.1.0/default/js/resources',
                    'preact': 'https://static.oracle.com/cdn/jet/11.1.0/3rdparty/preact/dist/preact.umd',
                    'text': 'https://static.oracle.com/cdn/jet/11.1.0/3rdparty/require/text',
                    'signals': 'https://static.oracle.com/cdn/jet/11.1.0/3rdparty/js-signals/signals.min',
                    'touchr': 'https://static.oracle.com/cdn/jet/11.1.0/3rdparty/touchr/touchr',
                    'customElements': 'https://static.oracle.com/cdn/jet/v8.3.0/3rdparty/webcomponents/custom-elements.min',
                    'css': 'https://static.oracle.com/cdn/jet/11.1.0/3rdparty/require-css/css.min'
                },
                config: {
                  i18n: { locale: browserLang },
                  ojL10n: { locale: browserLang }
                }
              });
      '''
        
        self.styles = dict()
        self.functions = dict()
        self.html = HTML()
        self.head = HEAD(father = self.html)
        self.meta1 = META(father=self.head, _charset='utf-8')
        self.meta2 = META(father=self.head, _keywords='cpu')
        self.meta3 = META(father=self.head, _name='description', _content='Charts showing cpu data from exawatcher')
        self.styleimport = STYLE(STYLEIMPORT, father=self.head, _type='text/css')
        self.script1 = SCRIPT(father=self.head, _src="https://static.oracle.com/cdn/jet/11.1.0/3rdparty/require/require.js")
        self.script2 = SCRIPT(LIBSANDLANG, father=self.head, _type='text/javascript')
        self.body = BODY(father = self.html)
        self.requires=[]
        self.commonjavascript = ''

    def genHtmlTitle(self, title):
        self.title = TITLE(title, father=self.head)

    def genstyle(self, name, value):
        self.styles[name] = value

    def addjavascript(self, js):
        self.commonjavascript += js
    
    def controlrequires(self):
        d=dict()
        i = 0
        for e in self.requires:
            d[e] = f'p{i}'
            i += 1
        for e in ["ojs/ojbootstrap"]:
            if e not in d: raise Exception(f'"{e}" is a required library')
        return d

    
    def require(self, *elems):
        self.requires = list(elems)
        return self.controlrequires()
    
    def jupyter(self, width=800, height=500, name='jupyter.html'):
        from IPython.display import IFrame as ifr, display
        with open(f'./{name}', 'w') as f: f.write(self.render())
        display(ifr(f'./{name}', width=width, height=height))

    def render(self):
        
        CUSTOM = '''
                {commonjavascript}
                require({requires},
                function ({parameters})
                {{
                    {defclasses}
                    {boot}.whenDocumentReady().then(() => {{
                        {initcontainers}
                    }});
                }});
        '''
        dr = self.controlrequires()
        userstyles = ''
        for x in self.styles: userstyles += f'.{x} {self.styles[x]}\n'
        self.head.add(STYLE(userstyles))
        self.body.render()
        parameters = [f'p{i}' for i in range(len(self.requires))]
        dformat = dict(initcontainers='', requires=self.requires, commonjavascript=self.commonjavascript, defclasses='', boot=dr["ojs/ojbootstrap"] ,parameters=','.join(parameters))
        for c in self.body.containers:
            f = self.body.containers[c]
            dformat['initcontainers'] += f(c)
        for c in self.body.defclasses:
           dformat['defclasses'] += self.body.defclasses[c](c)
        self.script3 = SCRIPT(CUSTOM.format(**dformat), father=self.head, _type='text/javascript')
        return self.html.render()