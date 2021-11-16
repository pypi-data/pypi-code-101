import os
import shutil
import glob


# desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
# visual studio server commit


def copy_file_if_not_exists(src: str, dst: str):
    if (os.path.isfile(dst)):
        print(f'file {dst} already exists.. skipping')
    else:
        return copy_file(src, dst)


## temp fix -- delete backup files
def backup_file_and_replace(src: str, dst: str):
    if (os.path.isfile(dst + ".bak")):
        delete_file(dst + "bak")
        # print(f'file {dst} exists.. trying to backup')
        # backup_file(dst)
    return copy_file(src, dst)


def copy_file(src: str, dst: str):
    try:
        shutil.copy(src, dst)
        print(f"File {src} copied to {dst} successfully.")
        return True

    # If source and destination are same
    except shutil.SameFileError:
        print("Source and destination represents the same file.")

    # If there is any permission issue
    except PermissionError:
        print("Permission denied.")

    # For other errors
    except Exception as e:
        print(f"Error occurred while copying file. -- {e}")

    return False


def backup_file(dst: str):
    return copy_file_if_not_exists(dst, dst + ".bak")


def move_file(src: str, dst: str):
    copy_file(src, dst)
    delete_file(src)


def delete_file(src: str):
    try:
        os.remove(src)
    except:
        print(f'file {src} not found')