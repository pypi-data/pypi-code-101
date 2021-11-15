import os
import pytz
import asyncio
import twitter
from tqdm import tqdm
from datetime import datetime
from typing import AnyStr, List
from dateutil.parser import parse


async def load_tweets(screen_name: AnyStr, offset: int):
    api = get_client()
    tweets = api.GetUserTimeline(screen_name=screen_name, count=200, max_id=offset)
    return tweets


def get_client():
    CONSUMER_KEY = str(os.getenv("TWITTER_CONSUMER_KEY"))
    CONSUMER_SECRET = str(os.getenv("TWITTER_CONSUMER_SECRET"))
    ACCESS_TOKEN = str(os.getenv("TWITTER_ACCESS_TOKEN"))
    ACCESS_TOKEN_SECRET = str(os.getenv("TWITTER_ACCESS_TOKEN_SECRET"))
    api = twitter.Api(consumer_key=CONSUMER_KEY,
                      consumer_secret=CONSUMER_SECRET,
                      access_token_key=ACCESS_TOKEN,
                      access_token_secret=ACCESS_TOKEN_SECRET)
    return api


async def delete_tweets(user_handle: AnyStr, days: int = 30):
    """
    This function gathers tweet id-s recursive that will be deleted
    and after that tries to delete tweets with found id-s
    :return:
    """
    api = get_client()
    user = api.GetUser(screen_name=user_handle)

    # get most recent tweet
    response = api.GetUserTimeline(screen_name=user_handle, count=1)
    max_item = response[-1]
    max_id = max_item.id

    now = datetime.utcnow()
    tz = pytz.timezone("UTC")
    now = tz.localize(now)

    async def _internal(max_id, out: List):
        """
        Internal recursion worker
        :param max_id:
        :param out:
        :return:
        """
        items = await load_tweets(offset=max_id)
        if len(items) < 2:
            return out
        for item in tqdm(items, desc="Loading tweet ID-s"):
            if item.user.id == user.id:
                try:
                    created_at = parse(item.created_at)
                    max_id = item.id
                    days = (now - created_at).days
                    if days >= days:
                        out.append(item.id)
                except Exception as ex:
                    print(ex)
        return await _internal(max_id=max_id, out=out)

    ids = await _internal(max_id=max_id, out=list())
    for idx, _id in tqdm(enumerate(ids), desc="Deleting tweets", total=len(ids)):
        try:
            api.DestroyStatus(_id)
        except Exception as ex:
            print(ex)
        await asyncio.sleep(delay=0.5)

    return
