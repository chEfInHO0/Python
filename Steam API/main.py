import requests
import asyncio

class API():
    def __init__(self) -> None:
        self.page = 1
        self.url = f'https://www.cheapshark.com/api/1.0/deals?storeID=1&upperPrice={self.page}'
    
    async def getPrice(self):
        req = requests.get(self.url)
        return req.json()
    
    async def showPrices(self):
        print(await self.getPrice())
    
    def nextPage(self):
        self.page += 1

self = API()

res = asyncio.run(self.getPrice())
keys = [key for key in res[0]]

for element in res:
    print("#"*15)
    for key in keys:
        print(f'{key} = {element[key]}')
    print("#"*15)