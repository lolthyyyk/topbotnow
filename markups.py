from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


btnMain = KeyboardButton('⬅️Главное меню')


#main menu
btnRandom = KeyboardButton('❇️Рандомное число')
btnOther = KeyboardButton('♦️Другое')
btnfilm = KeyboardButton('🟪️Порекомендовать фильм')
mainMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnRandom, btnOther, btnfilm)

#other menu
btnInfo = KeyboardButton('📊Информация')
btnMoney = KeyboardButton('🖥Время создания бота')
otherMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnInfo, btnMoney, btnMain)

#film menu

btnKino = KeyboardButton('✅Дальше')
kinoMenu = ReplyKeyboardMarkup(resize_keyboard = True).add(btnKino, btnMain)

#knopka
mainInline = InlineKeyboardMarkup(row_width=2)
btnRight = InlineKeyboardButton(text='▶️Дальше', callback_data='btnRight')

mainInline.insert(btnRight)