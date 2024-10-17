import RPi.GPIO as GPIO
import time
import telepot
from telepot.loop import MessageLoop
GPIO.setmode(GPIO.BOARD)
led = 12
GPIO.setup(led, GPIO.OUT)
token = '7759172637:AAFmWct5zFM-3A8lwv_QDPzSKKHWghl2SRM'
bot = telepot.Bot(token)
chat_id = '1601831087'
print(bot.getMe())

def bot_action(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    print(f'Received: {command}')
    if 'on' in command:
        message = 'LED on'
        GPIO.output(led, True)
        time.sleep(2)
        bot.sendMessage(chat_id, message)
    elif 'off' in command:
        message = 'LED off'
        GPIO.output(led, False)
        time.sleep(2)
        bot.sendMessage(chat_id, message)
MessageLoop(bot, bot_action).run_as_thread()
print('Bot is running...')
try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    print("Cleaning up GPIO...")
		    GPIO.cleanup()
