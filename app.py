import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '531101905:AAHvcXLR4j6Vfti-0Zu4PhnkXgFqZVAaba0'
WEBHOOK_URL = 'https://dec41a82.ngrok.io/show-fsm'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'weather',
        'financial',
		'sport',
		'place',
		'stock_number',
		'nba123',
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
            'source': 'user',
            'dest': 'sport',
            'conditions': 'is_going_to_sport'
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
            'source': 'sport',
            'dest': 'nba123',
            'conditions': 'is_going_to_nba123'
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
				'sport',
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
				'nba123'
            ],
            'dest': 'sport'
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
    app.run(port = 8443)
