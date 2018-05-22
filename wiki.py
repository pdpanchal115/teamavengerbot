import wikipedia

def wiki_search(name):
	return_str = ""
	try:
		string = ""
		string = wikipedia.summary(name)
		print (string)
		return_str = string
	except Exception as e:
		return_str = "Result Not Found"
		print (e)
	
	return return_str

if __name__ == "__main__":
	print (wiki_search("USA"))
