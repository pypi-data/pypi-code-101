import socket
import re


def get(domain, whois_server = "whois.iana.org"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((whois_server, 43))
    s.send((f"{domain}\r\n").encode("utf8"))

    msg = ''
    while 1:
        data = (s.recv(100)).decode("utf8")
        if data:
            msg += data
        else:
            break

    refer = re.search("refer:(.*)", msg).group(1).strip() if re.search("refer:(.*)", msg) else 0
    if refer:
        return get(domain, refer)
    else:
        return msg
