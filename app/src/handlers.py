from aiogram import Router, F

from aiogram.filters import CommandStart
from aiogram.types import Message

from buttons import Buttons
from get_text import menu_text, contact_text

router = Router()

@router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"{menu_text}", 
                         reply_markup=Buttons.menu_button)


@router.message(F.text == 'Contact')
async def get_contact_page(message: Message) -> None:
    await message.answer(f'{contact_text}', reply_markup=Buttons.contact_button)


@router.message(F.text == 'Cart 🛒')
async def get_busket_page(message: Message) -> None:
    await message.answer('это часть магазина корзина')

