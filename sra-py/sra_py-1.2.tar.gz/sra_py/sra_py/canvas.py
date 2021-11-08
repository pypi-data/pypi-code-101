import requests
import io
import aiohttp

SR = "https://some-random-api.ml/canvas/"

async def invert(avatar_url: str):
	async with aiohttp.ClientSession() as se:
		async with se.get(f"https://some-random-api.ml/canvas/invert?avatar={avatar_url}") as img:
			im = io.BytesIO(await img.read())
			await se.close()

	return im

async def wasted(avatar_url: str):
	async with aiohttp.ClientSession() as se:
		async with se.get(f"https://some-random-api.ml/canvas/wasted?avatar={avatar_url}") as img:
			im = io.BytesIO(await img.read())
			await se.close()

	return im

async def jail(avatar_url: str):
	async with aiohttp.ClientSession() as se:
		async with se.get(f"https://some-random-api.ml/canvas/jail?avatar={avatar_url}") as img:
			im = io.BytesIO(await img.read())
			await se.close()

	return im

async def mission_passed(avatar_url: str):
	async with aiohttp.ClientSession() as se:
		async with se.get(f"https://some-random-api.ml/canvas/passed?avatar={avatar_url}") as img:
			im = io.BytesIO(await img.read())
			await se.close()

	return im

async def glass(avatar_url: str):
	async with aiohttp.ClientSession() as se:
		async with se.get(f"https://some-random-api.ml/canvas/glass?avatar={avatar_url}") as img:
			im = io.BytesIO(await img.read())
			await se.close()

	return im

async def comrade(avatar_url: str):
	async with aiohttp.ClientSession() as se:
		async with se.get(f"https://some-random-api.ml/canvas/comrade?avatar={avatar_url}") as img:
			im = io.BytesIO(await img.read())
			await se.close()

	return im

async def simpcard(avatar_url: str):
	async with aiohttp.ClientSession() as se:
		async with se.get(f"https://some-random-api.ml/canvas/simpcard?avatar={avatar_url}") as img:
			im = io.BytesIO(await img.read())
			await se.close()

	return im

async def blur(avatar_url: str):
	async with aiohttp.ClientSession() as se:
		async with se.get(f"https://some-random-api.ml/canvas/blur?avatar={avatar_url}") as img:
			im = io.BytesIO(await img.read())
			await se.close()

	return im

async def pixelate(avatar_url: str):
	async with aiohttp.ClientSession() as se:
		async with se.get(f"https://some-random-api.ml/canvas/pixelate?avatar={avatar_url}") as img:
			im = io.BytesIO(await img.read())
			await se.close()

	return im