import platform
if(platform.system()!='Windows'):
    raise Exception("\n\n[Error]: only support windows.")

from winshotor.screenshotor import *

"""
this util is aim to screenshot for window.

1.WinInfo(hwnd): contain the hwnd、rect、title of a window. Strongly suggest <ReadOnly>
2.WinInfor(): Get all windows info.
    wininfor = WinInfor()
    wininfor.Update()  # update for the lastest windows infos
    wininfor.GetWinInfos()  # read from the last update.
3.WinShotor(hwnd): screenshot for window.
    winshotor = WinShotor(hwnd)
    img = winshotor.SnapShot()  # get np.array object with shape (h, w, 4)  RGB + Alpha
"""
