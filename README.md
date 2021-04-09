# python-Papago
python translator

## example
```py
from papago import Papago
import asyncio

async def main():
    papago = Papago('detect', 'ja')
    res = await papago.translate('안녕', honorific=True)
    print(res)

if __name__ == '__main__': asyncio.run(main())
```
prints:
```py
{
    'source': 'ko',
    'target': 'ja', 
    'text': '안녕', 
    'translatedText': 'こんにちは', 
    'sound': "kon'nichiwa", 
    'srcSound': 'annyong'
}
```
