from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery
from app.keyboards.inline import MAIN_KB
from app import ui_text

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(ui_text.START_TEXT, reply_markup=MAIN_KB)


@router.callback_query(F.data == "back_to_main")
async def back_to_main(callback: CallbackQuery):
    await callback.message.edit_text(ui_text.START_TEXT, reply_markup=MAIN_KB)
    await callback.answer()


@router.callback_query(F.data == "edu_profile")
async def cmd_profile(callback: CallbackQuery):
    user = callback.from_user
    user_info = (
        "👤 **Твой цифровой профиль**\n\n"
        f"✨ Рад видеть тебя, {user.full_name}!\n\n"
        f"🆔 **ID:** `{user.id}`\n"
        f"📛 **Имя:** {user.full_name}\n"
        f"🔗 **Юзернейм:** @{user.username if user.username else 'не установлен'}\n\n"
        "💡 *Здесь хранятся твои цифровые следы обучения.*"
    )
    from app.keyboards.inline import DONATE_KB # локальный импорт во избежание циклов
    from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
    
    back_kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")]
    ])
    
    await callback.message.edit_text(user_info, reply_markup=back_kb, parse_mode="Markdown")
    await callback.answer()

@router.callback_query(F.data == "edu_donate")
async def cmd_donate(callback: CallbackQuery):
    from app.keyboards.inline import DONATE_KB
    await callback.message.edit_text(ui_text.DONATE_TEXT, reply_markup=DONATE_KB)
    await callback.answer()