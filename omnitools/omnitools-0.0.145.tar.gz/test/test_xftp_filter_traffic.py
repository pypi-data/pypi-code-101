from omnitools import FTPESS, FTPESC, FTPS_ThrottledDTPHandler_Base, logger, FTPMS_Exception
import threading
import magic
import os


class tmp(FTPS_ThrottledDTPHandler_Base):
    def alter_recv(self, chunk):
        if not hasattr(self, "bytes_read"):
            self.bytes_read = b""
        inspect_first_n_bytes = 1024*10
        self.bytes_read += chunk
        if len(self.bytes_read) >= inspect_first_n_bytes:
            mime_type = magic.from_buffer(self.bytes_read, mime=True).split("/")
            self.bytes_read = None
            if "octet-stream" != mime_type[1]:
                print(
                    self.file_obj.name,
                    mime_type
                )
                if any(_ in mime_type[1] for _ in ["rar", "zlib", "7z"]):
                    self.file_obj.close()
                    os.remove(self.file_obj.name)
                    self._resp = ("426 {}; transfer aborted.".format("Forbidden file type"), logger.warning)
                    raise FTPMS_Exception
        return chunk


s = FTPESS()
s.server.max_cons_per_ip = 2
s.handler.dtp_handler.alter_recv = tmp.alter_recv
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
    c.storbinary("STOR test{}.rar".format(i), open("/path/to/zip.7z", "rb"))
    c.quit()
    c.close()
for i in range(0, 1):
    p = threading.Thread(target=job, args=(i,))
    p.daemon = True
    p.start()
    pass

input()
s.safe_stop()
