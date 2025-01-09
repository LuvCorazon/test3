from aiogram import Bot, Dispatcher, executor, types
from decouple import config
import logging
import os

token = config('TOKEN')

bot = Bot(token=token)
dp = Dispatcher(bot = bot)

Admins = [1093744655, ]

async def on_startup(_):
    for admin in Admins:
        await bot.send_message(chat_id=admin, text='bot activated')

@dp.message_handler(commands=['start'])
async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text=f'Hello {message.from_user.first_name}!\n'
                                f'Your tg id -{message.from_user.id}\n')


@dp.message_handler(commands=['meme'])
async def meme_handler(message: types.Message):
    photo_path = os.path.join('media', 'img.png')

    photo = open (photo_path, 'rb')

    await bot.send_photo(chat_id=message.from_user.id,
                         photo=photo,
                         caption = 'meme')

@dp.message_handler(lambda message: message.text.isdigit())  # Фильтруем сообщения, которые содержат только цифры
async def square_number_handler(message: types.Message):
    number = int(message.text)  # Преобразуем строку в целое число
    squared = number ** 2  # Возводим в квадрат
    logging.info(f"User {message.from_user.id} sent a number: {number}, squared result: {squared}")
    await message.answer(f"The square of {number} is {squared}")


@dp.message_handler()
async def echo_handler(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)


