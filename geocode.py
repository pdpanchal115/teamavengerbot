import requests

def location_search(name):
	return_str = ""
	try:
		GOOGLE_MAPS_API_URL = 'http://maps.googleapis.com/maps/api/geocode/json'

		params = {
			'address': str(name),
			'sensor': 'false'
			}

		    	# Do the request and get the response data
		req = requests.get(GOOGLE_MAPS_API_URL, params=params)
		res = req.json()
		result = res['results'][0]

		geodata = dict()
		geodata = {}
		string = ""
		geodata['lat'] = result['geometry']['location']['lat']
		geodata['lng'] = result['geometry']['location']['lng']
		geodata['address'] = result['formatted_address']

		print ('\n\n' + str(geodata) + '\n\n')

		string = "Location of address : " + str(geodata['address']) + " :\nlat : " + str(geodata['lat']) + "\nlng : " + str(geodata['lng'])
		return_str = string

	except Exception as e:
		return_str = "Result Not found"
		print (e)

	return return_str

if __name__ == "__main__":
	# a = {}
	# a = search('einfochips, near cargo moters, cg road,ahmedabad,gujarat')
	# print('{address}. (lat, lng) = ({lat}, {lng})'.format(**a))

	b = location_search('einfochips, near cargo moters, cg road,ahmedabad,Gujarat 380006')
	print (b)

# 221B Baker Street, London, Greater London NW1 6XE, UK. (lat, lng) = (51.5237038, -0.1585531)
