from omnitools import dt2yyyymmddhhmmss, IS_WIN32, getch, KEYS, sha3_512hd, getpw
from .utils import create_session, csm
from subprocess import call
from .api import ZS_API
from lxml import html
import traceback
import requests
import string
import copy
import os
import re


class ZS_FM(ZS_API):
    sortcols: dict = {
        "name": "name",
        "size": "size",
        "ttd": "dldate",
        "uploaded": "update",
        "viewed": "prv",
        "downloaded": "dls",
    }
    sortdirs: list = [
        "asc",
        "desc",
    ]
    cursor_pos: int = 0
    show_help: bool = True
    files_cache: dict = {}

    def __init__(self, *, debug = False):
        self.debug = debug
        self.s = create_session()

    def verify_hash(self, input: str) -> bool:
        if not input or not self.hash:
            return False
        return self.hash == sha3_512hd(sha3_512hd(sha3_512hd(input)))

    def get_filetable(self, page: int = 0, dir: int = 0, sortcol: str = "", sortdir: str = "", use_cache: bool = True) -> list:
        def append_files(_files):
            for file in _files:
                file_id = file.xpath("./@id")[0]
                if file_id == "add-folder":
                    continue
                is_dir = file_id.startswith("d")
                if is_dir:
                    file_id = file_id[1:]
                file_id = int(file_id)
                file_cell = file.xpath("./td[starts-with(@id, 'nametd')]/a")[0]
                file_name = file_cell.xpath("./text()")[0].strip()
                if not is_dir:
                    file_url = "https:"+file_cell.xpath("./@href")[0]
                    file_ttd = file.xpath("./td[7]/span/text()")[0].strip()
                    file_uploaded = file.xpath("./td[6]/text()")[0][:-2]
                    file_viewed = int(file.xpath("./td[4]/text()")[0].strip())
                    file_dl_ct = int(file.xpath("./td[5]/text()")[0].strip())
                    file_size = file.xpath("./td[3]/text()")[0].strip().split(" ")
                    file_size[0] = file_size[0].split(".")
                    file_size[0][-1] = file_size[0][-1][:2]
                    file_size[0] = ".".join(file_size[0])
                    file_size = " ".join(file_size)
                    has_pw = None
                    is_main = None
                    is_public = None
                    view = None
                else:
                    has_pw = False
                    is_public = False
                    is_main = False
                    view = None
                    file_uploaded = ""
                    file_viewed = ""
                    file_dl_ct = ""
                    file_url = self.domain+file.xpath("./td[8]/a/@href")[0]
                    stat = self.get_directory_stat(file_id)
                    file_ttd = "{} dirs".format(stat["dirs"]-1)
                    file_size = "{} files".format(stat["files"]-stat["dirs"]+1)
                    if len(file.xpath(".//*[contains(@src, 'key_delete')]")):
                        has_pw = True
                    if len(file.xpath(".//*[contains(@src, 'group_delete')]")):
                        is_public = True
                        if len(file.xpath(".//*[contains(@src, 'folder_table')]")):
                            view = 1
                        elif len(file.xpath(".//*[contains(@src, 'folder_image')]")):
                            view = 2
                        elif len(file.xpath(".//*[contains(@src, 'folder_audio')]")):
                            view = 3
                    if len(file.xpath("./td[2]//*[@class='upload_tip']")) > 1:
                        is_main = True
                data = [
                    file_id,
                    is_dir,
                    is_main,
                    has_pw,
                    is_public,
                    view,
                    file_uploaded,
                    file_viewed,
                    file_dl_ct,
                    file_name,
                    file_size,
                    file_ttd,
                    file_url,
                ]
                files.append(data)
        def get_files(page, dir, sortcol, sortdir):
            r = self.s.post(self.domain + "/fragments/myAccount/filetable.jsp", data={
                "page": int(page),
                "dir": int(dir),
                "sort": sortcol+sortdir,
            })
            if self.debug:
                print("get filetable", dir, page, sortcol, sortdir, r.status_code, len(r.content))
            if r.status_code != 200:
                raise Exception("cannot get filetable dir '{}' page '{}' sortcol '{}' sortdir '{}' due to status code '{}'\n{}".format(
                    dir, page, sortcol, sortdir,
                    r.status_code, r.content.decode()
                ))
            return html.fromstring(r.content.decode())
        if sortcol not in self.sortcols:
            raise ValueError("'{}' not in sortcols".format(sortcol))
        sortcol = self.sortcols[sortcol]
        if sortdir not in self.sortdirs:
            raise ValueError("'{}' not in sortdirs".format(sortdir))
        files = []
        _key = "{} {} {} {}".format(page, dir, sortcol, sortdir)
        if use_cache and _key in self.files_cache:
            return self.files_cache[_key]
        filetable = get_files(page, dir, sortcol, sortdir)
        append_files(filetable.xpath("//table//tr[@id]"))
        try:
            last_page = filetable.xpath("//*[contains(@onclick, 'browsePage')][last()]/text()")[0]
            last_page = int(last_page.strip()[0])
        except:
            return files
        for i in range(1, last_page):
            append_files(get_files(i, dir, sortcol, sortdir).xpath("//table//tr[@id]"))
        self.files_cache[_key] = files
        return files

    def print_files(self, dir, dir_name, sortcol, sortdir, files, pager_size, do_print) -> None:
        if self.cursor_pos < 0:
            self.cursor_pos = 0
        if self.cursor_pos > len(files)-1:
            self.cursor_pos = len(files)-1
        if not self.show_help:
            pager_size += 20
        max_i = 5
        files1 = copy.deepcopy(files)
        files = copy.deepcopy(files)
        if files:
            max_name = -1
            def view_to_txt(view):
                if view == 1:
                    return "folder"
                if view == 2:
                    return " audio"
                if view == 3:
                    return " table"
                return "      "
            for i in range(0, len(files1)):
                if files1[i][1]:
                    if files1[i][2]:
                        files1[i][-4] += " [main]"
                    files1[i][-4] = "[{}] [{}] [{}] {}".format(
                        "+pw" if files[i][3] else "-pw",
                        " public" if files[i][4] else "private",
                        view_to_txt(files[i][5]),
                        files1[i][-4],
                    )
                if len(files1[i][-4]) > max_name:
                    max_name = len(files1[i][-4])
            files1 = None
            for i in range(0, len(files)):
                if files[i][1]:
                    attr = ""
                    if files[i][2]:
                        attr += "[main] "
                    attr += "[{}] [{}] [{}]".format(
                        "+pw" if files[i][3] else "-pw",
                        " public" if files[i][4] else "private",
                        view_to_txt(files[i][5]),
                    )
                    files[i][-4] = "{}{}{}".format(files[i][-4], " "*(max_name-len(files[i][-4])-len(attr)), attr)
            if max_name < 9:
                max_name = 9
        else:
            max_name = 9
        max_size = 9
        max_ttd = 7
        max_uploaded = 19
        max_viewed = 6
        max_downloaded = 10
        #                    iiiii     <[x]>                     000.00 _B        00 Days        yyyy-mm-dd hh:mm:ss
        template_header = "   i+1   |  Check  |  {{:<{}}}{{}} |     Size  {{}} |    TTD  {{}} |        Uploaded     {{}} |  Viewed{{}} |  Downloaded{{}} ".format(
            max_name,
        )
        template = "<<"+">>|<<".join([
            "{{:>{}}}".format(max_i),
            "{{:>{}}}".format(5),
            "{{:<{}}}".format(max_name),
            "{{:>{}}}".format(max_size),
            "{{:>{}}}".format(max_ttd),
            "{{:>{}}}".format(max_uploaded),
            "{{:>{}}}".format(max_viewed),
            "{{:>{}}}".format(max_downloaded),
        ])+">>"
        template_sep = "--"+"--+--".join([
            "-"*max_i,
            "-"*5,
            "-"*max_name,
            "-"*max_size,
            "-"*max_ttd,
            "-"*max_uploaded,
            "-"*max_viewed,
            "-"*max_downloaded,
        ])+"--"
        offset = self.cursor_pos//pager_size
        lines = [template.format(
            offset*pager_size+i+1,
            "  {}  ".format(
                "*" if files[offset*pager_size+i] in self.checked_files else ("*" if file[1] and offset*pager_size+i == self.cursor_pos else " "),
            ),
            file[-4],
            file[-3],
            file[-2],
            file[-7],
            file[-6],
            file[-5],
        ).replace(
            ">>",
            "> " if offset*pager_size+i == self.cursor_pos else "  ",
        ).replace(
            "<<",
            " <" if offset*pager_size+i == self.cursor_pos else "  ",
        ) for i, file in enumerate(files[offset*pager_size:offset*pager_size+pager_size])]
        title = "~~ zippyshare file manager {} ~~"
        pager_info = "[dir '{}' ({})]   [checked {} file(s)]".format(
            dir_name,
            dir,
            len(self.checked_files),
        )
        title = title.format(pager_info)
        if not do_print:
            return
        if IS_WIN32:
            os.system("cls")
        else:
            os.system("clear")
        print(" "*((len(template_sep)-len(title))//2)+title)
        # print(" "*((len(template_sep)-len(pager_info))//2)+pager_info)
        print()
        print(template_sep)
        sortcol_i = list(self.sortcols.keys()).index(sortcol)
        print(template_header.format(
            "File Name",
            ("^" if sortdir == "asc" else "v") if sortcol_i == 0 else " ",
            ("^" if sortdir == "asc" else "v") if sortcol_i == 1 else " ",
            ("^" if sortdir == "asc" else "v") if sortcol_i == 2 else " ",
            ("^" if sortdir == "asc" else "v") if sortcol_i == 3 else " ",
            ("^" if sortdir == "asc" else "v") if sortcol_i == 4 else " ",
            ("^" if sortdir == "asc" else "v") if sortcol_i == 5 else " ",
        ))
        print(template_sep)
        if files:
            print("\n".join(lines))
            fs = len(files[offset*pager_size:offset*pager_size+pager_size])
            if fs < pager_size:
                for _ in range(0, pager_size-fs):
                    print(template.format("", "", "", "", "", "", "", "").replace("<<", "  ").replace(">>", "  "))
        else:
            half = pager_size // 2
            if pager_size%2 == 0:
                half -= 1
            for _ in range(0, half):
                print(template.format("", "", "", "", "", "", "", "").replace("<<", "  ").replace(">>", "  "))
            print(template.format("", "", "", "", "~empty~", "", "", "").replace("<<", "  ").replace(">>", "  "))
            for _ in range(0, pager_size//2):
                print(template.format("", "", "", "", "", "", "", "").replace("<<", "  ").replace(">>", "  "))
        files = None
        print(template_sep)
        print()
        if self.show_help:
            print('''\
                        [    Keys    ]\t[    Operations    ]
                                   H  \t  Show this menu
                                   F  \t  Filter items in current directory
                                   S  \t  Sort current directory
                                   O  \t  Order current directory
                                  F1  \t  Change view for highlighted directory
                                  F2  \t  Rename highlighted file or directory
                                  F3  \t  Set/Unset password for highlighted directory
                                  F4  \t  Toggle public/private for highlighted directory
                                  F5  \t  Refresh current directory
                                  F6  \t  Set highlighted directory as main directory
                                  F7  \t  Create directory at current directory
                                  F8  \t  Move checked files to current directory
                                  F9  \t  Save links for checked files
                                 F10  \t  Save file names and links for checked files
                              Delete  \t  Delete checked files or highlighted directory
                               Enter  \t  open highlighted file or directory link
                           Backspace  \t  Go to parent directory
    Up/Down/PageUp/PageDown/Home/End  \t  Navigate keys
          Space/Ctrl+<navigate keys>  \t  Check/Uncheck files or enter directory
                              Escape  \t  Uncheck all files
                         Ctrl+Delete  \t  Delete credentials if exported
                              Ctrl+C  \t  Exit''')
            print()

    def file_manager(
            self,
            dir: int = 0, dir_name: str = "root", prev_dir: int = 0,
            sortcol: str = "uploaded", sortdir: str = "desc",
            pager_size: int = 20
    ) -> bool:
        self.cursor_pos = 0
        files = self.get_filetable(dir=dir, sortcol=sortcol, sortdir=sortdir)
        key_pressed = None
        message = ""
        dir_unchanged = True
        if dir != 0:
            message = "Entered directory '{}'.".format(dir_name)
        while True:
            self.print_files(dir, dir_name, sortcol, sortdir, files, pager_size, True)
            if self.debug:
                if "Key pressed" in message:
                    message = "\n".join(_ for _ in message.splitlines() if "Key pressed" not in _)
                message += "\n      Key pressed: {}".format(key_pressed)
            print("    [    Message    ]\n      {}".format(message))
            if files:
                file = files[self.cursor_pos]
                is_dir = file[1]
            else:
                file = None
                is_dir = None
            key_pressed = getch()
            try:
                if key_pressed in [KEYS.S, KEYS.s]:
                    sortcol = input("    Enter sort column [{}]: ".format("'"+"', '".join(self.sortcols.keys())+"'"))
                    if sortcol not in self.sortcols:
                        sortcol = ""
                        message = "Failed to sort table. Reason: Incorrect sort column."
                        continue
                    files = self.get_filetable(dir=dir, sortcol=sortcol, sortdir=sortdir)
                    message = "Sorted table."
                elif key_pressed in [KEYS.O, KEYS.o]:
                    sortdir = input("    Enter sort order ['asc', 'desc']: ")
                    if sortdir not in self.sortdirs:
                        sortdir = ""
                        message = "Failed to sort table. Reason: Incorrect sort order."
                        continue
                    files = self.get_filetable(dir=dir, sortcol=sortcol, sortdir=sortdir)
                    message = "Sorted table."
                elif key_pressed in [KEYS.F, KEYS.f]:
                    kw = input("    Enter keyword or regular expression: ")
                    if kw:
                        try:
                            kw = re.compile(kw, flags=re.IGNORECASE)
                            key = lambda x: kw.search(x)
                        except:
                            key = lambda x: kw.lower() in x.lower()
                    else:
                        message = "Failed to filter items. Reason: Empty keyword or try F5."
                        continue
                    files = [file for file in files if key(file[-4])]
                    message = "Filtered items in current directory."
                elif key_pressed in [KEYS.H, KEYS.h]:
                    self.show_help = not self.show_help
                elif key_pressed == KEYS.CTRL_DEL:
                    confirmation = input("    Are you sure to deleted credentials? ['yes'] ".format(file[-4]))
                    if confirmation.lower() != "yes":
                        message = "Failed to deleted credentials. Reason: Confirmation is not 'yes'.".format(file[-4])
                        continue
                    csm.delete_credentials()
                    message = "Deleted credentials."
                elif key_pressed == KEYS.CTRL_C:
                    return True
                elif key_pressed == KEYS.F1:
                    if not file:
                        continue
                    view = input("    Enter view for directory '{}' ['1': folder; '2': audio; '3': table]: ".format(file[-4]))
                    if view not in ["1", "2", "3"]:
                        message = "Failed to change view for directory '{}'. Reason: Incorrect view.".format(file[-4])
                        continue
                    self.set_directory_view(file[0], int(view)-1)
                    files = self.get_filetable(dir=dir, sortcol=sortcol, sortdir=sortdir, use_cache=False)
                    message = "Changed directory '{}' view.".format(file[-4])
                elif key_pressed == KEYS.F2:
                    if not file:
                        continue
                    name = file[-4]
                    what = "directory" if is_dir else "file"
                    newname = input("    New name of {} '{}' (cannot modify extension): ".format(what, name))
                    if not newname:
                        message = "Failed to rename {} '{}' to '{}'. Reason: Empty name.".format(what, name, newname)
                        continue
                    if name == newname:
                        message = "Failed to rename {} '{}' to '{}'. Reason: Same name.".format(what, name, newname)
                        continue
                    if any(_ not in string.printable for _ in newname):
                        message = "Failed to rename {} '{}' to '{}'. Reason: Unprintable characters found.".format(what, name, newname.encode())
                        continue
                    if is_dir:
                        self.rename_directory(newname, file[0])
                    else:
                        self.rename_file(newname, file[0])
                    files = self.get_filetable(dir=dir, sortcol=sortcol, sortdir=sortdir, use_cache=False)
                    message = "Renamed {} '{}' to '{}'.".format(what, name, newname)
                elif key_pressed == KEYS.F3:
                    if not file:
                        continue
                    if not is_dir:
                        message = "Failed to set directory password. Reason: Cannot set file password."
                        continue
                    has_pw = file[3]
                    if has_pw:
                        confirmation = input("    Are you sure to unset directory '{}' password? ['yes'] ".format(file[-4]))
                        if confirmation.lower() != "yes":
                            message = "Failed to unset directory '{}' password. Reason: Confirmation is not 'yes'.".format(file[-4])
                            continue
                        self.set_directory_pw(file[0])
                        message = "Unset directory '{}' password.".format(file[-4])
                    else:
                        pw = getpw("    Enter password for directory '{}': ".format(file[-4]))
                        if not pw:
                            message = "Failed to set directory '{}' password. Reason: Empty password.".format(file[-4])
                            continue
                        print()
                        if pw != getpw("    Confirm password for directory '{}': ".format(file[-4])):
                            message = "Failed to set directory '{}' password. Reason: Password does not match.".format(file[-4])
                            continue
                        if any(_ not in string.printable for _ in pw):
                            message = "Failed to set directory '{}' password. Reason: Unprintable characters found.".format(file[-4])
                            continue
                        self.set_directory_pw(file[0], pw)
                        message = "Set directory '{}' password.".format(file[-4])
                    files = self.get_filetable(dir=dir, sortcol=sortcol, sortdir=sortdir, use_cache=False)
                elif key_pressed == KEYS.F4:
                    if not file:
                        continue
                    if not is_dir:
                        message = "Failed to set directory access. Reason: Cannot set file access."
                        continue
                    self.set_directory_access(file[0], not file[4])
                    files = self.get_filetable(dir=dir, sortcol=sortcol, sortdir=sortdir, use_cache=False)
                    message = "Toggled directory '{}' access.".format(file[-4])
                elif key_pressed == KEYS.F5:
                    files = self.get_filetable(dir=dir, sortcol=sortcol, sortdir=sortdir, use_cache=False)
                    message = "Refreshed current directory."
                elif key_pressed == KEYS.F6:
                    if not file:
                        continue
                    if not is_dir:
                        message = "Failed to set main directory. Reason: Cannot set file as main directory."
                        continue
                    confirmation = input("    Are you sure to set directory '{}' as main directory? ['yes'] ".format(file[-4]))
                    if confirmation.lower() != "yes":
                        message = "Failed to set directory '{}' as main directory. Reason: Confirmation is not 'yes'.".format(file[-4])
                        continue
                    self.set_main_directory(file[0])
                    message = "Set directory '{}' as main directory.".format(file[-4])
                    files = self.get_filetable(dir=dir, sortcol=sortcol, sortdir=sortdir, use_cache=False)
                elif key_pressed == KEYS.F7:
                    name = input("    Name of directory: ") or "New folder {}".format(dt2yyyymmddhhmmss())
                    if any(_ not in string.printable for _ in name):
                        message = "Failed to create directory '{}'. Reason: Unprintable characters found.".format(name.encode())
                        continue
                    self.create_directory(name, dir)
                    dir_unchanged = False
                    files = self.get_filetable(dir=dir, sortcol=sortcol, sortdir=sortdir, use_cache=False)
                    message = "Created directory '{}'.".format(name)
                elif key_pressed == KEYS.F8:
                    if not self.checked_files:
                        message = "Failed to move files to current directory. Reason: Empty checked files."
                        continue
                    confirmation = input("    Are you sure to move {} files to current directory? ['yes'] ".format(len(self.checked_files)))
                    if confirmation.lower() != "yes":
                        message = "Failed to move {} files to current directory. Reason: Confirmation is not 'yes'.".format(len(self.checked_files))
                        continue
                    self.move_files(dir)
                    dir_unchanged = False
                    message = "Moved {} files.".format(len(self.checked_files))
                    self.checked_files.clear()
                    files = self.get_filetable(dir=dir, sortcol=sortcol, sortdir=sortdir, use_cache=False)
                elif key_pressed == KEYS.F9:
                    if not self.checked_files:
                        message = "Failed to save links. Reason: Empty checked files."
                        continue
                    fn = "saved_links_{}.txt".format(dt2yyyymmddhhmmss())
                    open(fn, "wb").write(
                        ("\n".join(_[-1] for _ in self.checked_files)).encode()
                    )
                    message = "Saved links to file '{}'.".format(fn)
                elif key_pressed == KEYS.F10:
                    if not self.checked_files:
                        message = "Failed to save links. Reason: Empty checked files."
                        continue
                    delimiter = input("    Enter delimiter between name and link [default: '\\n']: ") or "\n"
                    delimiter = delimiter.replace("\\n", "\n").replace("\\r", "\r")
                    if any(_ not in string.printable for _ in delimiter):
                        delimiter = "\n"
                    fn = "saved_links_{}.txt".format(dt2yyyymmddhhmmss())
                    open(fn, "wb").write(
                        ("\n".join("{}{}{}".format(_[-4], delimiter, _[-1]) for _ in self.checked_files)).encode()
                    )
                    message = "Saved links to file '{}'.".format(fn)
                elif key_pressed == KEYS.DEL:
                    if not file:
                        continue
                    if is_dir:
                        what = "directory '{}'".format(file[-4])
                    else:
                        if not self.checked_files:
                            message = "Failed to delete file(s). Reason: Check file(s) first before delete."
                            continue
                        what = "{} files".format(len(self.checked_files))
                    if not self.verify_hash(getpw("    Enter password to delete {}: ".format(what))):
                        message = "Failed to delete {}. Reason: Password hash does not match.".format(what)
                        continue
                    if is_dir:
                        self.delete_directory("d{}".format(file[0]))
                    else:
                        self.delete_files()
                        self.checked_files.clear()
                    dir_unchanged = False
                    files = self.get_filetable(dir=dir, sortcol=sortcol, sortdir=sortdir, use_cache=False)
                    message = "Deleted {}.".format(what)
                elif key_pressed == KEYS.ESC:
                    message = "Unchecked {} files.".format(len(self.checked_files))
                    self.checked_files.clear()
                elif key_pressed == KEYS.BACKSPACE:
                    if prev_dir != dir:
                        if dir_unchanged:
                            return None
                        else:
                            return False
                    else:
                        message = "Failed to go to parent directory. Reason: Current directory is root."
                elif key_pressed == KEYS.ENTER:
                    if not file:
                        continue
                    url = file[-1]
                    if IS_WIN32:
                        os.startfile(url)
                    else:
                        call(["xdg-open", url])
                    message = "Opened highlighted file or directory link."
                elif key_pressed == KEYS.UP:
                    self.cursor_pos -= 1
                    message = "Moved up 1 item."
                elif key_pressed == KEYS.PGUP:
                    self.cursor_pos -= 10
                    message = "Moved up 10 items."
                elif key_pressed == KEYS.DOWN:
                    self.cursor_pos += 1
                    message = "Moved down 1 item."
                elif key_pressed == KEYS.PGDN:
                    self.cursor_pos += 10
                    message = "Moved down 10 items."
                elif key_pressed == KEYS.HOME:
                    self.cursor_pos = -1
                    message = "Moved to the start."
                elif key_pressed == KEYS.END:
                    self.cursor_pos = 999999999
                    message = "Moved to the end."
                elif key_pressed == KEYS.SPACE:
                    if not file:
                        continue
                    if not is_dir:
                        if file in self.checked_files:
                            self.checked_files.remove(file)
                        else:
                            self.checked_files.append(file)
                        message = "Toggled {} item.".format(1)
                    else:
                        prev_cursor_pos = self.cursor_pos
                        r = self.file_manager(
                            dir=file[0],
                            dir_name=file[-4],
                            prev_dir=dir,
                            sortcol=sortcol,
                            sortdir=sortdir,
                            pager_size=pager_size,
                        )
                        if r:
                            return True
                        for i in range(0, len(files)):
                            if files[i][0] == file[0]:
                                stat = self.get_directory_stat(file[0])
                                files[i][-2] = "{} dirs".format(stat["dirs"]-1)
                                files[i][-3] = "{} files".format(stat["files"]-stat["dirs"]+1)
                                break
                        if r is False:
                            dir_unchanged = False
                            self.get_filetable(dir=file[0], sortcol=sortcol, sortdir=sortdir, use_cache=False)
                        message = "Leaved directory '{}'.".format(file[-4])
                        self.cursor_pos = prev_cursor_pos
                elif key_pressed in [KEYS.CTRL_UP, KEYS.CTRL_PGUP, KEYS.CTRL_HOME]:
                    if not file:
                        continue
                    if not is_dir:
                        ct = 0
                        last = 1
                        if key_pressed == KEYS.CTRL_PGUP:
                            last = 10
                        if key_pressed == KEYS.CTRL_HOME:
                            last = 999999999
                        for i in range(0, last):
                            file = files[self.cursor_pos]
                            if file[1]:
                                break
                            if file in self.checked_files:
                                self.checked_files.remove(file)
                            else:
                                self.checked_files.append(file)
                            ct += 1
                            self.cursor_pos -= 1
                            cursor_pos = self.cursor_pos
                            self.print_files(dir, dir_name, sortcol, sortdir, files, pager_size, False)
                            if cursor_pos < 0:
                                break
                        message = "Toggled {} items.".format(ct)
                elif key_pressed in [KEYS.CTRL_DOWN, KEYS.CTRL_PGDN, KEYS.CTRL_END]:
                    if not file:
                        continue
                    if not is_dir:
                        ct = 0
                        last = 1
                        if key_pressed == KEYS.CTRL_PGDN:
                            last = 10
                        if key_pressed == KEYS.CTRL_END:
                            last = 999999999
                        for i in range(0, last):
                            file = files[self.cursor_pos]
                            if file[1]:
                                break
                            if file in self.checked_files:
                                self.checked_files.remove(file)
                            else:
                                self.checked_files.append(file)
                            ct += 1
                            self.cursor_pos += 1
                            cursor_pos = self.cursor_pos
                            self.print_files(dir, dir_name, sortcol, sortdir, files, pager_size, False)
                            if cursor_pos >= len(files):
                                break
                        message = "Toggled {} items.".format(ct)
            except requests.exceptions.RequestException as e:
                message = "Failed to perform operation '{}'. Reason: {}({})".format(key_pressed, e.__class__.__name__, e.args)
                if self.debug:
                    traceback.print_exc()
            except Exception as e:
                message = "Failed to perform operation '{}'. Reason: {}({})".format(key_pressed, e.__class__.__name__, e.args)
                if self.debug:
                    traceback.print_exc()


