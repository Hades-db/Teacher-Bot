# app/services/ai_engine.py

import aiohttp
from app.config import AI_KEY
from app.ui_text import AI_SYSTEM_PROMPT

async def ask_ai_mentor(user_message: str) -> str:
    """
    Отправляет асинхронный запрос напрямую к Google Gemini API (AI Studio).
    """
    # Твоя новейшая модель 
    model_name = "gemini-3.5-flash-lite"
    
    # Жесткий, точный URL без возможности склеивания путей
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={AI_KEY}"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    # Структура JSON payload для Google AI Studio
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": user_message}
                ]
            }
        ],
        # Наш токсичный батя-ментор в роли системной инструкции
        "systemInstruction": {
            "parts": [
                {"text": AI_SYSTEM_PROMPT}
            ]
        },
        "generationConfig": {
            "temperature": 1.0  # Для моделей 3.5 рекомендуется дефолтная температура 1.0
        }
    }

    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=headers, json=payload, timeout=30) as response:
                if response.status == 200:
                    data = await response.json()
                    # Извлекаем текст ответа из структуры Google API
                    return data['candidates'][0]['content']['parts'][0]['text']
                else:
                    error_text = await response.text()
                    print(f"Google API Error Status: {response.status}, Detail: {error_text}")
                    return "❌ Ошибка Google API. Ментор ушел на перекур, попробуй позже."
    except Exception as e:
        print(f"AI Engine Exception: {e}")
        return "❌ Не удалось связаться с ИИ-ментором. Проверь подключение к сети."
