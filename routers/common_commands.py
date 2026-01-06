from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router(name="common_commands")

@router.message(Command("help"))
async def cmd_help(message: Message) -> None:
    text_message="""
    Привет, просто отправь мне фото чека
    """
    await message.answer(text=text_message)

@router.message(Command("start"))
async def cmd_help(message: Message) -> None:
    await message.answer("Привет, я бот, который помогает сканировать чеки и вести твой бюджет, просто отправь мне фото чека и я его распаршу и сохраню в базу")