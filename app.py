import sys
import configparser
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine

config = configparser.ConfigParser()
config.read('config.ini')

API_TOKEN = config['TELEGRAM']['ACCESS_TOKEN']
WEBHOOK_URL = config['TELEGRAM']['WEBHOOK_URL'] + '/hook'

app = Flask(__name__)
bot = telegram.Bot(API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'weather',
        'financial',
		'place',
		'stock_number',
		'game',
		'finger'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'weather',
            'conditions': 'is_going_to_weather'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'financial',
            'conditions': 'is_going_to_financial'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'game',
            'conditions': 'is_going_to_game'
        },
		{
            'trigger': 'advance',
            'source': 'weather',
            'dest': 'place',
            'conditions': 'is_going_to_place'
        },
		{
            'trigger': 'advance',
            'source': 'financial',
            'dest': 'stock_number',
            'conditions': 'is_going_to_stock_number'
        },
		{
            'trigger': 'advance',
            'source': 'game',
            'dest': 'finger',
            'conditions': 'is_going_to_finger'
        },	
        {
            'trigger': 'go_back',
            'source': [
                'weather',
                'financial',
				'game'
            ],
            'dest': 'user'
        },
        {
            'trigger': 'go_back',
            'source': [
				'place'
            ],
            'dest': 'weather'
        },
        {
            'trigger': 'go_back',
            'source': [ 
				'stock_number'
            ],
            'dest': 'financial'
        },
         {
            'trigger': 'go_back',
            'source': [
				'finger'
            ],
            'dest': 'game'
        }       
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
