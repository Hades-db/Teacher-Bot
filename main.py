import asyncio
from aiogram import Bot, Dispatcher
from app.config import TOKEN
from app.handlers import commands, education

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(commands.router)
    dp.include_router(education.router)

    await bot.delete_webhook(drop_pending_updates=True)

    try:
        print("Teacher-Bot AI Agent started successfully!")
        await dp.start_polling(bot)
    except (KeyboardInterrupt, SystemExit):
        print("\nBot stopped manually.")
    except Exception as ex:
        print(f"Critical Bot Exception: {ex}")
    finally:
        await bot.session.close()
        print("Bot completely shut down.")

if __name__ == "__main__":
    asyncio.run(main())