import aiohttp
from .models import *

from .errors import recognizeError, MethodMissing


class KeyLevel:
    guest = 'guest'
    trusted = 'trusted'
    dedicated = 'dedicated'
    system = 'system'


class Api:

    def __init__(self, key: str, key_level: KeyLevel):
        self.key = key
        self.key_level = key_level
        self.tags = [
            'kiss',
            'baka',
            'wasted',
            'wag',
            'triggered',
            'trap',
            'tickle',
            'teehee',
            'stare',
            'smile',
            'sleepy',
            'slap',
            'sex',
            'pout',
            'poke',
            'pat',
            'lick',
            'lewd',
            'insult',
            'hug',
            'dance',
            'cuddle',
            'cry',
            'blush',
            'bite',
            'bang'
        ]

        self.headers = {
            'Authorization': f'{self.key_level} {self.key}'
        }


    async def banCheck(self, user_id: int) -> BanCheckResult:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(f'https://api.reboot.su/bans/{user_id}/check', ) as response:
                response = await response.json()

        if 'message' in response.keys():
            raise recognizeError(response['code'])
        else:
            return BanCheckResult(response)


    async def banInfo(self, user_id: int) -> BanInfoResult:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(f'https://api.reboot.su/bans/{user_id}/info', ) as response:
                response = await response.json()

        if 'message' in response.keys():
            raise recognizeError(response['code'])
        else:
            return BanInfoResult(response['user'])


    async def imageRandom(self, tag_: str) -> ImageRandomResult:
        if tag_ in self.tags:
            async with aiohttp.ClientSession(headers= self.headers) as session:
                async with session.get(f'https://api.reboot.su/images/random/{tag_}', ) as response:
                    response = await response.json()

            if 'message' in response.keys():
                raise recognizeError(response['code'])
            else:
                return ImageRandomResult(response)
        else:
            raise MethodMissing("Метод не найден.")


    async def imageId(self, id_: int) -> ImageIdResult:
        async with aiohttp.ClientSession(headers= self.headers) as session:
            async with session.get(f'https://api.reboot.su/images/id/{id_}', ) as response:
                response = await response.json()

        if 'message' in response.keys():
            raise recognizeError(response['code'])
        else:
            return ImageIdResult(response)
