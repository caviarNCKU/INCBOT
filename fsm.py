from transitions.extensions import GraphMachine
import test
import random

class TocMachine(GraphMachine):
	def __init__(self, **machine_configs):
		self.machine = GraphMachine(
			model = self,
			**machine_configs
		)

	def is_going_to_weather(self, update):
		text = update.message.text
		return text.lower() == 'weather'

	def is_going_to_financial(self, update):
		text = update.message.text
		return text.lower() == 'financial'

	def is_going_to_place(self, update):
		text = update.message.text
		return text.lower() == text.lower()

	def is_going_to_stock_number(self, update):
		text = update.message.text
		return text.lower() == text.lower()

	def is_going_to_game(self, update):
		text = update.message.text
		return text.lower() == 'game'

	def is_going_to_finger(self, update):
		text = update.message.text
		return text.lower() == text.lower() 

	def on_enter_game(self, update):
		if update.message.text == 'user':
			update.message.reply_text("Choose weather, financial, game")
			self.go_back(update)
		else:
			update.message.reply_text("paper,sissors,stone")
	def on_exit_game(self, update):
		print('Leaving game')

	def on_enter_finger(self, update):
		if update.message.text == 'user':
			pass
		else:
			temp = random.choice(['paper','sissors','stone'])
			update.message.reply_text(temp)
			if update.message.text == 'paper':
				if temp == 'stone':
					update.message.reply_text("You Win!")
				elif temp == 'paper':
					update.message.reply_text("Tie!")
				else:
					update.message.reply_text("You Lose")
			elif update.message.text == 'stone':
				if temp == 'sissors':
					update.message.reply_text("You Win!")
				elif temp == 'stone':
					update.message.reply_text("Tie!")
				else:
					update.message.reply_text("You Lose")
			else:
				if temp == 'paper':
					update.message.reply_text("You Win!")
				elif temp == 'sissors':
					update.message.reply_text("Tie!")
				else:
					update.message.reply_text("You Lose")
		self.go_back(update)

	def on_exit_finger(self, update):
		print('Leaving finger')

	def on_enter_weather(self, update):
		if update.message.text == 'user':
			update.message.reply_text("Choose weather, financial, game")
			self.go_back(update)
		else:
			update.message.reply_text("Press any word to show today's weather")

	def on_exit_weather(self, update):
		print('Leaving weather')

	def on_enter_financial(self, update):
		if update.message.text == 'user':
			update.message.reply_text("Choose weather, financial, game")
			self.go_back(update)
		else:
			update.message.reply_text("Your stock number is")

	def on_exit_financial(self, update):
		print('Leaving financial')

	def on_enter_place(self, update):
		if update.message.text == 'user':
			pass
		else:
			update.message.reply_text(test.Weather())
		self.go_back(update)	

	def on_exit_place(self, update):
		print('Leaving place')

	def on_enter_stock_number(self, update):
		if update.message.text == 'user':
			pass
		else:
			update.message.reply_text(test.getList(update.message.text))
		self.go_back(update)

	def on_exit_stock_number(self, update):
		print('Leaving stocknum')
