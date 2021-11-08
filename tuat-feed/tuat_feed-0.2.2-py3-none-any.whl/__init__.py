"""tuat-feed
農工大の掲示板のデータを取得するライブラリです。使い方としては次のように使うことができます。

>>> import tuat_feed
>>> feed = tuat_feed.fetch_technology() # 工学部掲示板情報の取得
# >>> feed = tuat_feed.fetch_agriculture() # 農学部掲示板情報の取得
>>> len(feed)
40
>>> feed[0]
Post(...)
"""

from .fetch import fetch, fetch_technology, fetch_agriculture
