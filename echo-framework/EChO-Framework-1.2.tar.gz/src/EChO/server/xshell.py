import paramiko


# 执行SSH指令
def do(host, p,  user, psw, cmd):
    # 定义SSH
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    # 执行远程命令并获取回复
    ssh.connect(hostname=host, port=p, username=user, password=psw)
    stdin, stdout, stderr = ssh.exec_command(cmd)

    # 处理回复内容
    result = stdout.read()

    if not result:
        result = stderr.read()
    ssh.close()

    return result.decode()
