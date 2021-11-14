#####################
# Author: Yuki Sui
# Date: 2021-11-14
# Version: 1.2
#####################

import time
import os
from pathlib import Path


def create_log_folder(folder_name, hidden):
    dirs = '.\\logs\\'
    dirs2 = '.\\logs\\' + folder_name + '\\' + get_time('date') + '\\'
    dirs3 = str(Path.home()) + '\\.1o9f1y\\' + folder_name + '\\' + get_time('date') + '\\'
    if not os.path.exists(dirs):
        os.makedirs(dirs)
    else:
        pass
    if not os.path.exists(dirs2):
        os.makedirs(dirs2)
    if hidden == 'yes':
        if not os.path.exists(dirs3):
            os.makedirs(dirs3)
        else:
            pass
    else:
        pass


def get_time(flag):
    if flag == 'datetime':
        return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if flag == 'date':
        return time.strftime("%Y-%m-%d", time.localtime())
    if flag == 'times':
        return time.strftime("%H:%M:%S", time.localtime())
    if flag == 'datetimefile':
        return time.strftime("%Y%m%d%H%M%S", time.localtime())


def write_log(name, position, level, message, mode='add', folder_name='logflys', hidden='no'):
    global LOGFILE, LOGFILE2, logfolder, logfolder_hidden, LOGFILE_hidden
    if hidden == "no":
        logfolder = '.\\logs\\' + folder_name + '\\' + get_time('date') + '\\'
    elif hidden == 'yes':
        logfolder = '.\\logs\\' + folder_name + '\\' + get_time('date') + '\\'
        logfolder_hidden = str(Path.home()) + '\\.1o9f1y\\' + folder_name + '\\' + get_time('date') + '\\'
    if mode == 'add':
        LOGFILE_hidden = name + '-' + get_time('date') + '.log'
        LOGFILE = logfolder + name + '-' + get_time('date') + '.log'
    elif mode == 'new':
        LOGFILE_hidden = name + '-' + get_time('datetimefile') + '.log'
        LOGFILE = logfolder + name + '-' + get_time('datetimefile') + '.log'
    create_log_folder(folder_name, hidden)
    if position == 'CLI':
        print(name + ' ' + get_time('datetime') + ' ' + '[' + str.upper(level) + ']' + ' ' + message + '\r\n')
    if position == 'file':
        if mode == 'add':
            File = open(LOGFILE, 'a', newline='')
            File.write(get_time('datetime') + ' ' + '[' + str.upper(level) + ']' + ' ' + message + '\r\n')
            File.close()
            if hidden == 'yes':
                LOGFILE2 = logfolder_hidden + LOGFILE_hidden
                File = open(LOGFILE2, 'a', newline='')
                File.write(get_time('datetime') + ' ' + '[' + str.upper(level) + ']' + ' ' + message + '\r\n')
                File.close()
        elif mode == 'new':
            File = open(LOGFILE, 'w', newline='')
            File.write(get_time('datetime') + ' ' + '[' + str.upper(level) + ']' + ' ' + message + '\r\n')
            File.close()
            if hidden == 'yes':
                LOGFILE2 = logfolder_hidden + LOGFILE_hidden
                File = open(LOGFILE2, 'a', newline='')
                File.write(get_time('datetime') + ' ' + '[' + str.upper(level) + ']' + ' ' + message + '\r\n')
                File.close()
    if position == 'fileCLI':
        print(name + ' ' + get_time('datetime') + ' ' + '[' + str.upper(level) + ']' + ' ' + message + '\r\n')
        if mode == 'add':
            File = open(LOGFILE, 'a', newline='')
            File.write(get_time('datetime') + ' ' + '[' + str.upper(level) + ']' + ' ' + message + '\r\n')
            File.close()
            if hidden == 'yes':
                LOGFILE2 = logfolder_hidden + LOGFILE_hidden
                File = open(LOGFILE2, 'a', newline='')
                File.write(get_time('datetime') + ' ' + '[' + str.upper(level) + ']' + ' ' + message + '\r\n')
                File.close()
        elif mode == 'new':
            File = open(LOGFILE, 'w', newline='')
            File.write(get_time('datetime') + ' ' + '[' + str.upper(level) + ']' + ' ' + message + '\r\n')
            File.close()
            if hidden == 'yes':
                LOGFILE2 = logfolder_hidden + LOGFILE_hidden
                File = open(LOGFILE2, 'a', newline='')
                File.write(get_time('datetime') + ' ' + '[' + str.upper(level) + ']' + ' ' + message + '\r\n')
                File.close()


if __name__ == '__main__':
    write_log('Doctor Who', 'CLI', 'info', "this is Doctor's log, only in CLI.")
    write_log('Doctor Who', 'fileCLI', 'info', "this is Doctor's log, in file and CLI.", mode='add')
    write_log('Doctor Who', 'file', 'info', "this is Doctor's log, only in file.")
    write_log('Tardis', 'CLI', 'info', "this is Tardis's log, only in CLI.")
    write_log('Tardis', 'fileCLI', 'info', "this is Tardis's log, in file and CLI.")
    write_log('Tardis', 'file', 'info', "this is Tardis's log, only in file.")
    write_log('Death', 'fileCLI', 'info', "this is Death's log, in file and CLI.", mode='add', folder_name='death')

    write_log('Doctor Who', 'CLI', 'info', "this is Doctor's log, only in CLI.", hidden='yes')
    write_log('Doctor Who', 'fileCLI', 'info', "this is Doctor's log, in file and CLI.", mode='add', hidden='yes')
    write_log('Doctor Who', 'file', 'info', "this is Doctor's log, only in file.", hidden='yes')
    write_log('Tardis', 'CLI', 'info', "this is Tardis's log, only in CLI.", hidden='yes')
    write_log('Tardis', 'fileCLI', 'info', "this is Tardis's log, in file and CLI.", hidden='yes')
    write_log('Tardis', 'file', 'info', "this is Tardis's log, only in file.", hidden='yes')
    write_log('Death', 'fileCLI', 'info', "this is Death's log, in file and CLI.",
              mode='add', folder_name='death', hidden='yes')
