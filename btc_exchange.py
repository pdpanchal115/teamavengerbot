import requests
import copy

def btc_exchange():
	return_str = ""
	try:
		api_Pocketbits = 'https://pocketbits.in/api/ticker'
		api_Coindelta = 'https://coindelta.com/api/v1/public/getticker/'
		api_Zebpay = 'https://www.zebapi.com/api/v1/market/ticker-new/btc/inr'
		api_Coinome = 'https://www.coinome.com/api/v1/ticker.json'
		api_Koinex = 'https://koinex.in/api/ticker'

		json_data = requests.get(api_Pocketbits).json()
		json_data1 = requests.get(api_Coindelta).json()
		json_data2 = requests.get(api_Zebpay).json()
		json_data3 = requests.get(api_Coinome).json()
		json_data4 = requests.get(api_Koinex).json()


		buy_list = [json_data['buy'], int(json_data1[0]['Ask']), int(json_data2['buy']), int(float(json_data3['btc-inr']['lowest_ask'])), int(json_data4['stats']['inr']['BTC']['lowest_ask'])]
		sell_list = [json_data['sell'], int(json_data1[0]['Bid']), int(json_data2['sell']), int(float(json_data3['btc-inr']['highest_bid'])), int(json_data4['stats']['inr']['BTC']['highest_bid'])]

		buy_copy = copy.deepcopy(buy_list)
		sell_copy = copy.deepcopy(sell_list)

		traders_list = ["Pocketbits", "Coindelta", "Zebapay", "Coinome", "Koinex"]

		buy_list.sort()
		sell_list.sort()

		lowest_buy = buy_list[0]
		highest_sell = sell_list[-1]

		lowest_buyer_list = []
		highest_seller_list = []

		for i in range(0,len(buy_copy)):
			if buy_copy[i] == lowest_buy:
				lowest_buyer_list.append(copy.deepcopy(traders_list[i]))

		for i in range(0,len(sell_copy)):
			if sell_copy[i] == highest_sell:
				highest_seller_list.append(copy.deepcopy(traders_list[i]))

		string = ""
		string = "Exchanges  |   Buy  |  Sell\n" + \
				 "-----------------------------------\n" + \
				 "Pocketbits  | " + str(json_data['buy']) + " | " + str(json_data['sell']) + "\n" + \
				 "Coindelta    | " + str(int(json_data1[0]['Ask'])) + " | " +str(int(json_data1[0]['Bid'])) + "\n" + \
				 "Zebapay      | " + str(json_data2['buy']) + " | " + str(json_data2['sell']) + "\n" + \
				 "Coinome     | " + str(int(float(json_data3['btc-inr']['lowest_ask']))) + " | " + str(int(float(json_data3['btc-inr']['highest_bid']))) + "\n" + \
				 "Koinex          | " + str(json_data4['stats']['inr']['BTC']['lowest_ask']) + " | " + str(json_data4['stats']['inr']['BTC']['highest_bid']) + "\n" + \
				 "Best            |   " + ",".join(lowest_buyer_list) + "  |  " + ",".join(highest_seller_list)
		
		# print("Exchanges   |   Buy  |  Sell")
		# print("Pocketbits  |", json_data['buy'],"|",json_data['sell'])
		# print("Coindelta   |", int(json_data1[0]['Ask']),"|",int(json_data1[0]['Bid']))
		# print("Zebapay     |", json_data2['buy'],"|",json_data2['sell'])
		# print("Coinome     |", int(float(json_data3['btc-inr']['lowest_ask'])),"|",int(float(json_data3['btc-inr']['highest_bid'])))
		# print("Koinex      |", json_data4['stats']['inr']['BTC']['lowest_ask'],"|",json_data4['stats']['inr']['BTC']['highest_bid'])

		return_str = string

	except Exception as e:
		return_str = "Result Not Found"
		print (e)
	
	return return_str

if __name__ == "__main__":
	print (btc_exchange())