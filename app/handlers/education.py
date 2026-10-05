from aiogram import Router, F
from aiogram.types import CallbackQuery, Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from app.keyboards.inline import get_education_keyboard, get_back_to_edu_keyboard
from app.services.ai_engine import ask_ai_mentor

router = Router()

class EducationStates(StatesGroup):
    waiting_for_answer = State()

@router.callback_query(F.data == "edu_menu")
async def show_edu_menu(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    text = (
        "🚀 **Твой интерактивный класс обучения**\n\n"
        "Выбери технологию или язык программирования, который хочешь разобрать. "
        "Твой AI-ментор мгновенно подготовит краткую выжимку теории, пример кода "
        "и выдаст тебе персональное практическое задание! 🔥"
    )
    await callback.message.edit_text(text, reply_markup=get_education_keyboard(), parse_mode="Markdown")
    await callback.answer()

@router.callback_query(F.data.startswith("theme_"))
async def handle_theme_selection(callback: CallbackQuery, state: FSMContext):
    theme_name = callback.data.split("_")[1]
    
    await callback.message.edit_text(f"⏳ *Ментор изучает твой запрос по теме '{theme_name}' и пишет лекцию...*", parse_mode="Markdown")
    
    prompt = f"Я хочу изучить технологию/тему: '{theme_name}'. Дай мне вводную лекцию по этой теме и практическое задание."
    ai_response = await ask_ai_mentor(prompt)
    
    await state.update_data(current_theme=theme_name)
    await state.set_state(EducationStates.waiting_for_answer)
    
    await callback.message.edit_text(
        text=ai_response,
        reply_markup=get_back_to_edu_keyboard(),
        parse_mode="Markdown"
    )
    await callback.answer()

@router.message(EducationStates.waiting_for_answer, F.text & ~F.text.startswith("/"))
async def handle_user_code_or_answer(message: Message, state: FSMContext):
    placeholder = await message.answer("⏳ *Ментор смотрит твой код/ответ и готовит разбор...*", parse_mode="Markdown")
    
    user_data = await state.get_data()
    theme_name = user_data.get("current_theme", "Общее программирование")
    
    full_prompt = (
        f"Контекст: Пользователь изучает тему '{theme_name}'.\n"
        f"Вот задание, которое ты ему дал ранее. Он прислал следующий ответ/код на проверку:\n\n"
        f"{message.text}\n\n"
        f"Проверь этот код согласно своим правилам характера (сделай сочное код-ревью с матами к месту) "
        f"и в конце обязательно выдай СЛЕДУЮЩЕЕ микро-задание по этой же теме."
    )
    
    ai_response = await ask_ai_mentor(full_prompt)
    
    await placeholder.edit_text(
        text=ai_response,
        reply_markup=get_back_to_edu_keyboard(),
        parse_mode="Markdown"
    )