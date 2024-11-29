# 2024-11-29 Kiri, All rights reserved.
from pentago.api import *
import re
import requests

class Software:
    def __init__(self):
        self._javascript_url = None

    @property
    def javascript_url(self) -> str:
        res = requests.get(API_BASE)
        pattern = r'/main\.[a-zA-Z0-9]+\.chunk\.js'
        match = re.search(pattern, res.text)
        if match:
            self._javascript_url = match.group(0)
        return API_BASE + self._javascript_url
    
    def update(self):
        res = requests.get(self.javascript_url)
        pattern = r'v\d+\.\d+\.\d+_[a-z0-9]+'
        match = re.search(pattern, res.text)
        if match:
            key = match.group(0)
            with open('license_key.txt', 'w') as file:
                file.write(key.strip())
