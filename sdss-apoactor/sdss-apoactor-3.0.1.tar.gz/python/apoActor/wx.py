#!/usr/bin/env python

import ctypes
from binascii import crc32
from socket import AF_INET, SOCK_DGRAM, socket
from sys import stdout
from time import sleep
from traceback import print_exc


class WX:
    """Weather server communications"""

    class v:
        """contains values received from the weather server"""

        pass

    def __init__(self, server="10.25.1.254", port=6251, timeout=15):
        self.server = (server, port)
        self.size = 2048
        self.defaultTimeout = timeout

    def connect(self):
        global sock
        try:
            sock = socket(AF_INET, SOCK_DGRAM)
            sock.settimeout(2)
            sock.connect(self.server)
            sock.settimeout(self.defaultTimeout)
        except:
            print_exc()
            return -1
        return 0

    def close(self):
        try:
            sock.close()
        except:
            print_exc()
            return -1
        return 0

    def recv(self):
        """receive a message from the server"""
        try:
            return sock.recv(self.size).decode()
        except:
            print_exc()
            return ""

    def recvonce(self):
        """receive a single message and close the connection"""
        self.connect()
        reply = self.recv().decode()
        self.close()
        return reply

    def send(self, messages):
        """send a list of messages to the server and return any reply"""
        for message in messages:
            try:
                sock.send(message.encode())
            except:
                print_exc()
                return ""

        try:
            return sock.recv(self.size).decode()
        except:
            print_exc()
            return ""

    def sendonce(self, messages):
        """send a list of messages and close the connection"""
        self.connect()
        reply = self.send(messages)
        self.close()
        return reply

    def uint(self, x):
        """converts a signed integer to an unsigned integer"""
        return ctypes.c_uint(x).value

    def recvcat(self, category="all", dict=False, debug=False):
        """recv the category, checking the datagram and
        returning the variables and their values

        format: <d_len> <d_crc32> <d_nval> timeStamp=<n> <keyword>=<val> end
        """

        reply = self.sendonce([category])

        if debug:
            print("category=%s, dict=%d, debug=%d" % (category, dict, debug))
            print(reply)
            stdout.flush()

        if "end" != reply[-3:]:
            self.v.recv_status = "Premature end of data"
            return WX()
        else:
            start = reply.find("timeStamp")
            stop = reply.find(" end")
            tmp = reply[:start].split()  # [len, crc32, nval]

            reply_bytes = reply[start:].encode()

            if -1 == start:
                self.v.recv_status = '"timeStamp" key not found'
            elif -1 == stop:
                self.v.recv_status = '"end" key not found'
            elif int(tmp[0]) != len(reply[start:]):
                self.v.recv_status = "Short packet"
            elif int(tmp[1], 16) != self.uint(0xFFFFFFFF & crc32(reply_bytes)):
                self.v.recv_status = "Invalid CRC32"
            elif int(tmp[2]) != len(reply[start:stop].split()):
                self.v.recv_status = "Missing value(s)"
            else:
                if dict:
                    self.v.d = {}
                    if "tuples" == category:
                        exec(
                            "self.v.d['"
                            + reply[start:stop]
                            .replace("=", "']=")
                            .replace(" ", "; self.v.d['")
                        )
                    else:
                        exec(
                            "self.v.d['"
                            + reply[start:stop]
                            .replace("=", "']='")
                            .replace(" ", "'; self.v.d['")
                            + "'"
                        )

                else:
                    exec(
                        "self.v."
                        + reply[start:stop]
                        .replace("=", "='")
                        .replace(" ", "'; self.v.")
                        + "';"
                    )
                self.v.recv_status = "OK"

        if debug:
            print(start, stop, tmp, int(tmp[0]), "%X" % int(tmp[1], 16), int(tmp[2]))
            print(
                len(reply[start:]),
                "%X" % self.uint(0xFFFFFFFF & crc32(reply[start:])),
                len(reply[start:stop].split()),
            )
            stdout.flush()

        return WX()

    def vclear(self, dict=False):
        """Delete the variables for class v"""
        if dict:
            del self.v
        else:
            for key in vars(self.v).copy().keys():
                exec("del self.v.%s" % key)


if __name__ == "__main__":

    if 0:
        w = WX()
        w.v.recv_status = "OK"
        while w.v.recv_status == "OK":
            w.recvcat(category="all", debug=1)
            sleep(1)
    else:
        print("Variables:\n")
        w = WX().recvcat(debug=1)
        print("recv_status =", w.v.recv_status)
        print(len(vars(w.v)))
        print(vars(w.v))
        w.vclear()
        print(len(vars(w.v)))

        w = WX().recvcat("site", debug=1)
        print("recv_status =", w.v.recv_status)
        print(len(vars(w.v)))

        print("\nDictionary:\n")
        w = WX().recvcat(dict=1, debug=1)
        print("recv_status =", w.v.recv_status)
        print(w.v.d)
        WX().vclear()
        w = WX().recvcat("site", dict=True, debug=True)
        print("recv_status =", w.v.recv_status)
        print(w.v.d)

        print("\nDictionary with Tuples:\n")
        w = WX().recvcat("tuples", dict=1, debug=1)
        print("recv_status =", w.v.recv_status)
        print(w.v.d)

# Traceback (most recent call last):
# File "./wx.py", line 171, in ?
# 	w = WX().recvcat ('tuples', dict=1, debug=1)
# File "./wx.py", line 128, in recvcat
# 	print start, stop, tmp, int (tmp[0]), '%X' % int (tmp[1], 16), int (tmp[2])
# UnboundLocalError: local variable 'start' referenced before assignment
