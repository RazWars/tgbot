import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message

TOKEN = "8210584001:AAF4DECXKljI9Wz1QAgpu6YJWxppzst5_pE"
CHANNEL_ID = -1003906497582  # твой канал

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def forward_message(message: Message):
    # если текст
    if message.text:
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text=f"📩 Новое сообщение:\n\n{message.text}"
        )
    # если фото
    elif message.photo:
        await bot.send_photo(
            chat_id=CHANNEL_ID,
            photo=message.photo[-1].file_id,
            caption="📸 Новое фото"
        )
    # если что-то другое
    else:
        await bot.send_message(
            chat_id=CHANNEL_ID,
            text="📦 Новый файл или другой тип сообщения"
        )

async def main():
    print("Бот запущен 🚀")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
