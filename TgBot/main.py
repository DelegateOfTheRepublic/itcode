import telebot
from telebot import types
from random import randint

bot = telebot.TeleBot('6192049448:AAGv4XQWI4ijeSw5MMCYDx9BETvR8-HOe-8')

ACTIONS = {
    'encrypt': 'Зашифровать сообщение',
    'decrypt': 'Расшифровать сообщение'
}

ERROR_MESSAGES = [
    'Увы, но это не подойдет...',
    'Мистер, обратите внимание на: [Теперь дай мне любое число]',
    '...',
    'Это должно быть число'
]

user_text = None
current_action = None

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Зашифровать сообщение")
    btn2 = types.KeyboardButton("Расшифровать сообщение")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Salve, {0.first_name}! Я скрытописец!".format(message.from_user), reply_markup=markup)
    bot.send_message(message.chat.id, text="Дай мне текст и выбери, что я должен с ним сделать...")

@bot.message_handler(func=lambda message: not message.text in ACTIONS.values())
def get_text(message, text = None):
     global user_text

     if user_text is None:
          user_text = message.text

@bot.message_handler(func=lambda message: message.text in ACTIONS.values())
def get_cipher_step(message, text=None):
    global user_text, current_action

    if user_text is None:
        bot.send_message(message.from_user.id, text='Для начала дай мне текст, только потом выбирай...')
        return
    msg = bot.send_message(message.from_user.id, text="Теперь дай мне любое число")

    if current_action is None:
         current_action = message.text

    if current_action == ACTIONS['encrypt']:
         bot.register_next_step_handler(msg, get_encrypted_text, user_text)
    elif current_action == ACTIONS['decrypt']:
         bot.register_next_step_handler(msg, get_encrypted_text, user_text, is_decrypt=True)


def get_encrypted_text(message, text: str, is_decrypt: bool = False):
    global user_text

    cipher_status_message = 'Шифрую текст...' if not is_decrypt else 'Расшифровываю текст...'
    cipher_result_message = 'Ваше зашифрованное сообщение, domine:' if not is_decrypt else 'Ваше расшифрованное сообщение, domine:'

    try:
        if not message.text.lstrip('-').isdigit():
            raise ValueError
        cipher_step = int(message.text)
    except ValueError:
            bot.send_message(message.from_user.id, text=ERROR_MESSAGES[randint(0, len(ERROR_MESSAGES))-1])
            get_cipher_step(message, text)
            return

    cipher_text = ''
    bot.send_message(message.from_user.id, text=cipher_status_message)
    for ch in text:
            cipher_text += chr(ord(ch) + cipher_step)

    bot.send_message(message.from_user.id, text=f'{cipher_result_message}  {cipher_text}')
    user_text = None

bot.polling(none_stop=True)