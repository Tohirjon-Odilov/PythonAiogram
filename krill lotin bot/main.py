import asyncio
from typing import Union
import logging
import sys
from tracemalloc import BaseFilter
# Kodni @AiogramUzDev yozdi
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from translitirate import to_cyrillic, to_latin

TOKEN = "6726534448:AAFZeQSAhl8vBlfE2dKdiN4dvEcPBaIa0QE"

dp = Dispatcher()

class ContentTypesFilter(BaseFilter):
 def __init__(self, content_types: Union[str, list]):
     self.content_types = content_types
 async def __call__(self, message: Message) -> bool:
     if isinstance(self.content_types, str):
         print(message)
         return message.content_type == self.content_types
     else:
         return message.content_type in self.content_types


@dp.message(CommandStart())
async def command_start_handler(message: Message):
 await message.answer(f"Salom {message.from_user.full_name} Lotin krill botiga xush kelibsiz\nIltimos menga krillcha yoki lotincha so'z yuboring men uni almashtirib beraman 🔄")


@dp.message(ContentTypesFilter(content_types=['text']))
async def translit(message: types.Message):
 text = message.text
 response = to_cyrillic(text) if text.isascii() else to_latin(text)
 await message.answer(response)
 print(f"user -> Fore.GREEN{message.from_user.full_name}Fore.RESET, sended message -> Fore.RED{message.text}Fore.RESET")

async def main():
 bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
 await dp.start_polling(bot)


if __name__ == "__main__":
 logging.basicConfig(level=logging.INFO, stream=sys.stdout)
 asyncio.run(main())
