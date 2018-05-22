import re
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter

def currency_exchange(string):
	return_str = ""
	try:
		l = []
		print (string)
		string = string.strip()
		string = re.sub(" +"," ",string)
		l = string.split(" ")
		l = [x.upper() for x in l]
		print (l)
		l = [x.replace(' ', '') for x in l]
		if "BITCOIN" in l:
			b = BtcConverter()
			if (l[0]).upper() == "BITCOIN":
				return_str = str(float(l[2]) * b.get_latest_price(l[1]))
			elif (l[1]).upper() == "BITCOIN":
				return_str = str(float(l[2]) / b.get_latest_price(l[0]))
			else:
				return_str = "Result Not found"
		else:
			c = CurrencyRates()
			return_str = str(c.convert(l[0], l[1], float(l[2])))

	except Exception as e:
		return_str = "Give proper input"
		print (e)
	
	return return_str

if __name__ == "__main__":
	print (currency_exchnge("USD INR 1"))
