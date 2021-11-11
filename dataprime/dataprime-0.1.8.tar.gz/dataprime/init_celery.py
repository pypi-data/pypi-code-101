"""
Copyright (c) [Year] [name of copyright holder]
[Software Name] is licensed under Mulan PSL v2.
You can use this software according to the terms and conditions of the Mulan PSL v2.
You may obtain a copy of Mulan PSL v2 at:
         http://license.coscl.org.cn/MulanPSL2
THIS SOFTWARE IS PROVIDED ON AN "AS IS" BASIS, WITHOUT WARRANTIES OF ANY KIND,
EITHER EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO NON-INFRINGEMENT,
MERCHANTABILITY OR FIT FOR A PARTICULAR PURPOSE.
See the Mulan PSL v2 for more details.
"""
import os

from dataprime_celery import celery_app, tasks, config
import inspect


def create_files():
    """初始化celery工程文件"""
    if not os.path.exists("../dataprime_celery"):
        os.mkdir("../dataprime_celery")

    for module in [celery_app, tasks, config]:
        source_code = inspect.getsource(module)
        file_path = os.path.join(os.getcwd(), module.__name__).replace(".", "/") + ".py"
        print(f"creating file: {file_path}")

        with open(file_path, "w") as f:
            f.write(source_code)

    print("celery文件已生成, 使用以下命令启动worker:")
    print("celery -A dataprime_celery.celery_app worker -l INFO")


if __name__ == '__main__':
    pass








