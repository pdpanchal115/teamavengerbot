from weather import Weather, Unit

# Lookup WOEID via http://weather.yahoo.com.

#lookup = weather.lookup(560743)
#condition = lookup.condition
#print(condition.text)
# Lookup via location name.

def weather_search(name):
	return_str = ""
	try:
		weather = Weather(unit=Unit.CELSIUS)
		location = weather.lookup_by_location(name)
		condition = location.condition
		string = ""
		string = string + "Today is " + str(condition.text) + " day.\n\n"
		#print("Ahmedabad " + str(condition.text))

		# Get weather forecasts for the upcoming days.
		
		forecasts = location.forecast
		string = string + "Future forecasting...\n\n"
		for forecast in forecasts:
			string = string + "Date : " + str(forecast.date) + "\nHigh Temp: " + str(forecast.high) + "C\nLow Temp: " + str(forecast.low) +"C\nCondition: " +  str(forecast.text) + "\n\n"
		    # print(forecast.text)
		    # print(forecast.date)
		    # print(forecast.high)
		    # print(forecast.low)
		return_str = string
	
	except Exception as e:
		return_str = "Result Not found"
		print (e)
	
	return return_str    
	
if __name__ == "__main__":
	a = weather_search("Ahmedabad")
	print (a)

# Lookup via latitude and longitude

#w = Weather(Unit.CELSIUS)
#lookup = w.lookup_by_latlng(23.022505, 72.5713621)
#condition = lookup.condition
#print(condition.text)
