import platform
if(platform.system()!='Windows'):
    raise Exception("\n\n[Error]: only support windows.")

from uploadtool.upload import UploadTool


"""
这个小工具允许你便捷的在Lib/site-package下编写你的库(一般在这个目录下不能build，会报错。)
1. 在合适的位置准备一个文件夹
2. 在文件夹内创建setup.py
3. 在文件夹内创建一个任意名称的py文件，里面这样写:
# -------------------------------------------------------
from uploadtool import *

# 要和setup.py里面的package name一致
ut = UploadTool("你的包的名称", "你的pypi账号", "你的pypi密码")
ut.Upload()  # 也可以用ut()

# --------------------------------------------------
工作原理:
	1.删除当前目录中过时的文件夹
	2.拷贝Lib/site-package下特定名称的库(你可以直接在Lib/site-package下编写此库)到目录下
	3.python -m build
	4.twine upload(如果不传入账号和密码，那么在上传时会要求你输入账号和密码.)

"""


"""
This gadget allows you to easily write your library under lib / site package (generally, you can't build in this directory, and an error will be reported.)
1. Prepare a folder in the appropriate location
2. Create setup.py in the folder
3. Create a py file with any name in the folder, which reads:
# -------------------------------------------------------
from uploadtool import *

# It should be consistent with the package name in setup.py
ut = UploadTool("your package name", "your pypi count", "your pypi password")
ut.Upload()  # you can use ut() instead of it.
# --------------------------------------------------
working principle:
	1. Delete obsolete folders in the current directory
	2. Copy the library with a specific name under lib / site package (you can write this library directly under lib / site package) to the directory
	3.python -m build
	4. Twin upload (if you don't pass in the account and password, you will be asked to enter the account and password when uploading.)
"""

