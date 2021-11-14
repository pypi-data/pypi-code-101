from ftplib import FTP_TLS as _FTP_TLS, FTP as FTPC, Error, B_CRLF, _SSLSocket
from pyftpdlib.servers import ThreadedFTPServer
from pyftpdlib.handlers import TLS_FTPHandler, FTPHandler, ThrottledDTPHandler, TLS_DTPHandler, RetryError, _FileReadWriteError, logger
from .xtrace import successstacks
import socket
import ssl


class FTPMS_Exception(Exception):
    pass


class FTP_ThrottledDTPHandler_Base(ThrottledDTPHandler):
    def alter_send(self, data: bytes):
        return data

    def alter_recv(self, chunk: bytes):
        return chunk

    def send(self, data):
        if any("FTPHandler.ftp_" in _ for _ in successstacks()):
            data = self.alter_send(data)
        return super(FTP_ThrottledDTPHandler_Base, self).send(data)

    def handle_read(self):
        try:
            chunk = self.recv(self.ac_in_buffer_size)
            if chunk:
                try:
                    chunk = self.alter_recv(chunk)
                    if not chunk:
                        raise ValueError
                except ValueError:
                    return self.close()
                except FTPMS_Exception:
                    return self.close()
        except RetryError:
            pass
        except socket.error:
            self.handle_error()
        else:
            self.tot_bytes_received += len(chunk)
            if not chunk:
                self.transfer_finished = True
                return
            if self._data_wrapper is not None:
                chunk = self._data_wrapper(chunk)
            try:
                self.file_obj.write(chunk)
            except OSError as err:
                raise _FileReadWriteError(err)

    handle_read_event = handle_read


class FTPS_ThrottledDTPHandler_Base(FTP_ThrottledDTPHandler_Base, TLS_DTPHandler):
    pass


class FTPS_Base:
    handler = None
    server = None
    s = None

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
        self.handler: TLS_FTPHandler = type("FTPESS_TLS_FTPHandler", (TLS_FTPHandler,), dict(
            dtp_handler=type("FTPESS_ThrottledDTPHandler", (FTPS_ThrottledDTPHandler_Base, ), {})
        ))
        self.handler.passive_ports = range(50100, 51100)


class FTPS(FTPS_Base):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.handler: FTPHandler = type("FTPS_FTPHandler", (FTPHandler,), dict(
            dtp_handler=type("FTPS_ThrottledDTPHandler", (FTP_ThrottledDTPHandler_Base,), {})
        ))
        self.handler.passive_ports = range(50100, 51100)


class FTP_TLS(_FTP_TLS):
    def __init__(self, *args, unwrap_sslsocket_after_completed_transfer: bool = True, **kwargs):
        self.unwrap_sslsocket_after_completed_transfer = unwrap_sslsocket_after_completed_transfer
        super().__init__(*args, **kwargs)

    def storlines(self, cmd, fp, callback=None):
        self.voidcmd('TYPE A')
        with self.transfercmd(cmd) as conn:
            while 1:
                buf = fp.readline(self.maxline + 1)
                if len(buf) > self.maxline:
                    raise Error("got more than %d bytes" % self.maxline)
                if not buf:
                    break
                if buf[-2:] != B_CRLF:
                    if buf[-1] in B_CRLF: buf = buf[:-1]
                    buf = buf + B_CRLF
                try:
                    conn.sendall(buf)
                except ssl.SSLError:
                    pass
                except ConnectionResetError:
                    pass
                if callback:
                    callback(buf)
            if self.unwrap_sslsocket_after_completed_transfer:
                try:
                    if _SSLSocket is not None and isinstance(conn, _SSLSocket):
                        conn.unwrap()
                except ssl.SSLError:
                    pass
                except FileNotFoundError:
                    pass
        return self.voidresp()

    def storbinary(self, cmd, fp, blocksize=8192, callback=None, rest=None):
        self.voidcmd('TYPE I')
        with self.transfercmd(cmd, rest) as conn:
            while 1:
                buf = fp.read(blocksize)
                if not buf:
                    break
                try:
                    conn.sendall(buf)
                except ssl.SSLError:
                    pass
                except ConnectionResetError:
                    pass
                if callback:
                    callback(buf)
            if self.unwrap_sslsocket_after_completed_transfer:
                try:
                    if _SSLSocket is not None and isinstance(conn, _SSLSocket):
                        conn.unwrap()
                except ssl.SSLError:
                    pass
                except FileNotFoundError:
                    pass
        return self.voidresp()


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
        conn, size = FTPC.ntransfercmd(self, cmd, rest)
        conn = self.sock.context.wrap_socket(
            conn, server_hostname=self.host, session=self.sock.session
        )
        return conn, size


