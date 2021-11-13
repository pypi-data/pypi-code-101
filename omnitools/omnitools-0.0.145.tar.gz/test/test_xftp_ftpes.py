from omnitools import FTPESS, FTPESC
import threading


s = FTPESS()
s.server.max_cons_per_ip = 2
s.handler.authorizer.add_anonymous('C:\\tmp', perm="elradfmwMT")
s.handler.certfile = "/path/to/cert.pem"
s.handler.tls_control_required = True
s.handler.tls_data_required = True
s.configure()
p = threading.Thread(target=s.start)
p.daemon = True
p.start()


def job(i):
    c = FTPESC(timeout=5)
    while True:
        try:
            c.connect("127.0.0.1", 8021)
            break
        except:
            import time
            time.sleep(1)
    c.login()
    c.prot_p()
    # c.dir()
    import io
    c.storlines("STOR test{}.txt".format(i), io.BytesIO(b"hii\r\n"*9))
    result = []
    c.retrbinary("RETR test{}.txt".format(i), lambda x: result.append(x))
    print(result)
    c.quit()
    c.close()
for i in range(0, 1):
    p = threading.Thread(target=job, args=(i,))
    p.daemon = True
    p.start()

input()
s.safe_stop()
