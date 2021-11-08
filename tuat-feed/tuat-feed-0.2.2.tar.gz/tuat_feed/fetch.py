from typing import List
from tuat_feed.post import Post
import requests


def fetch(
    gakubu="technology",
    category: str = "all",
    url: str = "https://api.ihavenojob.work/tuat/",
) -> List[Post]:
    """投稿の取得

    Parameters
    ----------
    gakubu : str, optional学部。"technology", "agriculture"。デフォルトは"technology"。
        取得する
    category : str, optional
        取得する投稿の種類。"all", "campus", "academic"。デフォルトでは"all"。
    url : str, optional
        データを取得するAPIのURL、デフォルトでは"https://api.ihavenojob.work/tuat/"

    Returns
    -------
    List[Post]
        投稿の一覧

    Raises
    ------
    ValueError
        gakubu, categoryに規定外の入力があった場合
    """

    if gakubu == "technology":
        G = "/T/"
    elif gakubu == "agriculture":
        G = "/A/"
    else:
        raise ValueError(
            f'gakubu must be one of "technology" or "agriculture". {gakubu} was supplied.'
        )

    if category == "all":
        response = requests.get(url + G)
    elif category == "academic":
        response = requests.get(url + G + "academic")
    elif category == "campus":
        response = requests.get(url + G + "campus")
    else:
        raise ValueError(
            f'category must be one of "all", "academic" or "campus". {category} was supplied.'
        )

    feed = response.json()
    posts = []
    for p in feed:
        posts.append(Post.parse_post(p))
    return posts


def fetch_technology(
    category: str = "all",
    url: str = "https://api.ihavenojob.work/tuat/",
) -> List[Post]:
    """工学部掲示板情報の取得

    Parameters
    ----------
    category : str, optional
        情報のカテゴリ。詳細は`fetch`を確認してください。
    url : str, optional
        API URL詳細は`fetch`を確認してください。

    Returns
    -------
    List[Post]
        投稿の一覧

    Raises
    ------
    ValueError
        gakubu, categoryに規定外の入力があった場合
    """
    return fetch(gakubu="technology", category=category, url=url)


def fetch_agriculture(
    category: str = "all",
    url: str = "https://api.ihavenojob.work/tuat/",
) -> List[Post]:
    """工学部掲示板情報の取得

    Parameters
    ----------
    category : str, optional
        情報のカテゴリ。詳細は`fetch`を確認してください。
    url : str, optional
        API URL詳細は`fetch`を確認してください。

    Returns
    -------
    List[Post]
        投稿の一覧

    Raises
    ------
    ValueError
        gakubu, categoryに規定外の入力があった場合
    """
    return fetch(gakubu="agriculture", category=category, url=url)
