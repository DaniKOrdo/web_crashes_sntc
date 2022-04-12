import requests
import schedule
import telebot
import tlg_token
import time;

# Entrada de mensaje /comando #

bot = telebot.TeleBot(tlg_token.token)

@bot.message_handler(commands = ['bot','Bot'])
def bot_activo(message):
    msg = ''' ✅ Bot activo '''
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=['status', 'estado', tlg_token.rraw])
def bot_status(message):
    msg = get_Web(tlg_token.rra)
    bot.send_message(message.chat.id, msg)

@bot.message_handler(commands=[tlg_token.sntw])
def bot_status(message):
    msg = get_Web(tlg_token.snt)
    bot.send_message(message.chat.id, msg)

def get_Web(web):
    localTime = time.asctime(time.localtime(time.time()))
    r = requests.get(web)
    if r.status_code == 200:
        return '✅ Staus Code: ' + str(r.status_code)
    return '❌ Staus Code: ' + str(r.status_code) + ' ' + localTime


# Mensajes automaticos  #

def bot_send_text(bot_message):
    
    bot_token = tlg_token.token
    bot_chatID = tlg_token.chatID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response

def report():
    localTime = time.asctime(time.localtime(time.time()))
    r = requests.get(tlg_token.rra)
    if r.status_code != 200:
        message = '⚠️Web ' + tlg_token.rraw + ' caida: ' + str(r.status_code)
        bot_send_text(message)
    else:
        bot_send_text("Ok")
        print('Todo ok: ' + localTime)

def check_bot_status():
    message = '✅ Bot funcionando'
    bot_send_text(message)

# __main__ #

if __name__ == '__main__':

    schedule.every(5).minutes.do(report)
    schedule.every().day.at("09:00").do(check_bot_status)
    bot.polling(none_stop=True)

    while True:
        schedule.run_pending()