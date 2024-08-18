import telebot
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
import cryptocompare as cc

cryptocompare_API_key = 'a3025b6d7a2472633c9b5345b9228dbd'
cc.cryptocompare._set_api_key_parameter(cryptocompare_API_key)

bot = telebot.TeleBot('6789972418:AAENfEGvgOrJDySlYvV4YAOxBsBxiwhqhFY')

channel_1_button = InlineKeyboardButton(text='freeairdropland1', url='https://t.me/freeairdropland1')
launch_button = InlineKeyboardButton(text='دریافت کلید🔑', url='https://t.me/Hamsterfrkeysbot/Key')
keyboard_channel_button = InlineKeyboardMarkup(row_width=1)
keyboard_channel_button.add(channel_1_button)
keyboard_launch = InlineKeyboardMarkup()
keyboard_launch.add(launch_button)

def is_user_member(user_id):
    try: 
        member = bot.get_chat_member(chat_id=CHANNEL_NAME, user_id=user_id)
        if member.status in ['member', 'administrator', 'creator']:
            return True
    except Exception as e:
        print(f'Error: {e}')


@bot.message_handler(commands=['start'])
def start_reply(message):
    user_id = message.from_user.id
    if is_user_member(user_id):
        bot.send_message(message.chat.id, '''
برای استفاده از ربات لطفا در کانال زیر عضو شوید
                         
پس از عضویت بر روی /join کلیک کنید


        ''', reply_markup=keyboard_channel_button)
    else:
        bot.send_message(message.chat.id, '''

رای استفاده از ربات لطفا در کانال زیر عضو شوید
                         
پس از عضویت بر روی /join کلیک کنید
    
        ''', reply_markup=keyboard_channel_button)

CHANNEL_NAME = '@freeairdropland1' 

@bot.callback_query_handler(func=lambda call:True)
def check_join_button(call):
    if call.data == 'done':
        bot.answer_callback_query(call.id, '''لطفا دستور زیر را ارسال کنید 
/join     
                                  ''', show_alert=True)
    
def is_user_member(user_id):
    try: 
        member = bot.get_chat_member(chat_id=CHANNEL_NAME, user_id=user_id)
        if member.status in ['member', 'administrator', 'creator']:
            return True
    except Exception as e:
        print(f'Error: {e}')

@bot.message_handler(commands='join')
def check_join(message):
    user_id = message.from_user.id
    if is_user_member(user_id):
        bot.send_message(message.chat.id, ''' 
🇬🇧This Bot Provides  Hamster Kombat 3d bike Key Codes For Free 

🇮🇷این ربات بصورت رایگان کد های کلید همستر را در اختیار شما قرار میدهد. 

🇷🇺 Этот робот бесплатно предоставит вам коды ключей хомяка.

 Coded by @freeairdropland1
 
                         ''', reply_markup=keyboard_launch)
    else:
        bot.send_message(message.chat.id, 'شما هنوز عضو نشدید')


bot.polling()
