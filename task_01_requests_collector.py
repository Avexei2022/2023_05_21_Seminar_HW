import datetime
from telebot import types
import telebot



API_TOKEN = ''
bot = telebot.TeleBot(API_TOKEN)

markup = types.ReplyKeyboardMarkup(row_width=1)
btn_request = types.KeyboardButton('Обращение')
markup.add(btn_request)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(mes):
    bot.send_message(mes.from_user.id,
                     f"Привет {mes.from_user.first_name}! Я бот - Супер помощник.\n"+
                     " Для обращения в службу техподдержки набери слово 'обращение'."
                     , reply_markup=markup)
    


@bot.message_handler(func=lambda message: message.text.lower() == "обращение")
def reguest_collector(mes):
    bot.send_message(mes.chat.id, 'Задай вопрос или опиши проблему')
    bot.register_next_step_handler(mes, reguest_step)


def reguest_step(m):
    data = open('reguests.txt', mode='a', encoding='utf-8')
    text = f'0 &*& {datetime.datetime.now()} &*& {m.from_user.id} &*& {m.from_user.first_name} &*& {m.text}\n'
    data.write(text)
    data.close()
    bot.send_message(m.chat.id,
                     f'Уважемый {m.from_user.first_name}! Твое обращение:\n {m.text}\n'+
                    'направлено в техподдержку. Ответ направят в ближайшее время.\n'+
                    'Спасибо за обращение!')
    return



bot.polling()
