import asyncio
from datetime import datetime

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher

from dependencies.depends import get_location, get_weather

from bot.config import TOKEN, WEATHER_API_KEY
from bot.schemas import Temperature, Wind, Sun, WindDirection
from bot.keyboard import keyboard

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

latitude, longitude = asyncio.run(get_location())
data = asyncio.run(get_weather(lat=latitude, lon=longitude, api_key=WEATHER_API_KEY))
print(data)


@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.answer("Выберите то, что хотите узнать", reply_markup=keyboard)


@dp.callback_query_handler(text='btn_wind')
async def process_callback_button1(callback_query: types.CallbackQuery):
    if dt := data.get("wind"):
        wind: Wind = Wind(**dt)
        degrees = round(wind.deg / 45) * 45
        degrees = 0 if degrees == 360 else degrees
        response = f'Скорость ветра {wind.speed}м/с\n' \
                   f'Направление ветра {WindDirection(degrees).name}'
    else:
        response = "Не удалось получить данные от сервиса погоды\n" \
                   "Пожалуйста, попробуйте  позже"
    await callback_query.message.answer(text=response, reply_markup=keyboard)


@dp.callback_query_handler(text='btn_main')
async def get_temperature(callback_query: types.CallbackQuery):
    if dt := data.get("main"):
        temp: Temperature = Temperature(**dt)
        response = f'Температура за бортом {temp.temp - 273.15: .2f}℃\n' \
                   f'Ощущаешься как {temp.feels_like - 273.15: .2f}℃\n' \
                   f'Максимальная {temp.temp_max - 273.15: .2f}℃\n' \
                   f'Минимальная {temp.temp_min - 273.15: .2f}℃\n' \
                   f'Атмосферное давление {temp.pressure}гПа\n' \
                   f'Влажность {temp.humidity}%'
    else:
        response = "Не удалось получить данные от сервиса погоды\n" \
                   "Пожалуйста, попробуйте  позже"
    await callback_query.message.answer(text=response, reply_markup=keyboard)


@dp.callback_query_handler(text='btn_sun')
async def get_sunrise(callback_query: types.CallbackQuery):
    if dt := data.get("sys"):
        sun: Sun = Sun(**dt)
        response = f'Восход в AM{datetime.fromtimestamp(sun.sunrise).strftime("%I:%M:%S")}\n' \
                   f'Закат в PM{datetime.fromtimestamp(sun.sunset).strftime("%I:%M:%S")}'
    else:
        response = "Не удалось получить данные от сервиса погоды\n" \
                   "Пожалуйста, попробуйте  позже"

    await callback_query.message.answer(text=response, reply_markup=keyboard)
