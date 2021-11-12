from ftplib import FTP_TLS, FTP
from pyftpdlib.servers import ThreadedFTPServer
from pyftpdlib.handlers import TLS_FTPHandler, FTPHandler
import ssl


class FTPS_Base:
    handler = None
    server = None

    def __init__(self, addr: str = "127.0.0.1", port: int = 8021):
        if type(self) is FTPS_Base:
            raise NotImplementedError
        self.addr = addr
        self.port = port
        self.server = ThreadedFTPServer

    def configure(self):
        self.s = self.server((self.addr, self.port), self.handler)

    def start(self):
        self.s.serve_forever()

    def __del__(self):
        self.stop()

    def stop(self):
        self.s.close()
        self.s.close_all()

    def safe_stop(self):
        self.s.close_when_done()
        self.s.close_all()



class FTPESS(FTPS_Base):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.handler: TLS_FTPHandler = type("Handler", (TLS_FTPHandler,), {})
        self.handler.passive_ports = range(50100, 51100)


class FTPS(FTPS_Base):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.handler: FTPHandler = type("Handler", (FTPHandler,), {})
        self.handler.passive_ports = range(50100, 51100)


class FTPESC(FTP_TLS):
    trust_server_pasv_ipv4_address = True


class FTPSC(FTP_TLS):
    trust_server_pasv_ipv4_address = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._sock = None

    @property
    def sock(self):
        return self._sock

    @sock.setter
    def sock(self, value):
        if value is not None and not isinstance(value, ssl.SSLSocket):
            value = self.context.wrap_socket(value)
        self._sock = value

    def ntransfercmd(self, cmd, rest=None):
        conn, size = FTP.ntransfercmd(self, cmd, rest)
        conn = self.sock.context.wrap_socket(
            conn, server_hostname=self.host, session=self.sock.session
        )
        return conn, size

    def storbinary(self, cmd, fp, blocksize=8192, callback=None, rest=None):
        self.voidcmd('TYPE I')
        with self.transfercmd(cmd, rest) as conn:
            while 1:
                buf = fp.read(blocksize)
                if not buf:
                    break
                conn.sendall(buf)
                if callback:
                    callback(buf)
        return self.voidresp()


