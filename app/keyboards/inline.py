from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from app.ui_text import START_TEXT


MAIN_KB = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🚀 Начать Обучение", callback_data="edu_menu")],
        [InlineKeyboardButton(text="👤 Мой Профиль", callback_data="edu_profile")],
        [InlineKeyboardButton(text="☕ На чай ментору", callback_data="edu_donate")]
    ]
)


MAIN_THEMES = [
    "Верстка", "JavaScript", "PHP", "TypeScript", "NodeJS", "Python", "Java", "C++",
    "Rust", "Kotlin", "SQL", "Vue", "React", "Angular", "Next", "jQuery", "Laravel",
    "Git", "Webpack", "Gulp", "Terminal", "Internet", "Деплой", "Глоссарий", "Сленг"
]

def get_education_keyboard() -> InlineKeyboardMarkup:
    buttons = []
    for theme in MAIN_THEMES:
        buttons.append(InlineKeyboardButton(text=theme, callback_data=f"theme_{theme}"))
    
    rows = [buttons[i:i + 3] for i in range(0, len(buttons), 3)]
    
    rows.append([InlineKeyboardButton(text="🔙 Назад в меню", callback_data="back_to_main")])
    
    return InlineKeyboardMarkup(inline_keyboard=rows)

DONATE_KB = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="💵 Elcart", url="https://payqr.kg#00020101021132700013p2p.elcart.kg010111032b230f418481d524f8761a86b048e432712021113021253034175204482259199417%20****%20****%2093036304EA0B"),
            InlineKeyboardButton(text="💸 MBank", url="https://mbank.kg")
        ],
        [InlineKeyboardButton(text="🔙 Назад", callback_data="back_to_main")]
    ]
)

def get_back_to_edu_keyboard() -> InlineKeyboardMarkup:
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text="🔙 К списку технологий", callback_data="edu_menu")]
        ]
    )