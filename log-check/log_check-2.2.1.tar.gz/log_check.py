# -*- coding: UTF-8 -*-

import sys, re, os

help = """
Usage:
    log_check [option] [paths|files]

Option:
    -S, -show_ok                show ok file.
    -H, -hide_ok                hide ok file, progress bar instead.
    -h, -help                   just show this.

Example:
    log_ckeck                   check all .cpp, .h, .hpp, .mm in `./`
    log_check ../crcp           check all .cpp, .h, .hpp, .mm in `../crcp`
    log_check main.cpp          check main.cpp
"""

g_unknow_logs = []

class Progress:
    def __init__(self, max = 100, width = 60):
        self.max = max
        self.width = width
        self.i = 0

    def next(self, info=None):
        self.i = self.i+1
        finished = int(self.i / self.max * self.width + 0.5) # 四舍五入
        rest = self.width - finished
        if info==None:
            bar = '|{}{}|{}/{}'.format('#'*finished, ' '*rest, self.i, self.max)
        else:
            bar = '|{}{}|{}/{}`{}`'.format('#'*finished, ' '*rest, self.i, self.max, info)
        print('\b'*len(bar), end='')
        print(bar, end='')


def getfiles(current_dir, types, files = []):
    dir_list = os.listdir(current_dir)
    for dir in dir_list:
        path = os.path.join(current_dir, dir)
        if os.path.isdir(path):
            getfiles(path, types, files)
        else:
            obs_path = current_dir + '/' + dir
            for type in types:
                if obs_path.endswith(type):
                    files.append(obs_path.replace('\\', '/'))
    return files


# return end_pos and arg_num
def parse(text, start_pos):
    left_braces = {'(', '[', '{'}
    right_braces = {')', ']', '}'}
    deep = 1
    i = start_pos
    arg_num = 0
    in_dou_quote = False
    in_sin_quote = False
    while deep!=0 and i<len(text):
        c = text[i]
        if c == '"':
            in_dou_quote = not in_dou_quote
        if c == "'":
            in_sin_quote = not in_sin_quote
        if not in_dou_quote and not in_sin_quote:
            if c in left_braces:
                deep = deep+1
            if c in right_braces:
                deep = deep-1
        if c == ',' and deep == 1 and not in_dou_quote and not in_sin_quote:
            arg_num = arg_num+1
        i = i+1
    end_pos = i+1
    if deep != 0:
        raise Exception('deep({}) error'.format(deep))
    if text[end_pos-1] != ';':
        raise Exception('parse error, not end with;')
    return (end_pos, arg_num)

def count_num_brace(per_log):
    first_quote_idx = per_log.find('\"')
    second_quote_idx = per_log.find('\"', first_quote_idx+1)
    if first_quote_idx == -1 or second_quote_idx == -1:
        raise Exception('num of `\"` < 2 : first_quote_idx = {}, second_quote_idx = {}'.format(first_quote_idx, second_quote_idx))

    format_str = per_log[first_quote_idx+1:second_quote_idx]
    res = re.findall(r'({.*?})', format_str)
    if res:
        return len(res)
    return 0


bad_log_fmt = """


{}
--------------------------------------------------------------
{} [line {}] : {{}} = {}, argc = {}
--------------------------------------------------------------"""

def check(files, show_ok):
    max_file_name_len = max([len(file_name) for file_name in files])

    bad_files = []

    if show_ok == None:
        show_ok = len(files) <= 128

    progress = Progress(max=len(files))

    for source_file in files:
        try:
            text = open(source_file, encoding='utf-8').read().replace('\\\"', '').replace('\\\'', '')
        except UnicodeDecodeError:
            print('\n can not read file `{}`'.format(source_file))
            continue
        iter = re.finditer('(LOG[T|D|I|W|E|C]\(.*?\n{0,}.*?\);)', text, re.MULTILINE)

        bad_logs = []
        log_len = 0
        for item in iter:
            log_len = log_len+1
            per_log = item.group()
            location = len(re.findall('\n', text[:item.start()])) + 1
            try:
                end_pos, num_arg = parse(text, item.start() + per_log.index(',')+1)
                if end_pos != item.end():
                    per_log = text[item.start():end_pos]
                
                num_brace = count_num_brace(per_log)
            except Exception as e:
                g_unknow_logs.append({'file':source_file, 'line':location, 'exception': e, 'log':per_log})
                continue
                
            if num_brace != num_arg:
                print(bad_log_fmt.format(per_log, source_file, location, num_brace, num_arg))
                bad_logs.append((per_log, num_brace, num_arg))
            
        space_num = max_file_name_len-len(source_file)
        if len(bad_logs) == 0:
            if show_ok:
                space_num = max_file_name_len-len(source_file)
                print('{}{} all {:2} LOGs ok'.format(source_file, ' '*space_num, log_len))
        else:
            print('{}{} {:2} bad LOGs total\n'.format(source_file, ' '*space_num, len(bad_logs)))
            bad_files.append({'source_file':source_file, 'bad_logs': bad_logs})
        
        if not show_ok:
            progress.next()

    print()
    print()
    print('({}/{})(badfile/total) {:3} bad LOG total'.format(len(bad_files), len(files), sum([len(bad_file['bad_logs']) for bad_file in bad_files])))
    print()
    print()
    print()
    print('{} unknown LOGs:'.format(len(g_unknow_logs)))
    for log in g_unknow_logs:
        print(log)

def main():
    if '-help' in sys.argv or '-h' in sys.argv:
        print(help)
        exit()

    default_types = ['.cpp', '.h', '.hpp', '.mm']
    show_ok = None
    show_ok_res = {
       '-S'       : True,
       '-show_ok' : True,
       '-H'       : False,
       '-hide_ok' : False,
    }
    for arg in show_ok_res:
        if arg in sys.argv:
            sys.argv.remove(arg)
            show_ok = show_ok_res[arg]
        
    if len(sys.argv) > 1:
        files = []
        for arg in sys.argv[1:]:
            if os.path.isdir(arg):
                files = files + getfiles(arg, default_types)
            elif os.path.isfile(arg):
                files.append(arg)
                print('{} is file'.format(arg))
            else:
                print('`{}` is not file or dir!!!', arg)
        check(files, show_ok)
    else:
        check(getfiles('./', default_types), show_ok)

if __name__ == "__main__":
    main()