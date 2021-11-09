import os
import pytweet

client=pytweet.Client(os.environ["bearer_token"], consumer_key=os.environ["api_key"], consumer_key_secret=os.environ["api_key_secret"], access_token=os.environ["access_token"], access_token_secret=os.environ["access_token_secret"])

# client.tweet("hello tweet... tweet...")
tweet=client.fetch_tweet(1453927577018458119)
print(tweet)
# tweet.reply("Tweet.. tweet... spooky. I hope im not late! Just migrated to the south and arrived in my lovely nest OwO")


























#{'created_at': 'Tue Nov 09 01:09:37 +0000 2021', 'id': 1457878004864933894, 'id_str': '1457878004864933894', 'text': '@TheGenocides lmao', 'truncated': False, 'entities': {'hashtags': [], 'symbols': [], 'user_mentions': [{'screen_name': 'TheGenocides', 'name': 'TheGenocide', 'id': 1382006704171196419, 'id_str': '1382006704171196419', 'indices': [0, 13]}], 'urls': []}, 'source': '<a href="https://youtube.com" rel="nofollow">TweetyBott</a>', 'in_reply_to_status_id': 1457872650840133632, 'in_reply_to_status_id_str': '1457872650840133632', 'in_reply_to_user_id': 1382006704171196419, 'in_reply_to_user_id_str': '1382006704171196419', 'in_reply_to_screen_name': 'TheGenocides', 'user': {'id': 1445987330582405122, 'id_str': '1445987330582405122', 'name': 'Tweety', 'screen_name': 'TweetyBott', 'location': 'https://discord.gg/XHBhg6A4jJ', 'description': "I'm a bot :robot: made by @TheGenocides | OwO i love Amongus | Owo will you be my friend?", 'url': 'https://t.co/FrISXgipmT', 'entities': {'url': {'urls': [{'url': 'https://t.co/FrISXgipmT', 'expanded_url': 'https://discord.gg/XHBhg6A4jJ', 'display_url': 'discord.gg/XHBhg6A4jJ', 'indices': [0, 23]}]}, 'description': {'urls': []}}, 'protected': False, 'followers_count': 2, 'friends_count': 5, 'listed_count': 0, 'created_at': 'Thu Oct 07 05:40:32 +0000 2021', 'favourites_count': 18, 'utc_offset': None, 'time_zone': None, 'geo_enabled': False, 'verified': False, 'statuses_count': 60, 'lang': None, 'contributors_enabled': False, 'is_translator': False, 'is_translation_enabled': False, 'profile_background_color': 'F5F8FA', 'profile_background_image_url': None, 'profile_background_image_url_https': None, 'profile_background_tile': False, 'profile_image_url': 'http://pbs.twimg.com/profile_images/1457524164135321607/bDjkzNfJ_normal.jpg', 'profile_image_url_https': 'https://pbs.twimg.com/profile_images/1457524164135321607/bDjkzNfJ_normal.jpg', 'profile_link_color': '1DA1F2', 'profile_sidebar_border_color': 'C0DEED', 'profile_sidebar_fill_color': 'DDEEF6', 'profile_text_color': '333333', 'profile_use_background_image': True, 'has_extended_profile': True, 'default_profile': True, 'default_profile_image': False, 'following': False, 'follow_request_sent': False, 'notifications': False, 'translator_type': 'none', 'withheld_in_countries': []}, 'geo': None, 'coordinates': None, 'place': None, 'contributors': None, 'is_quote_status': False, 'retweet_count': 0, 'favorite_count': 0, 'favorited': False, 'retweeted': False, 'lang': 'ht'}