import aiohttp
import aiofiles
import json

async def getData(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def readJSON(file_path):
    async with aiofiles.open(file_path, mode='r') as file:
        content = await file.read()
        return json.loads(content)