#!/usr/bin/env python3
# Yonghang Wang

import sys
import argparse
import os
import re
import csv
import copy
import json
import traceback
import string
from wcwidth import wcswidth
from collections import defaultdict
from itertools import zip_longest
#from colorama import Fore, Back, Style
from colors import color
from qic import commandline


def prepare_table(xjson,xheader=None) :
    header=list()
    if xheader :
        if type(xheader) is list :
            header = xheader
        else :
            header = [ h for h in xheader.split(",") if h]
    data = list()
    try:
        if type(xjson) is str :
            js = json.loads(xjson)
        else :
            js = xjson
        if type(js) is list and all([type(i) is list for i in js]) :
            for row in js :
                r=list()
                for col in row :
                    r.append(str(col))
                data.append(r)
        elif type(js) is list and all([type(i) is dict for i in js]) :
            # now each row is a dict
            if not header :
                loaded=set()
                for row in js :
                    for k in row.keys() :
                        if k not in loaded :
                            header.append(k)
                            loaded.add(k)
            for row in js :
                r=list()
                for h in header :
                    r.append(row.get(h,""))
                data.append(r)
        else :
            print("# not supported format.",file=sys.stderr,flush=True)
            print(json.dumps(js,indent=2),file=sys.stderr,flush=True)
            return (None,None)
    except:
        traceback.print_exc()
        return (None,None)
    if header :
        return (data,header)
    else :
        return (data[1:],data[0])

class xtable:
    def __init__(self, data=None, header=None, cols=None, noheader=False,tree=False,maxrows=2**30, widthhint=None,rowperpage=2**30,debug=False):
        self.__noheader = noheader
        self.__maxrows = maxrows
        self.__rowperpage = rowperpage or 2**30
        self.__widthhint = widthhint
        self.__tree = tree 
        self.__data = data or list()
        self.__header = header or list()
        if cols and re.search(",", cols):
            ncols = len(header)
            xmap = [int(i) for i in re.split(r",", cols) if int(i) < ncols]
            self.__header = [header[i] for i in xmap]
            self.__data = list()
            if data :
                for d in data:
                    self.__data.append([d[i] for i in xmap])
        else:
            if self.__noheader and len(self.__data) > 0 :
                self.__header = self.__data[0]
                self.__data = self.__data[1:self.__maxrows]
        self.__num_of_cols = len(self.__header)
        self.__debug = debug

    def get_data(self) :
        return self.__data
    def get_header(self) :
        return self.__header

    @staticmethod
    def init_from_csv(csvfile, xheader=None, delimiter=',', quotechar='"'):
        header=list()
        data=list()
        if xheader :
            if type(xheader) is list :
                header = xheader
            else :
                header = [ h for h in xheader.split(",") if h]
        import os
        csvfile = os.path.expanduser(csvfile)
        with open(csvfile,newline='') as cf :
            reader = csv.reader(cf, delimiter=delimiter, quotechar=quotechar)
            data += [[c for c in r] for r in reader if r ]
        if not header and len(data)>0:
            header = data[0]
            data = data[1:]
        return xtable(data,header)

    @staticmethod
    def init_from_csv_fh(csvfh, xheader=None, delimiter=',', quotechar='"'):
        header=list()
        data=list()
        if xheader :
            if type(xheader) is list :
                header = xheader
            else :
                header = [ h for h in xheader.split(",") if h]
        reader = csv.reader(csvfh, delimiter=delimiter, quotechar=quotechar)
        data += [[c for c in r] for r in reader if r]
        if not header and len(data)>0:
            header = data[0]
            data = data[1:]
        return xtable(data,header)

    @staticmethod
    def init_from_json(xjson, xheader=None):
        if type(xjson) is str and os.path.isfile(xjson) :
            xjson = open(xjson,"r").read()
        data,hdr = prepare_table(xjson,xheader)
        return xtable(data,hdr)

    @staticmethod
    def init_from_list(xlist, xheader=None):
        data,hdr = prepare_table(xlist,xheader)
        return xtable(data,hdr)

    def __len__(self):
        return len(self.__data)

    def __getitem__(self, pos):
        return self.__data[pos]

    def __add__(self, other):
        if self.__num_of_cols != other.__num_of_cols:
            return None
        return xtable(self.__data + other.__data, self.__header)

    def __iadd__(self, other):
        if self.__num_of_cols != other.__num_of_cols:
            return None
        self.__data += other.__data

    def json(self):
        import json
        tbl = list()
        for r in self.__data:
            row = dict()
            for ix, val in enumerate(r):
                row[self.__header[ix]] = val
            tbl.append(row)
        return json.dumps(tbl, indent=2)

    def yaml(self):
        import yaml
        tbl = list()
        for r in self.__data:
            row = dict()
            for ix, val in enumerate(r):
                row[self.__header[ix]] = val
            tbl.append(row)
        return yaml.safe_dump(tbl, default_flow_style=False)

    def markdown(self):
        if not self.__header  or not self.__data :
            return ""
        res = ""
        width = [int(0) for _ in range(len(self.__header))]
        for r in ([self.__header] + self.__data) :
            for i, c in enumerate(r) :
                if len(str(c)) > int(width[i]) :
                    width[i] = len(c)
        width = [max(4,w) for w in width]
        fmtstr = "| " + "|".join([" {:"+str(w)+"} " for w in width]) + " |"
        res += (fmtstr.format(*self.__header)) + "\n"
        res += (fmtstr.format(*(['-'*w for w in width]))) + "\n"
        for r in self.__data :
            if r :
                res += (fmtstr.format(*r)) + "\n"
        return res

    def csv(self):
        import io
        si = io.StringIO()
        w = csv.writer(si)
        if self.__header:
            w.writerow(self.__header)
        for r in self.__data:
            w.writerow(r)
        return si.getvalue()

    def html(self):
        res = '<table border=1 style="border-collapse:collapse;">\n'
        res += "<tr>\n"
        for h in self.__header:
            res += "<td><b>" + str(h) + "</b></td>\n"
        res += "</tr>\n"
        for row in self.__data:
            res += "<tr>\n"
            for c in row:
                if not c :
                    if c == 0 :
                        c = "0"
                    else :
                        c = ""
                res += "<td><pre>" + str(c) + "</pre></td>\n"
            res += "</tr>\n"
        return res

    def pivot(self):
        maxcolwidth = max([wcswidth(h) for h in self.__header])
        fmtstr = "{:" + str(maxcolwidth) + "} : {}"
        res = ""
        for r, row in enumerate(self.__data):
            if r > 0:
                res += "--\n"
            for i, c in enumerate(row):
                res += fmtstr.format(self.__header[i], c) + "\n"
        return res

    def __wcswidth_x(self, s):
        res = 0
        for ln in s.splitlines():
            wclen = wcswidth(ln)
            if wclen > res:
                res = wclen
        return res

    def __splitstring(self, s, maxcolwidth):
        result = list()
        for ln in s.splitlines():
            if wcswidth(ln) <= maxcolwidth:
                result.append(ln)
            else:
                left = ln
                while left:
                    start = 0
                    end = min(maxcolwidth, len(left))
                    oldend = end
                    while end > start and (wcswidth(left[start:end]) > maxcolwidth or left[end-1] not in string.punctuation+string.whitespace ):
                        end -= 1
                    if end == start :
                        end = oldend
                    result.append(left[start:end])
                    left = left[end:]
        return result

    def __splitrow(self, row, width):
        return zip_longest(*[self.__splitstring(str(c), width[ix]) for ix,c in enumerate(row) if ix<len(width)], fillvalue="")

    def __repr__(self):
        if self.__debug :
            print("# self.__header = ",self.__header, file=sys.stderr, flush=True)
            print("# self.__data = \n",self.__data, file=sys.stderr, flush=True)
        def supports_color():
            plat = sys.platform
            supported_platform = plat != 'Pocket PC' and (plat != 'win32' or 'ANSICON' in os.environ)
            is_a_tty = hasattr(sys.stdout, 'isatty') and sys.stdout.isatty()
            m = re.search(r"^xterm",os.environ.get("TERM","n/a"),re.IGNORECASE)
            try :
                ret,out,err = commandline.qx("uname -s")
            except :
                return False
            iscygwin = re.search(r"cygwin",out,re.IGNORECASE)
            return (is_a_tty or iscygwin) and (m or supported_platform)
        colored = False
        if supports_color() or os.environ.get("force_ansicolor","").lower() in ["true","yes","y","1"] :
            colored = True
        if os.environ.get("force_ansicolor","").lower() in ["false","no","n","0"] :
            colored = False
        width = [0 for _ in range(len(self.__header))]
        for row in self.__data + [self.__header]:
            for ix, col in enumerate(row):
                if not col :
                    if col == 0 :
                        col = "0"
                    else :
                        col = ""
                if ix > len(width) - 1:
                    break
                wclen = self.__wcswidth_x(str(col))
                if wclen > width[ix]:
                    width[ix] = wclen
        #"0:20,1:30"
        if self.__widthhint :
            for s in self.__widthhint.split(",") :
                m = re.match(r"(\d+):(\d+)",s)
                if m :
                    ix = int(m.group(1))
                    w = int(m.group(2))
                    if 0 <= ix < len(width) and w > 0 and w < width[ix] :
                        width[ix] = w
        twidth = copy.copy(width)
        for ix, w in enumerate(twidth):
            twidth[ix] = (
                w - wcswidth(str(self.__header[ix])) + len(str(self.__header[ix]))
            )
        fmtstr = "".join(["{:" + str(l + 1) + "}" for l in twidth])
        res = ""
        headlines=""
        if not self.__noheader:
            xhdr =  [h[:width[i]] for i,h in enumerate(self.__header)]
            if colored :
                hcolor = os.environ.get("xtable_header_color","21")
                m = re.search(r"(\d+)",hcolor)
                if m :
                    hc = int(m.group(1))
                else :
                    hc = 21
                res += '\033[1m' + color(fmtstr.format(*xhdr).strip(),fg=hc) + '\033[0m' + "\n"
                res += "|".join(['-'*(int(w)) for w in width]) + "\n"
            else :
                res += fmtstr.format(*xhdr).strip() + "\n"
                res += "|".join(['-'*(int(w)) for w in width]) + "\n"
            headlines = res
        oldrow = None
        rcolor = os.environ.get("xtable_rows_color","58:95")
        m = re.search(r"(\d+):(\d+)",rcolor)
        if m :
            c1 = int(m.group(1))
            c2 = int(m.group(2))
        else :
            c1 = 58
            c1 = 95
        forecolors=[lambda x:color(str(x),fg=c1),lambda x:color(str(x),fg=c2)]
        for rn,r in enumerate(self.__data):
            if rn != 0 and rn % self.__rowperpage == 0 :
                res += headlines
            if rn == 0 :
                row = [str(c) if c or c==0 else "" for c in r]
                oldrow = r
            else :
                if not self.__tree :
                    row = [str(c) if c or c==0 else "" for c in r]
                else :
                    nr = [ c for c in r ]
                    for ix, c in enumerate(r) :
                        if (oldrow[ix] is None and c is None) or c == oldrow[ix] :
                            nr[ix] = ""
                        else :
                            break
                    row = [str(c) if c or c==0 else "" for c in nr]
                    oldrow = r
            if len(row) < len(width):
                row.extend([""] * (len(width) - len(row)))
            for t in self.__splitrow(row,width):
                twidth = copy.copy(width)
                for ix, w in enumerate(twidth):
                    twidth[ix] = w - wcswidth(str(t[ix])) + len(str(t[ix]))
                fmtstr = "".join(["{:" + str(l + 1) + "}" for l in twidth])
                if colored :
                    res += forecolors[rn%2](fmtstr.format(*t).rstrip()) + "\n"
                else :
                    res += fmtstr.format(*t).rstrip() + "\n"
        return res

def tokenize(s):
    offset = 0
    tokens = list()
    while True:
        m = re.search(r"\S+\s*", s[offset:])
        if m:
            tokens.append([offset + m.start(), offset + m.end(), m.group().strip()])
            offset += m.end()
        else:
            break
    tokens[-1][1] += 9999
    return tokens


def xtable_main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-H", "--header", dest="header", help="header columns")
    parser.add_argument("-f", "--infile", dest="infile", help="input file")
    parser.add_argument( "-C", "--dump-column", dest="dumpcols", help="only print columns indentified by index numbers.",)
    parser.add_argument( "-b", "--sep-char", dest="sepchar", default="\s+", help="char to seperate columns. note, default is SPACE, not ','",)
    parser.add_argument( "-w", "--widthhint", dest="widthhint", default=None, help="hint for col width. '0:20,2:30,'",)
    parser.add_argument( "-p", "--page", dest="page", type=int,default=2**30, help="rows per page. print header line again",)
    parser.add_argument( "-t", "--table", dest="table", action="store_true", default=False, help="input preformatted by spaces. header should not include spaces.",)
    parser.add_argument( "-c", "--column", action="append", dest="column", help="column names. used when there're spaces within.",)
    parser.add_argument( "-v", "--pivot", dest="pivot", action="store_true", default=False, help="pivot wide tables.",)
    parser.add_argument( "-s", "--sortby", dest="sortby", help="column id starts with 0.")
    parser.add_argument("-F", "--tgtformat", dest="format", help="json,yaml,csv,html or md(markdown)")
    parser.add_argument( "-X", "--debug", dest="debug", action="store_true", default=False, help="debug mode",)
    parser.add_argument( "--forcecsv", dest="forcecsv", action="store_true", default=False, help="treat input as CSV",)
    parser.add_argument( "--dataonly", dest="dataonly", action="store_true", default=False, help="indicate there's no header",)
    parser.add_argument( "--tree", dest="tree", action="store_true", default=False, help="indicate the table is of tree struture",)
    parser.add_argument( "--colors", dest="colors", action="store_true", default=False, help="show colors for xtable_header/rows_color",)
    args = parser.parse_args()

    _args_lineno = False # disabled option

    def showcolors() :
        for i in range(256) :
            print(color('Color {:3}  '.format(i), fg=i), end="")
            if (i+1)%8 == 0 :
                print("")
    if args.colors :
        showcolors()
        sys.exit(0)

    def showres(t) :
        if args.pivot:
            print(t.pivot())
        else:
            if args.format == "json":
                print(t.json(), end="")
            elif args.format == "yaml":
                print(t.yaml(), end="")
            elif args.format == "csv":
                print(t.csv(), end="")
            elif args.format == "html":
                print(t.html(), end="")
            elif args.format in ["md","markdown"]:
                print(t.markdown(), end="")
            else:
                print(t, end="")

    colsdict = defaultdict()
    colsdict_revert = defaultdict()
    if args.column:
        for c in args.column:
            oc = c
            mc = re.sub("\s", "_", oc)
            colsdict[oc] = mc
            colsdict_revert[mc] = oc
    if args.header and colsdict:
        for c, nc in colsdict.items():
            args.header = re.sub(c, nc, args.header)
    xheader = None
    header = list()
    if _args_lineno:
        header.append("#")
    if args.header:
        mhdr = args.header
        if not args.table:
            header.extend(re.split(r"{}".format(args.sepchar), mhdr))
        else:
            xheader = tokenize(mhdr)
            header = [v.strip() for (s, t, v) in xheader]
    data = list()
    lno = 0
    INPUT = sys.stdin
    if args.infile:
        INPUT = open(args.infile, "r") 

    def dump_xtable(xt) :
        res =  "# xtable.header : " +  json.dumps(xt.get_header()) + "\n"
        res += "# xtable.data   : " +  json.dumps(xt.get_data())  
        return
        
    if args.forcecsv :
        done = False
        try :
            xt = xtable.init_from_csv_fh(INPUT,delimiter=args.sepchar)
            xt = xtable(
                        header=xt.get_header(),
                        data=xt.get_data(),
                        cols=args.dumpcols,
                        noheader=args.dataonly,
                        tree=args.tree,
                        widthhint=args.widthhint,
                        rowperpage=args.page,
                    )
            if args.debug :
                print(dump_xtable(xt),file=sys.stderr,flush=True)
            showres(xt)
            done = True
        except :
            traceback.print_exc()
            pass
        if done :
            sys.exit(0)

    instr = INPUT.read()
    js = None
    try :
        js = json.loads(instr)
    except :
        INPUT = instr.splitlines()

    if js :
        if type(js) is list :
            xt = xtable.init_from_json(js,args.header)
            xt = xtable(
                        header=xt.get_header(),
                        data=xt.get_data(),
                        cols=args.dumpcols,
                        noheader=args.dataonly,
                        tree=args.tree,
                        widthhint=args.widthhint,
                        rowperpage=args.page,
                    )
            if args.debug :
                print(dump_xtable(xt),file=sys.stderr,flush=True)
            showres(xt)
        sys.exit(0)

    for ln in INPUT:
        if not ln or not re.search(r"\S+", ln):
            continue
        if not header:
            for c, nc in colsdict.items():
                ln = re.sub(c, nc, ln)
        if not args.table:
            arr = re.split(r"{}".format(args.sepchar), ln.strip())
        else:
            if xheader:
                arr = [ln[s:t].strip() for (s, t, v) in xheader]
            else:
                for c, nc in colsdict.items():
                    ln = re.sub(c, nc, ln)
                xheader = tokenize(ln)
                if _args_lineno:
                    header = ["#"] + [v.strip() for (s, t, v) in xheader]
                else:
                    header = [v.strip() for (s, t, v) in xheader]
                continue
        if len(header) == 0 or (_args_lineno and len(header) == 1):
            if not args.table:
                header.extend(arr)
        else:
            lno += 1
            if _args_lineno:
                data.append([str(lno)] + arr)
            else:
                data.append(arr)
    oheader = list()
    for h in header:
        nh = colsdict_revert.get(h, h)
        oheader.append(nh)
    if args.dataonly:
        data = [oheader] + data
    if args.sortby:
        def fsort(x):
            v = list()
            for i in re.split(r",", args.sortby):
                v0 = x[int(i)] or ""
                if re.match(r"^\d+(\.\d*)*$", v0):
                    v.append(float(v0))
                else:
                    v.append(0)
                v.append(v0)
            return v
        data = sorted(data, key=fsort)
    xt = xtable(
                header=oheader,
                data=data,
                cols=args.dumpcols,
                noheader=args.dataonly,
                tree=args.tree,
                widthhint=args.widthhint,
                rowperpage=args.page,
                debug=args.debug
            )
    if args.debug :
        dump_xtable(xt)
    showres(xt)
    

if __name__ == "__main__":
    xtable_main()
