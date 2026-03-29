from pycoingecko import CoinGeckoAPI
from telegram import Bot
import asyncio
import time
import os

TOKEN = os.getenv("TELEGRAM_TOKEN")

# Retrive the price of a specific crypto (bitcoin)

def price_tracking():
	cg = CoinGeckoAPI()

	targets = {
		'bitcoin' : 40000,
	}

	met_targets = {}

	for crypto, crypto_target in targets.items():
		response = cg.get_price(ids = crypto, vs_currencies = 'gbp')
		current_price = response[crypto]['gbp']
		target_price = targets[crypto]

		if current_price >= target_price:
			met_targets[crypto] = current_price

	if met_targets:
		message_body = 'congrats, you made some money\n\n'
		for crypto, crypto_price in met_targets.items():
			current_price = crypto_price
			target_price = targets[crypto]
			message_body += (f'{crypto}\n'
					f'Current price:{current_price}\n'
					f'Target price: {target_price}\n\n'
					)

		asyncio.run(send_telegram_message(message_body))

async def send_telegram_message(message):
	bot_token = 'TOKEN'
	chatID = 'CHATID'

	bot = Bot(token = bot_token)
	await bot.send_message(chat_id = chatID, text = message)
	

while True:
	price_tracking()
	time.sleep(60)
