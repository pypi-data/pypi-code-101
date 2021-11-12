def IntToBytes(data: int, padd: int = 4):
    return (data).to_bytes(padd, byteorder='big', signed=False)

def IntFromBytes(data: bytes) -> int:
    return int.from_bytes(data, byteorder='big')

def formatBytes(data: bytes, sep: str = " 0x") -> str:
    bytes_str = map("{:02x}".upper().format, data)
    return "0x" + sep.join(bytes_str)
