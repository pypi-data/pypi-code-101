import youtube_dl as ydl
import re
from urllib.parse import quote
from typing import (
	Dict,
	List,
	Union
)

__all__ = (
	'Pytdl',
	'Stream',
	'YoutubeVideos',
	'YoutubeVideo',
	'SpotifyMusics',
	'SpotifyMusic',
	'SpotifyTypeError',
	'YoutubeTypeError',
	'SpotifyUrlError',
	'YoutubeUrlError'
)

JSON = Dict[str, Union[str, List, Dict]]

from .webBug import get, spotifyGet
from .dataParser import Parser

sl = r'https://open\.spotify\.com/(album|paylist)/[A-Za-z0-1_\-]{22}'
yl = r'https://www\.youtube\.com/playlist?list=[A-Za-z0-1_\-]{34}'
s = r'https://open\.spotify\.com/track/[A-Za-z0-1_\-]{22}'
y = r'https://www\.youtube\.com/watch?v=[A-Za-z0-1_\-]{11}'

from base64 import b64decode
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials as SCC

client_id = \
	b64decode(b'N2U0ZDI2ZDAyMjNlNDkxNzgzMmI1NDIxNmZmODE2OWU=') \
	.decode()
client_secret = \
	b64decode(b'NTc0YWViNzY2MmMxNDNiM2EwMThjODYwZDI5M2I4ZmU=') \
	.decode()

sp = spotipy.Spotify(auth_manager=SCC(
	client_id = client_id,
	client_secret = client_secret
))

def dp(d : int) -> str:
	result = ''
	h = d // 3600
	m = (d - h * 3600) // 60
	s = (d - h * 3600) - m * 60

	if h < 10:
		result += '0' + str(h)
	else:
		result += str(h)
	result += ':'
	if m < 10:
		result += '0' + str(m)
	else:
		result += str(m)
	result += ':'
	if s < 10:
		result += '0' + str(s)
	else:
		result += str(s)

	return result

class UnKnownError(Exception):
	...

class SpotifyTypeError(Exception):
	...

class YoutubeTypeError(Exception):
	...

class SpotifyUrlError(Exception):
	...

class YoutubeUrlError(Exception):
	...

class Stream:
	def __init__(self, url : str):
		self.__url = url

	def download(self, path : str = './'):
		self.opt = {
			'format': 'bestaudio/best',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192'
			}],
			'outtmpl': path if path != "./" else "./%(id)s.mp3"
		}
		
		with ydl.YoutubeDL(self.opt) as dl:
			dl.extract_info(self.__url, download=True)

class SpotifyMusics:
	def __init__(self, url : str):
		if not (re.match(sl, url) or re.match(s, url)):
			raise SpotifyTypeError('%s is not a spotify url' % (url))
		elif not re.match(sl, url):
			raise SpotifyUrlError('%s is not a spotify list url' % (url))

		self.__url = url
		self.__type = url.split('/')[3]

	async def create(self) -> None:
		self.ytdl : Pytdl = Pytdl()
		if self.__type == 'album':
			sl = await self.ytdl.spotifyResultList(self.__url)
		else:
			sl = await self.ytdl.spotifyPlayList(self.__url)

		self.musicList = []
		for s in sl:
			data = (await self.resultList(s['title']))[0]
			self.musicList.append(
				YoutubeVideo('https://www.youtube.com/watch?v=' + data['id'], data)
			)

class YoutubeVideos:
	def __init__(self, url : str):
		if not (re.match(yl, url) or re.match(y, url)):
			raise YoutubeTypeError('%s is not a youtube url' % (url))
		elif not re.match(yl, url):
			raise YoutubeUrlError('%s is not a youtube list url' % (url))

		self.__url = url

	async def create(self) -> None:
		self.ytdl : Pytdl = Pytdl()
		yl = await self.ytdl.PlayList(self.__url.split('=')[0])

		self.videoList = []
		for y in yl:
			self.videoList.append(
				YoutubeVideo('https://www.youtube.com/watch?v=' + y['id'], y)
			)

class SpotifyMusic:
	def __init__(self, url : str):
		if not (re.match(sl, url) or re.match(s, url)):
			raise YoutubeTypeError('%s is not a youtube url' % (url))
		elif not re.match(s, url):
			raise YoutubeUrlError('%s is not a youtube list url' % (url))

		self.__url = url

	async def create(self) -> None:
		self.ytdl : Pytdl = Pytdl()
		s = (await self.ytdl.spotifyTrack(self.__url.split('/')[4]))[0]

		y = (await self.ytdl.resultList(s['title']))[0]
		self.music = YoutubeVideo(
			'http://www.youtube.com/watch?v=' + y['id'],
			y
		)

class YoutubeVideo:
	def __init__(self, url : str, data : JSON = {}):
		if not (re.match(yl, url) or re.match(y, url)):
			raise YoutubeTypeError('%s is not a youtube url' % (url))
		elif not re.match(y, url):
			raise YoutubeUrlError('%s is not a youtube list url' % (url))

		self.__url = url
		self.__data = data

	async def create(self) -> None:
		self.opt = {
			'format': 'bestaudio/best',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192'
			}]
		}

		data = self.__data
		with ydl.YoutubeDL(self.opt) as dl:
			info = dl.extract_info(self.__url, download=False)

		if len(data) != 0:
			self.id = data['id']
			self.title = data['title']
			self.duration = data['length']
			self.thumbnail = data['thumbnail']
		else:
			self.id = info['id']
			self.title = info['title']
			self.duration = dp(info['duration'])
			self.thumbnail = info['thumbnail']
		self.video_url = info['webpage_url']
		self.voice_url = info['url']
		self.stream = Stream(info['webpage_url'])

class Pytdl:
	__VideoSearchUrl = \
	'https://www.youtube.com/results?search_query=%s'
	__PlaylistSearchUrl = \
	'https://www.youtube.com/playlist?list=%s'
	__IdUrl = __NextSearchUrl = \
	'https://www.youtube.com/watch?v=%s'

	async def resultList(self, query : str) -> List[JSON]:
		return await get(
			self.__VideoSearchUrl % (quote(query)),
			Parser('search')
		)

	async def spotifyResultList(self, query : str) -> List[JSON]:
		return await spotifyGet(
			query,
			Parser('spotifyAlbum')
		)

	async def playList(self, list_id : str) -> List[JSON]:
		return await get(
			self.__PlaylistSearchUrl % (list_id),
			Parser('playlist')
		)

	async def spotifyPlayList(self, list_id : str) -> List[JSON]:
		return await spotifyGet(
			'/playlist/%s' % (list_id),
			Parser('spotifyList')
		)

	async def resultsList(self, querys : List[str]) -> List[List[JSON]]:
		return [(await self.resultList(q)) for q in querys]

	async def spotifyResultsList(self, querys : List[str]) -> List[List[JSON]]:
		return [(await self.spotifyResultList(q)) for q in querys]

	async def next(self, id : str) -> JSON:
		return await get(
			self.__NextSearchUrl % (id),
			Parser('video')
		)

	async def spotifyTrack(self, id : str) -> JSON:
		return await spotifyGet(
			'https://open.spotify.com/track/%s' % (id),
			Parser('spotifyTrack')
		)

	async def info(self, url : str) -> Union[YoutubeVideos, YoutubeVideo, SpotifyMusic, SpotifyMusics]:
		try:
			return YoutubeVideo(url)
		except YoutubeUrlError:
			return YoutubeVideos(url)
		except YoutubeTypeError:
			return SpotifyMusic(url)
		except SpotifyUrlError:
			return SpotifyMusics(url)
		except:
			raise UnKnownError('\'%s\' is not a correct url' \
			% url)