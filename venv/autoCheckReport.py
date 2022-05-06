import logging
import requests
import schedule
import time
import dk_token as dk
import httpconnection as hc

# Enable logging
logging.basicConfig(
    filename='autoCheckReport.log', 
    encoding='utf-8',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def bot_send_text(bot_message):
    
    bot_token = dk.TOKEN
    bot_chatID = dk.CHADID
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

    response = requests.get(send_text)

    return response.json()


def report():
    local_time = time.asctime(time.localtime(time.time()))

    if hc.connection(dk.RER_W) == 200:
        message = 'Todo Ok ' + local_time
        print(message)
    elif hc.connection(dk.RER_W) == -10:
        message = '❌ Error ' + dk.RER_W + ' (O no existe)'
        print('Error ' + dk.RER_N + ' Error ' + local_time)
        bot_send_text(message)
    else:
        message = '⚠️Web ' + dk.RER_N + ' Caida⚠️ ' + local_time
        print('Web ' + dk.RER_N + ' Caida ' + local_time)
        bot_send_text(message)
        bot_send_text("Código: " + hc.connection(dk.RER_W))


def check_bot_status():
    message = '✅ Bot funcionando 9:00'
    bot_send_text(message)
    

if __name__ == '__main__':
        
    schedule.every(5).minutes.do(report)
    schedule.every().day.at("09:00").do(check_bot_status)

    while True:
        schedule.run_pending()