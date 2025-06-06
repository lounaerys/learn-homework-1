"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import ephem
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')

# старый прокси не работает, но оставила все, как есть, хоть здесь и выдает ошибку.
# добавила код в своего тг-бота и он, в принципе, рабочий.

PROXY = {
    'proxy_url': 'socks5://t1.learn.python.ru:1080',
    'urllib3_proxy_kwargs': {
        'username': 'learn',
        'password': 'python'
    }
}


def greet_user(update, context):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text('Привет! Я умею определять, в каком созвездии сейчас находится планета. ' \
    'Для этого набери в чате команду /planet и название планеты на английском, например "/planet Mercury"')


def talk_to_me(update, context):
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(text)

def planet_command(update, context):
    command_parts = update.message.text.split()

    if len(command_parts) < 2:
        return
    
    planet_name = command_parts[1].capitalize()

    if planet_name == 'Mars':
        planet = ephem.Mars()
    elif planet_name == 'Venus':
        planet = ephem.Venus()
    elif planet_name == 'Jupiter':
        planet = ephem.Jupiter()
    elif planet_name == 'Saturn':
        planet = ephem.Saturn()
    elif planet_name == 'Mercury':
        planet = ephem.Mercury()
    elif planet_name == 'Uranus':
        planet = ephem.Uranus()
    elif planet_name == 'Neptune':
        planet = ephem.Neptune()
    elif planet_name == 'Pluto':
        planet = ephem.Pluto()
    else:
        return
    
    planet.compute()
    constellation = ephem.constellation(planet)
    update.message.reply_text(f'Планета {planet_name} сейчас в созвездии {constellation}')


def main():
    mybot = Updater("КЛЮЧ, КОТОРЫЙ НАМ ВЫДАЛ BotFather", request_kwargs=PROXY, use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler('planet', planet_command))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()

