import logging
import socket


class Rcon:
    
    PACKET_PREFIX = b'\xff' * 4
    
    def __init__(self, host="localhost", port=27960, password=""):
        self._host = host
        self._port = port
        self._password = password
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    def connect(self):
        logging.info("Rcon connect to: %s:%s" % (self._host, self._port), )
        self._socket.connect((self._host, self._port))
        self._socket.settimeout(0.5)

    def disconnect(self):
        self._socket.shutdown(2)
        self._socket.close()
        logging.info("Rcon disconnect from %s:%s" % (self._host, self._port), )
            
    def __send(self, data):
        self._socket.send(self.PACKET_PREFIX + ("%s\n" % data).encode())
        
    def __recv(self):
        return self._socket.recv(4096)[len(self.PACKET_PREFIX):].decode()
    
    def __parse(self, data):
        return data.split("\n", 1)[1]
    
    def run(self, cmd, retries=3):
        logging.info("Rcon run: %s" % cmd)
        request = 'rcon "%s" %s' % (self._password, cmd)
        while retries:
            logging.debug("Rcon send: %s" % request)
            response = ""
            self.__send(request)
            try:
                while True:
                    response += self.__recv()
            except Exception as e:
                if response:
                    logging.debug("Rcon response: %s" % response)
                    return self.__parse(response)
                elif retries == 0:
                    raise e
                else:
                    retries -= 1
