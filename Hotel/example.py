import requests

url = "https://hotels4.p.rapidapi.com/locations/v2/search"

querystring = {"query":"new york","locale":"en_US","currency":"USD"}

headers = {
	"X-RapidAPI-Host": "hotels4.p.rapidapi.com",
	"X-RapidAPI-Key": "68ca88a6cbmsh5f6bc817997461fp11434fjsn20609b8f8808"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)