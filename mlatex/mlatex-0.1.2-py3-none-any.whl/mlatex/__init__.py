'''
basically this creates a table, and figure (with subfigures) in a way for auto reports.
need to call:
tex = initialise(text.tex)
that creates the document and you can load your packages here!
similar need to end the document with:
latex.end(tex)

to make a table use
latex.table
things to note, header and body of table are separate (so that lines can be made correctly.
it can split a long narrow table into several columns and handles multi tables (sort of).
note table and body need to be in the form for list of lists (so

[[A,B],[C,D]]
corresponds to
A B
C D
note A can either be a string or a typle/list
if its a typle/list make it in form ('gets written',style)
where style can be things like l,b,s (for italics, bold and textsc)

figure is pretty painless and is basically just a list of filenames and it plonks the graphs in with captions.


TODO: Adding in COLOR library to allow for colors :-)
'''



import math
import os

ALPHABET = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
NUMBERS = ['0','1','2','3','4','5','6','7','8','9']
ALIGNKEYS = 'lcr'
ALIGNB = {'l':'\\begin{flushleft}',
          'c':'\\begin{center}',
          'r':'\\begin{flushright}'}
ALIGNE = {'l':'\\end{flushleft}\n',
          'c':'\\end{center}\n',
          'r':'\\end{flushright}\n'}

BADDIES = {'_':'\\_',
           '%':'\\%'}

COMMANDS = {'\COMMA':','}

TABLETHRESHOLD = 50
MINCONTTABLELENGTH = 3

def writelist(latex,alist):
    for i in range(0,len(alist)):
        latex.write(alist[i])
        if i<len(alist)-1:
            latex.write(',')

def clean(rawstring):
    string = str(rawstring)
    newstring = ''
    for i in range(0,len(string)):
        if not string[i] in BADDIES:
            newstring += string[i]
            continue
        if i == 0:
            newstring+=BADDIES[string[i]]
        elif string[i-1:i+1] !=BADDIES[string[i]]:
            newstring+=BADDIES[string[i]]
        else:
            newstring+=string[i]
    for command in COMMANDS.keys():
        if command in newstring:
            newstring = newstring.replace(command,COMMANDS[command])
    return newstring
                   
def comment(latex,string):
    latex.write('% '+string+'\n')


def beginitemize(latex):
    latex.write('\\begin{itemize}\n')

def enditemize(latex):
    latex.write('\\end{itemize}\n')

def item(latex,text,style='',size = None,skip=None,color=None):
    latex.write('\\item ')
    lwrite(latex,text,style = style,size = size,skip=skip,color=color)

def beginenumerate(latex):
    latex.write('\\begin{enumerate}\n')

def endenumerate(latex):
    latex.write('\\end{enumerate}\n')

def lenumerate(latex,thelist,size = None,skip = None,color = None):
    beginenumerate(latex)
    for eorp in thelist:
        if type(eorp) in [type([]),type((1,0))]:
            elem = clean(eorp[0])
            if len(eorp) >1:
                style = eorp[1]
        else:
            elem = clean(eorp)
            style = ''
        item(latex,elem,style = style,size = size,skip = skip,color = color)
    endenumerate(latex)




def getpackandopts(package):
    if type(package) == type('string'):
        return package,''
    if len(package)==1:
        return package[0],''
    pack = package[0]
    opts = '['
    for i in range(1,len(package)):
        if i > 1:
            opts+=','
        opts += package[i]
    opts+=']'
    return package[0],opts



def usepackage(latex,package):
    pack,opts = getpackandopts(package)
    latex.write('\\usepackage')
    latex.write(opts)
    latex.write('{')
    latex.write(pack)
    latex.write('}\n')
    if pack == 'hyperref':
        return True
    return False


def addtocsolver(latex,href):
    index = '4'
    if href:
        index = '5'
    latex.write('\\DeclareRobustCommand{\\SkipTocEntry}['+index+']{}\n')
    


def initialise(fname,dclass = 'article',dopt = [],packages=['graphicx','booktabs']):
    latex = open(fname,'w')
    latex.write('\\documentclass[')
    writelist(latex,dopt)
    latex.write(']{')
    latex.write(dclass)
    latex.write('}\n')
    href = False
    for package in packages:
        hrefpack = usepackage(latex,package)
        if hrefpack:
            href = True
    addtocsolver(latex,href)
    latex.write('\\begin{document}\n')
    latex.write('\\newcounter{tabfix}')    
    return latex



def getfoldershort_sub(fname,sep):
    shortname = fname.replace('.tex','')
    fbits = fname.split(sep)
    folder = ''
    for i in range(0,len(fbits)-1):
        folder += fbits[i]+'/'
    return folder,shortname

def getfoldershortname(fname):
    for sep in ['/','\\']:
        if '/' in fname:
            return getfoldershort_sub(fname,sep)
    shortname = fname.replace('.tex','')
    folder = '.'
    return folder,shortname
    


def end(latex,fname,pdf=False,generate = False,runtimes = 5):
    folder,shortname = getfoldershortname(fname)
    latex.write('\n')
    latex.write('\\end{document}')
    latex.close()
    if not generate:
        return
    if pdf:
        for i in range(runtimes):
            os.system('pdflatex ' + shortname+'.tex -aux-directory='+folder+' -output-directory='+folder)
            os.system('bibtex ' + shortname)
    if not pdf:
        for i in range(runtimes):
            os.system('latex ' + shortname+'.tex')
            os.system('bibtex ' + shortname)
        os.system('DviPs ' + shortname+'.dvi')
        os.system('ps2pdf ' + shortname+'.ps')



def multiplecolumnscols(cols,columns,divider = '||'):
    colstemp = cols
    start = ''
    end = ''
    while colstemp[-1]== '|':
        end += colstemp[-1]
        colstemp = colstemp[:-1]
    while colstemp[0] == '|':
        start += colstemp[0]
        colstemp = colstemp[1:]
    newcols = start
    for i in range(0,columns):
        if i > 0 :
            newcols += divider
        newcols += colstemp
    newcols += end
    return newcols

def getlength(header,tableinfo):
    length = 0
    for row in header+tableinfo:
        lenny = len(row)
        if lenny > length:
            length = lenny
    return length
    
def multiplecolumnstableinfo(tableinfo,header,columns):
    if len(tableinfo) == 0 and len(header) == 0:
        return
    lenny = len(tableinfo)
    oneoncol = int(math.ceil((lenny-1)/float(columns)))
    newtableinfo = []
    newheader = []
    for row in header:
        newheader.append(row*columns)
    ci = 1
    blank = []
    length = getlength(header,tableinfo)
    for element in length:
        blank.append('')
    while True:
        row = []
        for i in range(0,columns):
            if i >= len(tableinfo):
                row+=blank
            else:
                row+=tableinfo[ci+i*oneoncol]
        newtableinfo.append(row)
        ci+=1
        if ci>oneoncol:
            break
    return newtableinfo,newheader
        



def subtable(latex,tableinfo,header,cols,caption,columns,label,place,borders,align,continued = False):
    if continued:
        latex.write('\\setcounter{table}{\\value{tabfix}}')
    else:
        latex.write('\\setcounter{tabfix}{\\value{table}}')
    latex.write('\\begin{table}['+place+']\n')
    if not align in ALIGNB:
        raise Exception()
    latex.write(ALIGNB[align])
    latex.write('\n')    
    assignlabel = None
    if caption!=None:
        if continued:
            latex.write('\\caption{'+clean(caption)+' -- Continued}')
        else:
            latex.write('\\caption{'+clean(caption)+'}')
            assignlabel = writelabel(latex,caption,label,'tab')
    latex.write('\\begin{tabular}{'+cols+'}\n')
    toprule(latex,borders)
    writerows(latex,header,borders)
    midrule(latex,borders)
    writerows(latex,tableinfo,borders)
    bottomrule(latex,borders)
    latex.write('\\end{tabular}\n')
    latex.write(ALIGNE[align])
    latex.write('\n')
    latex.write('\\end{table}\n')
    return assignlabel    

def writerows(latex,rows,borders):
    first = True
    for row in rows:        
        if not first:
            midrule(latex,borders,minimalhandle = False)
        else:
            first = False            
        i = 0
        for element in row:
            if i>0:
                latex.write('&')
            tablesub(latex,element)
            i+=1
        latex.write('\\\\\n')
        

def table(latex,rawtableinfo,rawheader,rawcols,caption= '',columns =1,divider='|' ,label = False,place = 'htbp',borders = 'Minimal',align = 'c',maxrows = TABLETHRESHOLD,minrows = MINCONTTABLELENGTH):
    if columns == 1:
        tableinfo = rawtableinfo
        header = rawheader
        cols = rawcols
    else:
        tableinfo = multiplecolumnstableinfo(rawtableinfo,rawheader,columns)
        cols = multiplecolumnscols(rawcols,columns,divider)
    tablenny = len(tableinfo)
    headlenny = len(header)
    if headlenny + minrows > maxrows:
        raise Exception('cannot be made')
    if tablenny + headlenny <=maxrows:
        assignlabel = subtable(latex,tableinfo,header,cols,caption,columns,label,place,borders,align)
        return assignlabel
    q,r = divmod(tablenny,maxrows - headlenny)
    if r == 0:
        tables = q
        offset = 0 
    elif r < minrows:
        offset = int(math.ceil((minrows-r)/float(q)))
        tables = q+1
    elif r<=maxrows-headlenny:
        tables = q+1
        offset = 0
    else:
        raise Exception()
    t = maxrows - headlenny - offset
    assignlabel = subtable(latex,tableinfo[0:t],header,cols,caption,columns,label,place,borders,align)
    if tables>1:
        clear(latex)
    for i in range(1,tables):
        tinfo = tableinfo[t*i:t*(i+1)]
        if len(tinfo) < minrows:
            raise Exception()
        subtable(latex,tinfo,header,cols,caption,columns,label,place,borders,align,continued = True)
        clear(latex)
    return assignlabel




def toprule(latex,border,minimalhandle = True):
    bordersub(latex,border,'\\toprule\n',minimalhandle)

def midrule(latex,border,minimalhandle = True):
    bordersub(latex,border,'\\midrule\n',minimalhandle)

def bottomrule(latex,border,minimalhandle = True):
    bordersub(latex,border,'\\bottomrule\n',minimalhandle)

def bordersub(latex,border,string,minimalhandle):
    if border == False:
        pass
    elif border in ['all','All','ALL']:
        latex.write(string)
    elif border == True:
        latex.write(string)
    elif border == 'Minimal':
        if minimalhandle:
            latex.write(string)
    else:
        raise Exception(border)



    

def writeheader(latex,header,border):
    i = 0
    toprule(latex,border)
    for element in header:
        if i>0:
            latex.write('&')
        tablesub(latex,element)
        i+=1
    if border != False:
        midrule(latex,'all')
    

    



def stylise(latex,element,style):
    brackets = createstyle(latex,style)
    latex.write(clean(element))
    for i in range(0,brackets):
        latex.write('}')
    

def tablesub(latex,element):
    if type(element) in [type((0,0)),type([0,0])]:
        if len(element) == 0:
            return
        elif len(element) == 1:
            latex.write(clean(element[0]))
        else:
            stylise(latex,element[0],element[1])
    else:
        latex.write(clean(element))



def epsfig(latex,fname,width):
    latex.write('\\epsfig{file='+fname+',width='+width+'}')

def includegraphics(latex,fname,width):
    latex.write('\\includegraphics[width='+width+']{'+fname+'}')    


def getfiguretype(eps):
    #if eps:
    #    return epsfig
    return includegraphics


def getsublabel(sublab,lenny):
    if sublab in [None,'None',False]:
        sublabel = []
        for i in range(0,lenny):
            sublabel.append('')
        return sublabel
    if type(sublab) not in [type([]),type((1,2))]:
        raise Exception()
    if len(sublab)!=lenny:
        raise Exception()
    sublabel = []
    for lab in sublab:
        sublabel.append('\n\\label{'+lab+'}')
    return sublabel

def figure(latex,fnames,caption = None,label=False,sublabels = None,subcaptions=[],width=None,place='htbp',eps=False):
    '''
    formate:
    Caption is the caption
    fnames is a list of the files
    subcaptions is the list of the subcaptions
    options is the htbp
    '''
    figsubfunc = getfiguretype(eps)
    latex.write('\n')
    latex.write('\\begin{figure}[htbp]\n')
    latex.write('\\centering\n')
    if len(fnames)>1:
        if width==None:
            width = '0.48\\textwidth'
        if len(fnames)!=len(subcaptions):
            raise Exception()
        latex.write('{\n')
        sublabel = getsublabel(sublabels,len(fnames))
        for i in range(0,len(fnames)):
            latex.write('\\subfigure['+clean(subcaptions[i])+']{\n')
            figsubfunc(latex,fnames[i],width)
            latex.write('}'+sublabel[i]+'\n')
        latex.write('}\n')
    else:
        if width==None:
            width = '0.8\\textwidth'
        figsubfunc(latex,fnames[0],width)
        latex.write('\n')
    assignlabel = None
    if caption != None:
        latex.write('\\caption{'+clean(caption)+'}\n')
        assignlabel = writelabel(latex,caption,label,'fig')
    latex.write('\\end{figure}\n')
    latex.write('\n')
    return assignlabel

def createstyle(latex,style):
    brackets = 0 
    if 'b' in style:
        brackets+=1
        latex.write('\\textbf{')
    if 'i' in style:
        brackets+=1
        latex.write('\\textit{')
    if 's' in style:
        brackets+=1
        latex.write('\\textsc{')
    if '0' in style:
        brackets += 1
        latex.write('{\\tiny ')
    if '1' in style:
        brackets += 1
        latex.write('{\\scriptsize ')
    if '2' in style:
        brackets += 1
        latex.write('{\\small ')
    if '3' in style:
        brackets += 1
        latex.write('{\\normalsize ')
    if '4' in style:
        brackets += 1
        latex.write('{\\large ')
    if '5' in style:
        brackets += 1
        latex.write('{\\Large ')
    if '6' in style:
        brackets += 1
        latex.write('{\\LARGE ')
    if '7' in style:
        brackets += 1
        latex.write('{\\huge ')
    if '8' in style:
        brackets += 1
        latex.write('{\\Huge ')
    return brackets

def lwrite(latex,text,style='',size = None,skip=None,color=None):
    for char in ALIGNKEYS:
        if char in style:
            latex.write(ALIGNB[char])          
    brackets = 0
    if size!=None:
        brackets+=1
        latex.write('{\\'+size)
    brackets+=createstyle(latex,style)
    if color!=None:
        brackets+=1
        latex.write('\\textcolor{'+color+'}{')
    if brackets ==0 and skip!=None:
        brackets+=1
        latex.write('{')
    latex.write(clean(text))
    for i in range(0,brackets):
        latex.write('}')
    if skip!=None:
        latex.write('\\\\['+skip+']\n')
    for char in ALIGNKEYS:
        if char in style:
            latex.write(ALIGNE[char])
    
def getlabel(string):
    label = ''
    for char in string:
        if char.upper() in ALPHABET+NUMBERS:
            label+=char
    return label





def getnumstr(num):
    if num == True:
        return ''
    return '*'

def writeblock(latex,string,blockname,blockshort,label,skiptoc,num):
    numstr = getnumstr(num)
    latex.write('\n')
    if skiptoc:
        latex.write('\\addtocontents{toc}{\\SkipTocEntry}')
    latex.write('\\'+blockname+numstr+'{'+clean(string)+'}')
    assignedlabel = writelabel(latex,string,label,blockshort)
    latex.write('\\phantom{teehee}\\hspace{1cm}\n')
    return assignedlabel
    




def chapter(latex,string,label = False,skiptoc = False,num = True):
    return writeblock(latex,string,'chapter','chp',label,skiptoc,num)

def section(latex,string,label = False,skiptoc = False,num = True):
    return writeblock(latex,string,'section','sec',label,skiptoc,num)

def subsection(latex,string,label = False,skiptoc = False,num = True):
    return writeblock(latex,string,'subsection','ssc',label,skiptoc,num)

def subsubsection(latex,string,label = False,skiptoc = False,num=True):
    return writeblock(latex,string,'subsubsection','sss',label,skiptoc,num)




def writelabel(latex,string,label,obj):
    if label == False:
        latex.write('\n')
        return None
    if label==None:
        latex.write('\\label{'+obj + ':'+getlabel(string) + '}\n')
        return obj + ':'+getlabel(string)
    latex.write('\\label{'+str(label)+'}\n')
    return str(label)

def clear(latex):
    latex.write('\\clearpage\n')


