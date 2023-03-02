import json

from aiohttp import ClientSession
from bot.schemas import Location


async def get_location():
    data: dict = {}
    async with ClientSession() as session:
        async with session.get("https://ipinfo.io/json") as response:
            resp = json.loads(await response.text())["loc"].split(",")
            data["latitude"] = resp[0]
            data["longitude"] = resp[1]
            return resp


async def get_weather(*, lat: float, lon: float, api_key: str, part: str = "current") -> dict:
    async with ClientSession() as session:
        async with session.get(
                f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}") as response:
            resp = json.loads(await response.text())
            return resp
