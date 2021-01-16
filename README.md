# python-Papago
python translator

## example
```py
from papago import Papago
import asyncio

loop = asyncio.get_event_loop()

async def main():
    return await Papago('detect', 'ja', 'Hello').translate(honorific=True)

print(loop.run_until_complete(main()))
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
