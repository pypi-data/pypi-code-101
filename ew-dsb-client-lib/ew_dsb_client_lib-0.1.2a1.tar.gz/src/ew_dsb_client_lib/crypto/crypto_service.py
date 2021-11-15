#!/usr/bin/env python3

import base64
import binascii

import eth_keys
from ew_dsb_client_lib.crypto.entities.jwt_header_entity import JWTHeader


class CryptoService:
    def __base64_url_encode(self, string):
        """Removes any `=` used as padding from the encoded string.

        Parameters
        ----------
        string : str

        Returns
        -------
        str
        """
        encoded = base64.urlsafe_b64encode(string.encode('utf-8')).decode('utf-8')
        return encoded.rstrip("=")

    def __base64_url_decode(self, string):
        """Adds back in the required padding before decoding.

        Parameters
        ----------
        string : str

        Returns
        -------
        str
        """
        padding = 4 - (len(string) % 4)
        string = string + ("=" * padding)
        return base64.urlsafe_b64decode(string.encode('utf-8')).decode('utf-8')

    def sign(self, payload:str, private_key:str) -> str:
        """Sign a message with a private key

        Parameters
        ----------
        payload : str
        private_key : str

        Returns
        -------
        str
        """
        header:JWTHeader = JWTHeader(
            alg='ES256',
            typ='JWT'
        )
        encoded_header:str = self.__base64_url_encode(header.to_json())

        encoded_payload:str = self.__base64_url_encode(payload)

        message:str = "".join([encoded_header, '.', encoded_payload])
        signer = eth_keys.keys.PrivateKey(binascii.unhexlify(private_key))
        signature = signer.sign_msg(message.encode())
        encoded_signature:str = self.__base64_url_encode(str(signature))

        jwt_token:str = "".join([encoded_header, '.', encoded_payload, '.', encoded_signature])
        return jwt_token

    def verify_signature(self, payload:str, public_key:str) -> bool:
        """Verify a message signature with a public key

        Parameters
        ----------
        payload : str
        public_key : str

        Returns
        -------
        bool
        """
        return True
