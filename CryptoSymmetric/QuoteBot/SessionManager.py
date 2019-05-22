import struct
import os
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
import binascii

BLOCK_SIZE = 16


pad = lambda s: s + ((BLOCK_SIZE - len(s) % BLOCK_SIZE) * chr(BLOCK_SIZE - len(s) % BLOCK_SIZE)).encode()


def unpad(s):
    if (len(s) % BLOCK_SIZE ) != 0:
        ValueError("Bad serialization data: unpad len")

    has_padding = all(s[-1] == x for x in s[-s[-1]:])
    if not has_padding:
        return s

    return s[:-s[-1]]

# CIPHER_KEY = binascii.unhexlify(os.environ.get("ENCKEY"))
CIPHER_KEY = b'MYMEGAFLAG111111'

class AESCipher:
    def __init__(self, key):
        self.key = key

    def encrypt(self, raw):
        raw = pad(raw)
        cipher = AES.new(self.key, AES.MODE_ECB)
        return b64encode(cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = b64decode(enc)
        cipher = AES.new(self.key, AES.MODE_ECB)
        return unpad(cipher.decrypt(enc))

class Serializer:
    @staticmethod
    def serialize_dict(data):
        serialized_data = b''
        for key in data:
            serialized_data += Serializer.serialize_str(key)
            serialized_data += Serializer.serialize_str(data[key])

        return serialized_data

    @staticmethod
    def serialize_str(s):
        return struct.pack('<I', len(s)) + s

    @staticmethod
    def unserialize_dict(serialized_data):
        data = {}
        k = 0
        while k < len(serialized_data):
            key, k = Serializer.unserialize_str(serialized_data, k)
            value, k = Serializer.unserialize_str(serialized_data, k)
            data[key] = value
        return data

    @staticmethod
    def unserialize_str(serialized_str, start_index):
        if start_index + 4 > len(serialized_str):
            raise ValueError("Bad serialization data 3")
        len_str = struct.unpack("<I", serialized_str[start_index:start_index+4])[0]
        if start_index + 4 + len_str > len(serialized_str):
            raise ValueError("Bad serialization data 4")
        return serialized_str[start_index + 4:start_index + 4 + len_str], start_index + 4 + len_str

class Session:
    def __init__(self):
        self.data = {}

    def __init__(self, data = None):
        if data == None:
            self.data = {}
        else:
            try:
                serialized_data = AESCipher(CIPHER_KEY).decrypt(data)
            except Exception as e:
                raise ValueError("Bad serialization data 5")

            self.data = Serializer.unserialize_dict(serialized_data)

    def set_value(self, key, value):
        self.data[key] = value

    def get_value(self, key):
        return self.data.get(key)

    def get_cookie(self):
        return AESCipher(CIPHER_KEY).encrypt(Serializer.serialize_dict(self.data))


