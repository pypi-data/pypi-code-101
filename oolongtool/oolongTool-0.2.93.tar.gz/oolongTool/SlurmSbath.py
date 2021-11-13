import os
import pexpect

#########################################################################
# 模版
class Template(object):
    def __init__(self):
        self.root = """#!/bin/bash
#SBATCH -n 4
#SBATCH --gres gpu:1
#SBATCH -p dell"""
        self.FileNameList = []
        ##########################################################################
        self.JOB_name = "Tune_0" # 显示在squeue中的名字
        self.log_name = "Tune_0.log" # 输出的log名字
        self.bash_name = "Tune_0.sh" # 输出的脚本的名字
        self.env = "TPAMI"
        self.work_dir = '.'
        self.bash_dir = '.'
        self.exec = "PLEASE CHANGE HERE"
        # 如果需要使用其他人账户 
        self.work_user = None
        self.work_password = None
        self.cur_user = None
        # self.init_text = "source /home/LAB/anaconda3/bin/activate TPAMI"  # 环境启动脚本
    
    def save(self, save=True, dir='.', using_other=False):
        dir = self.bash_dir
        self.email_title = self.JOB_name
        self.email_content = os.path.join(self.bash_dir, self.log_name) # 内容必须为文本文件
        root = self.root
        work_dir = 'cd ' + self.work_dir
        inputLog = "#SBATCH -o {}".format(self.log_name)
        sbatch = "#SBATCH -J {}".format(self.JOB_name)
        init_text = "source /home/LAB/anaconda3/bin/activate {}".format(self.env)
        # log_dir = 'cd ' + self.bash_dir
        if using_other:
            # 如果是采用他人账户，无需加上路径
            sendmail = "PostMessage -c {} -s {} -t mail".format(self.log_name, self.email_title)
        else:
            sendmail = "PostMessage -c {} -s {} -t mail".format(self.email_content, self.email_title)


        exec = self.exec
        File_name = self.bash_name
        self.__check()

        if using_other:
        # 如果使用他人的账户
            command = "\n".join([work_dir, init_text, exec])
            exec = f"ChangeUser -u {self.work_user} -p {self.work_password} -c \"{command}\""
            work_dir = ''
            init_text = ''

        text = (root + '\n' +
                inputLog + '\n' +
                sbatch + '\n' +
                work_dir + '\n' +
                init_text + '\n' +
                exec + '\n' +
                # log_dir + '\n' +
                sendmail)

        if save:
            if not os.path.exists(dir):
                os.makedirs(dir)
            with open(os.path.join(dir, File_name), 'w') as f:
                f.write(text)
                print(os.path.join(dir, File_name), " created!")
            assert File_name not in self.FileNameList, f"the {File_name} had been created!!!"
            self.FileNameList.append(File_name)

            if using_other:
                self.save_run_all_dataset(dir, user=self.cur_user)
                self.expand_permissions(self.bash_dir)
            else:
                self.save_run_all_dataset(dir)

        return File_name

    def save_run_all_dataset(self, dir='.', user=None):
        if user:
            with open(os.path.join(dir, f"run_all_dataset_{user[0]}.sh"), 'w') as f:
                text = ["sbatch " + x + "\n" for x in self.FileNameList]
                f.writelines(text)
        else:
            with open(os.path.join(dir, "run_all_dataset.sh"), 'w') as f:
                text = ["sbatch " + x + "\n" for x in self.FileNameList]
                f.writelines(text)
    
    def __check(self):
        assert self.log_name.endswith(".log"), "log must end with .log"
        assert self.bash_name.endswith(".sh"), "bash must end with .sh"
    
    def expand_permissions(self, _dir):
        # child = pexpect.spawn(f'cd {self.bash_dir}', encoding='utf-8')
        child = pexpect.spawn(f'chmod 777 -R {_dir}', encoding='utf-8')
    
        

    
