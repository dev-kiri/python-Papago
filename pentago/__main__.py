# 2024-11-29 Kiri, All rights reserved.
from pentago.lang import *
from pentago.api import *
from pentago.client import *
from pentago.hash import Crypto
from pentago.response import Response
from pentago.detect import Detect
from typing import Dict
import requests
import json

class Pentago:
    def __init__(self, source: str, target: str):
        self.source = source
        self.target = target

    async def translate(self, text: str, honorific: bool = False, verbose: bool = False) -> Dict[str, str]:
        if self.source == 'auto':
            self.source = await Detect(text).lang()
        crypto = Crypto(API_TRANS)
        body = {'authorization': crypto.authorization, 'timestamp': crypto.timestamp, 'deviceId': crypto.device_id}
        headers = {
            **CLIENT_HEADER,
            **body,
            'referer': API_BASE,
            'x-apigw-partnerid': API_ID,
        }
        data = {'authroization' if k == 'authorization' else k: v for k, v in body.items()}
        res = requests.post(API_TRANS, headers=headers, data={
            **data,
            'locale': 'ko',
            'dict': 'true',
            'dictDisplay': '30',
            'honorific': 'true' if honorific else 'false',
            'instant': 'false',
            'paging': 'true',
            'source': self.source,
            'target': self.target,
            'text': text
        })
        status = Response(res.status_code)
        if status.response:
            content = res.json()
            if verbose: return json.dumps(content, indent=4)
            sound: str = None
            srcSound: str = None
            if 'tlit' in content:
                sound = ' '.join(list(map(lambda x: x['phoneme'], content['tlit']['message']['tlitResult'])))
            if 'tlitSrc' in content:
                srcSound = ' '.join(list(map(lambda x: x['phoneme'], content['tlitSrc']['message']['tlitResult'])))
            return {
                'source': self.source,
                'target': self.target,
                'text': text,
                'translatedText': content['translatedText'],
                'sound': sound,
                'srcSound': srcSound
            }        
    