import time
import pynvml
import smtplib 
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class GPUMoniter:
    def __init__(self, email_from, passwd, email_to, min_per_check=10, min_send_num=1):
        """
        arg:
            min_per_check: float-每隔多少分种检查一次
            min_send_num: int-当达到最低要求是发送邮件
            msg_from: str-发送的邮箱
            passwd: ste-邮箱的POP3/SMTP服务码
            msg_to: [str]-目标邮箱
        """
        self.pre_free_num = 0 # 上一次的情况 
        self.min_per_check=min_per_check
        self.min_send_num=min_send_num
        self.email_from=email_from
        self.passwd=passwd
        self.email_to=email_to
    
    def monitor(self):
        while True:
            cur_free_num = self.check_gpu()
            # 只有检查到达标时发送，检查垃圾邮件数目
            if self.pre_free_num < self.min_send_num  and cur_free_num >= self.min_send_num:
                self.send_emai(cur_free_num)
            self.pre_free_num = cur_free_num

            time.sleep(self.min_per_check * 60)
            
    def check_gpu(self):
        """检查gpu的显存使用情况，如果小于百分之2，认为是空的"""
        pynvml.nvmlInit()
        num_gpu = pynvml.nvmlDeviceGetCount()
        num_free = 0
        for i in range(num_gpu):
            handle = pynvml.nvmlDeviceGetHandleByIndex(i)
            meminfo = pynvml.nvmlDeviceGetMemoryInfo(handle)
            if meminfo.used / meminfo.total < 0.02:
                num_free += 1

        return num_free

    def send_emai(self, free_gpu_num):
        """发送邮件"""
        emali=MIMEMultipart()
        conntent=f"{time.strftime('%Y-%m-%d %H:%M:%S',  time.localtime())}----有{free_gpu_num}张GPU空闲"
        emali.attach(MIMEText(conntent, 'plain', 'utf-8'))
        emali['Subject']="GPU-通知" # 设置邮件主题
        emali['From']=self.email_from # 发送方
        
        try:
            s = smtplib.SMTP_SSL("smtp.qq.com", 465)
            s.login(self.email_from, self.passwd)
            s.sendmail(self.email_from, self.email_to, emali.as_string())
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S',  time.localtime())}----邮件发送成功")
        except:
            print(f"{time.strftime('%Y-%m-%d %H:%M:%S',  time.localtime())}----发送失败")