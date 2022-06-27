import logging
from bs4 import BeautifulSoup
from array import *
import requests
from aiogram import Bot, types, executor, Dispatcher
from aiogram.dispatcher.filters import Text
import aiogram.utils.markdown as fmt
from aiogram import types
import aiogram.utils.markdown as fmt
bot = Bot(token='5418995392:AAEJ98Pv1FdTYQKrxd7lhax8Zm0vhIPiCy0')
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)
url = 'https://quote.rbc.ru/ticker/181206'
page = requests.get(url)
print(page.status_code)
filteredNews = []
allNews = []
soup = BeautifulSoup(page.text, "html.parser")
print(soup)
allNews = soup.findAll('a', class_='g-item__title')
for data in filteredNews:
    print(data)        
@dp.message_handler(commands=["start"])
async def start(message:types.Message):
    await message.reply("Вас приветсвует поисковой бот,функции бота ниже")
    await message.answer(
        fmt.text(
            fmt.text("start"),
            fmt.text("next"),
            fmt.text("help"),
            fmt.text("compare"),
            fmt.text("info"),
            fmt.text("news"),
            sep="\n"
        ), parse_mode="HTML"
    )
@dp.message_handler(commands=["news"])
async def start(message:types.Message):
    await message.reply("свежие новости")
    await message.answer(
        fmt.text(
            fmt.text("Цена газа в Европе превысила $1500 за тыс. кубометров"),
            fmt.text("Ирак может нарастить поставки нефти в ЕС на фоне сокращения импорта из РФ"),
            fmt.text("Цена нефти Brent упала на 5% и опустилась ниже $109 впервые с 19 мая"),
            sep="\n"
        ), parse_mode="HTML"
    )
@dp.message_handler(commands=["info"])
async def start(message:types.Message):
    await message.reply("По данным Министерства нефти и газа Республики Казахстан, доказанные запасы нефти и газового конденсата в стране достигают 39,8 миллиардов баррелей (примерно 5,3 миллиардов тонн). При сохранении текущего уровня производства и неизменном объёме запасов добыча нефти и газа в стране может длиться в течение 70 лет. ")    
@dp.message_handler(commands=["compare"])
async def start(message:types.Message):
    await message.reply("сравнение цен")
    await message.answer(
        fmt.text(
            fmt.text("ср.цена за прошлый год:82.25"),
            fmt.text("ср.цена за этот год:109.05"),
            fmt.text("изм:+27"),
            sep="\n"
        ), parse_mode="HTML"
    )
@dp.message_handler(commands="next")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["цены на нефть WTI", "цены на нефть BRENT"]
    keyboard.add(*buttons)
    await message.answer("помощь", reply_markup=keyboard)
@dp.message_handler(Text(equals="цены на нефть WTI"))
async def with_puree(message: types.Message):
    await message.reply("107.06")
@dp.message_handler(Text(equals="цены на нефть BRENT"))
async def with_puree(message: types.Message):
    await message.reply("110.04")
@dp.message_handler(commands="help")
async def cmd_inline_url(message: types.Message):
    buttons = [
        types.InlineKeyboardButton(text="BRANT", url="https://ru.investing.com/commodities/brent-oil"),
        types.InlineKeyboardButton(text="Performance", url="https://www.profinance.ru/chart/brent/")
    ]
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(*buttons)
    await message.answer("информация о нефти", reply_markup=keyboard)

if __name__=="__main__":
    executor.start_polling(dp, skip_updates=True)
    

