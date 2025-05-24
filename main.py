from openai import OpenAI
import asyncio,os
import logging
import sys
from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.types import Message
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv("API")
dp = Dispatcher()
client = OpenAI(
  base_url="https://api.langdock.com/openai/eu/v1",
  api_key="sk-ybAKXXIEqd2Hh2u43r2D5alm5qSwp6rRqh-7fsjJkCU3ahbkIJ0qcER9CFDmT1BmpjSenRGUgxZKQhKW3fa8gQ"
)
def CHat(matin:str):
    completion = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": matin+" uzbecha ko`proq ma`lumot ber."}
        ]
    )
    return (completion.choices[0].message.content)

@dp.message(Command(commands=["start"]))
async def start_handler(message: Message):
    await message.answer(f"Assalomu allekum, {html.bold(message.from_user.full_name)}!")

@dp.message()
async def message_handler(message: Message):
    try:
        A:str = message.text
        await message.answer(CHat(A))
    except:
        await message.answer("Bu mavzu yo`q❌, boshqa yozing❗")


async def main():
    bot = Bot(token=TOKEN,default=DefaultBotProperties(parse_mode=ParseMode.HTML),)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format=f"%(asctime)s - %(name)s - %(levelname)s - %(message)s")
    logging.info("Bot is starting...")
    asyncio.run(main())






