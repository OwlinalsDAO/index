import aiohttp
from aiohttp import ClientError
from fake_useragent import UserAgent

class OwlinalsIndexer:

    def __init__(self, page: int, ) -> None:
        self.page = page

    async def __aenter__(self, *args):
        user_agent = UserAgent().random
        headers = {
            'Accept': 'application/json, text/plain, */*',
            'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
            'Connection': 'keep-alive',
            'Origin': 'https://geniidata.com',
            'Referer': 'https://geniidata.com/',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-site',
            'User-Agent': user_agent,
            'sec-ch-ua-mobile': '?1',
        }
        # self.session = aiohttp.ClientSession(headers=headers)
        self.session = aiohttp.ClientSession(connector=aiohttp.TCPConnector(limit=64,verify_ssl=False),headers=headers)
        return self

    async def __aexit__(self, *args):
        await self.session.close()

    async def index_page(self):
        url = f'https://www.geniidata.com/api/dashboard/chart/public/data?chartId=276771&pageSize=100&page={self.page}&searchKey=&searchValue='

        try:
            response = await self.session.get(url)
            response.raise_for_status()
            response_json = await response.text()
            return response_json
        except ClientError as e:
            print(f"Error in web_challenge request: {e}")
