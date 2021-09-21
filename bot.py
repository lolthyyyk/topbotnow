from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import markups as nav

import random
 
bot = Bot(token='bb')
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply("Привет!\nНапиши мне что-нибудь!", reply_markup = nav.mainMenu)
    
def kinofilmik():
    andint

@dp.message_handler()
async def bot_message(message: types.Message):
    #await bot.send_message(message.from_user.id, message.text)
    if message.text == '❇️Рандомное число':
        await bot.send_message(message.from_user.id, 'Ваше число: ' + str(random.randint(100, 9999)))
        
    elif message.text == '⬅️Главное меню':
        await bot.send_message(message.from_user.id, '⬅️Главное меню', reply_markup =nav.mainMenu)
        
    elif message.text == '♦️Другое':
        await bot.send_message(message.from_user.id, '♦️Другое', reply_markup =nav.otherMenu)
    
    elif message.text == '🖥Время создания бота':
        await bot.send_message(message.from_user.id, 'На данный момент бот делается 3 дня!')
        
    elif message.text == '📊Информация':
        await bot.send_message(message.from_user.id, 'Бот подскажет новинки фильмов, порекомендует по рейтингу и сделает ваш вечер незабываемым. В будующем в базе будет более 100 новинок и крутых киношедевров!')
        
    elif message.text == '🟪️Порекомендовать фильм':
        await bot.send_message(message.from_user.id, '♦️Другое', reply_markup =nav.kinoMenu)
        
    elif message.text == '✅Дальше':
        await bot.send_message(message.from_user.id, 'Ваш фильм:')
        
    
    else:
        await message.reply('Неизвестная команда!')
        

if __name__ == '__main__':
    executor.start_polling(dp)