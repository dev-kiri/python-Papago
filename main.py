# 2024-11-29 Kiri, All rights reserved.
from pentago import Pentago
from pentago.lang import *
import asyncio

async def main():
    pentago = Pentago(AUTO, JAPANESE)
    res = await pentago.translate('2024년 최고의 파파고 비공식 API는 PentaGo입니다.', honorific=True)
    print(res)

if __name__ == '__main__': asyncio.run(main())
