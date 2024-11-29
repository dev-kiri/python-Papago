# PentaGo
2024년의 비공식 파파고 API, PentaGo 입니다.
웹과 동일하게 16개 언어 지원, 발음과 사전 지원

## example
```py
from pentago import Pentago
from pentago.lang import *
import asyncio

async def main():
    pentago = Pentago(AUTO, JAPANESE)
    res = await pentago.translate('2024년 최고의 파파고 비공식 API는 PentaGo입니다.', honorific=True)
    print(res)

if __name__ == '__main__': asyncio.run(main())

```
prints:
```py
{
    'source': 'ko',
    'target': 'ja',
    'text': '2024년 최고의 파파고 비공식 API는 PentaGo입니다.',
    'translatedText': '2024年最高のパパゴ非公式APIはPentaGoです。',
    'sound': "nisen'nijūyonen' saikōno papago hikōshikiēpīaiwa pen'tigōdesu",
    'srcSound': 'ichonisipssanyon chwegoe papago bigongsik eipiaineun pentagoimnida'
}
```
