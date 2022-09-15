def command(x):
	text = x
	new_text=""
	for i in text:
		if i != "$":
			new_text += i
		else:
			pass
	new_text = new_text.split(" ")
	for i in new_text:
		if i.isnumeric():
			return i
		else:
			pass

import json
import requests

key = "https://api.binance.com/api/v3/ticker/price?symbol="
currencies = "BTCUSDT"

url = key+currencies
data = requests.get(url)
data = data.json()["price"]

text = "bitcoin will be 18000$"

text_data = float(command(text))
data = float(data)

if text_data > data:
	print("POSITIVE")
else:
	print("NEGATIVE")
