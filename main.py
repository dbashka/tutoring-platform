import asyncio
from aiogram import Bot, Dispatcher
from config import BOT_TOKEN
from utils.db_utils import init_db
from handlers import start_handler

async def main():
    # Ініціалізуємо базу
    await init_db()

    # Запускаємо бота
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.include_router(start_handler.router)

    print("🤖 Бот запущено...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())