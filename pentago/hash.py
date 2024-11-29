# 2024-11-29 Kiri, All rights reserved.
import hmac
import uuid
import time
import base64
from pentago.update import Software

_DIGEST_MOD: str = 'MD5'

class Crypto:
    def __init__(self, text: str):
        self.text = text
        self._device_id = None
        self._timestamp = None
        self._hash = None
        self._authorization = None

    @property
    def key(self) -> str:
        try:
            with open('license_key.txt', 'r') as file:
                return file.read()
        except:
            Software().update()
            return self.key

    @property
    def device_id(self) -> str | None:
        if self._device_id is None:
            self._device_id = str(uuid.uuid4())
        return self._device_id
    
    @property
    def timestamp(self) -> str | None:
        if self._timestamp is None:
            self._timestamp = str(int(time.time() * 1000))
        return self._timestamp
    
    @property
    def hash(self) -> str | None:
        if self._hash is None:
            device_id = self.device_id
            timestamp = self.timestamp
            message = f'{device_id}\n{self.text}\n{timestamp}'.encode()
            md5 = hmac.digest(self.key.encode(), message, _DIGEST_MOD)
            self._hash = base64.b64encode(md5).decode()
        return self._hash
    
    @property
    def authorization(self) -> str | None:
        if self._authorization is None:
            self._authorization = f'PPG {self.device_id}:{self.hash}'
        return self._authorization