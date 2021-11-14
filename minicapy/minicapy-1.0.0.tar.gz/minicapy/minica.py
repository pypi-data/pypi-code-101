from ctypes import c_char_p, cdll
from pathlib import Path

minicaso = cdll.LoadLibrary(Path(__file__).parent / "minica.dll")


def create_domain_cert(domain: str) -> int:
    """Create an ssl certificate for the given domain.
    Return code meanings:
        0 -> success
        1 -> couldn't create CA files minica-key.pem and minica.pem
        2 -> couldn't create certificate, likely already exists"""
    return minicaso.generateCertificate(c_char_p(domain.encode("utf-8")))


def create_ip_cert(ip_address: str) -> int:
    """Create an ssl certificate for an ip address.
    Return code meanings:
        0 -> success
        1 -> couldn't create CA files minica-key.pem and minica.pem
        2 -> couldn't create certificate, likely already exists"""
    return minicaso.generateIPCertificate(c_char_p(ip_address.encode("utf-8")))
