import requests
import hmac
import base64
import time
import uuid

class Papago:

    def __init__(self, source, target, text):
        if not isinstance(source, str): raise TypeError('Invalid source parameter type')
        if not isinstance(target, str): raise TypeError('Invalid target parameter type')
        if not isinstance(text, str): raise TypeError('Invalid text parameter type')
        self.source = source
        self.target = target
        self.text = text

    async def __encrypt(self, text, passphrase):
        hash = hmac.digest(passphrase.encode(), text.encode(), 'MD5')
        return base64.b64encode(hash).decode()

    async def __detect(self, query):
        url = 'https://papago.naver.com/apis/langs/dect'
        timestamp = str(int(time.time() * 1000))
        deviceId = uuid.uuid4()
        hash = await self.__encrypt(f'{deviceId}\n{url}\n{timestamp}', 'v1.5.2_0d13cb6cf4')
        auth = f'PPG {deviceId}:{hash}'
        response = requests.post(
            url,
            headers = {
                'Authorization': auth,
                'Timestamp': timestamp,
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
            },
            data = dict(query=query)
        ).json()
        langcode = response['langCode']

        if langcode != 'unk':
            return langcode

    async def translate(self, honorific = False, verbose = False):
        url = 'https://papago.naver.com/apis/n2mt/translate'
        timestamp = str(int(time.time() * 1000))
        deviceId = uuid.uuid4()
        hash = await self.__encrypt(f'{deviceId}\n{url}\n{timestamp}', 'v1.5.2_0d13cb6cf4')
        auth = f'PPG {deviceId}:{hash}'
        if self.source == 'detect':
            self.source = await self.__detect(self.text)
            if not self.source:
                raise Exception('Cannot detect text')
        response = requests.post(
            url,
            headers = {
                'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'Authorization': auth,
                'Timestamp': timestamp,
                'Device-Type': 'pc',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
            },
            data = {
                'deviceId': deviceId,
                'locale': 'ko',
                'dict': 'true',
                'dictDisplay': '30',
                'honorific': 'true' if honorific else 'false',
                'instant': 'false',
                'paging': 'false',
                'source': self.source,
                'target': self.target,
                'text': self.text
            }
        )
        if response.status_code == 500: raise ValueError('Invalid langCode parameter')
        if response.status_code == 403: raise ConnectionAbortedError('Connnection aborted')
        if response.status_code != 200: raise Exception('Unexpected Error')
        body = response.json()
        sound = None
        srcSound = None
        if 'tlit' in body:
            sound = ' '.join(list(map(lambda x: x['phoneme'], body['tlit']['message']['tlitResult'])))
        if 'tlitSrc' in body:
            srcSound = ' '.join(list(map(lambda x: x['phoneme'], body['tlitSrc']['message']['tlitResult'])))
        return {
            'source': self.source,
            'target': self.target,
            'text': self.text,
            'translatedText': body['translatedText'],
            'sound': sound,
            'srcSound': srcSound
        }
