# 2024-11-29 Kiri, All rights reserved.
from typing import Dict

CLIENT_DEVICE_TYPE: str = 'pc'
CLIENT_CONTENT_TYPE: str = 'application/x-www-form-urlencoded; charset=UTF-8'
CLIENT_USER_AGENT: str = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0'

CLIENT_HEADER: Dict[str, str] = {
    'content-type': CLIENT_CONTENT_TYPE,
    'device-type': CLIENT_DEVICE_TYPE,
    'user-agent': CLIENT_USER_AGENT
}