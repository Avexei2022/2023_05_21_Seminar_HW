import telebot

txt_file = 'reguests.txt'


def bot_init():
    API_TOKEN = ''
    bot = telebot.TeleBot(API_TOKEN)
    return bot


def read_files():
    data = open(txt_file, mode='r', encoding='utf-8')
    rows = data.read().split("\n")
    data.close()
    return rows


def check_rows():
    rows = read_files()
    for i in range(len(rows)-1):
        current_msg = (rows[i].split(" &*& "))
        create_message(current_msg)


def create_message(current_msg):
    if current_msg[0] == "0":
        print(f'\nНовое обращение от пользователя: {current_msg[3]}\n' +
              f'Текст обращения: "{current_msg[4]}"\n')
        operator_msg = input("\nВведите ответ: ")
        print(f'\nНа обращение: "{current_msg[4]}"\n' +
              f'\nПодготовлен ответ: "{operator_msg}"\n')
        check_out = input('Для отправки сообщения введите "Да"\n' +
                          'Для пропуска данного обращения введите введите любые символы.\n' +
                          '\nОтправить? ')
        if check_out.lower() == "да":
            sender_answer(current_msg, operator_msg)


def sender_answer(current_msg, operator_msg):
    bot = bot_init()
    bot.send_message(current_msg[2], f'Уважаемый {current_msg[3]}!\n' +
                     f'На Ваше обращение: "{current_msg[4]}"\n' +
                     f'Отвечаем следующее: "{operator_msg}"')
    replace_message(current_msg)


def replace_message(current_msg):
    with open(txt_file, 'r') as f:
        old_data = f.read()
        new_data = old_data.replace(
            f'0 &*& {current_msg[1]} &*& {current_msg[2]}', f'1 &*& {current_msg[1]} &*& {current_msg[2]}')
    with open(txt_file, 'w') as f:
        f.write(new_data)

print('Старт сервиса подготовки ответов на обращения.\n')
check_rows()
print('Сервис завершил работу.\n')
