from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import sys
import os
import logging
import asyncio

load_dotenv()
API_TOKEN = os.getenv('BOT_TOKEN')

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message : Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}-!")

async def main() -> None:
    bot = Bot(token=API_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())