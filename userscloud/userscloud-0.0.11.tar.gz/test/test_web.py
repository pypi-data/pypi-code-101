import userscloud
import traceback


uc = userscloud.UC_WEB(debug=True)

try:
    # uc.register(["blackhole", "blackhole"], "blackhole@gmail.com")
    uc.login()

    # uc.delete_all_sessions()
    # input()
    # print(uc.get_api_key())
    # input()
    # uc.change_api_key()
    # input()
    # print(uc.get_all_folders())
    # uc.create_new_folder(uc.ROOT, "what")
    # print(uc.get_all_folders())
    # input()
    # link = uc.upload_remote_url(uc.ROOT, "https://pastebin.com/raw/sViuU9AN")
    # print(uc.list_folder(uc.ROOT))
    # print(link)
    # uc.delete_file(link.split("/")[-1])
    # print(uc.list_folder(uc.ROOT))
    # print(uc.list_trash())
    # files = uc.get_trash()
    # [print(file) for file in files]
    # uc.restore_file(files[0][1]["file_id"])
    # print(uc.list_folder(uc.ROOT))
    # input()
    # print(uc.list_folder(uc.ROOT))
    # print(uc.upload_copy_url('''https://userscloud.com/gfjrkeud5u38'''))
    # print(uc.list_folder(uc.ROOT))
    # input()

    root_folders, root_files = uc.get_folder(uc.ROOT)
    [print(folder) for folder in root_folders]

    # print(uc.list_folder(uc.ROOT))
    # print(uc.edit_folder(root_folders[-1][1]["fld_id"], "what 2", "?"))
    # print(uc.list_folder(uc.ROOT))
    # input()
    # print(uc.list_folder(uc.ROOT))
    # print(uc.delete_folder(root_folders[-1][2]["fld_id"], root_folders[-1][2]["del_folder"]))
    # print(uc.list_folder(uc.ROOT))
    # uc.create_new_folder(uc.ROOT, "what")
    # input()

    print(uc.list_folder(root_folders[0][1]["fld_id"]))
    folders, files = uc.get_folder(root_folders[0][1]["fld_id"])
    [print(file) for file in files]

    # print(uc.list_folder(root_folders[-1][1]["fld_id"]))
    # print(uc.copy_file(files[0][1], root_folders[0][1]["fld_id"], root_folders[-1][1]["fld_id"]))
    # print(uc.list_folder(root_folders[-1][1]["fld_id"]))
    # input()
    # sub_folders, sub_files = uc.get_folder(root_folders[-1][1]["fld_id"])
    # print(uc.list_folder(uc.ROOT))
    # print(uc.list_folder(root_folders[-1][1]["fld_id"]))
    # print(uc.move_file(sub_files[0][1], root_folders[-1][1]["fld_id"], uc.ROOT))
    # print(uc.list_folder(uc.ROOT))
    # print(uc.list_folder(root_folders[-1][1]["fld_id"]))
    # input()
    # [print(file) for file in root_files]
    # print(uc.list_folder(uc.ROOT))
    # print(uc.edit_file(root_files[0][3]["file_code"], "what shit b.mp4", "???", "pwd"))
    # print(uc.list_folder(uc.ROOT))
    # input()

    # link = uc.upload_file(root_folders[-1][1]["fld_id"], "/path/to/zip.zip")
    # print(link)
except:
    traceback.print_exc()


uc.logout()
