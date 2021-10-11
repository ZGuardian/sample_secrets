import requests

url = "https://skyscanner-skyscanner-flight-search-v1.p.rapidapi.com/apiservices/autosuggest/v1.0/UK/GBP/en-GB/"

querystring = {"query":"Stockholm"}

headers = {
    'x-rapidapi-host': "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com",
    'x-rapidapi-key': "eb9d30db74msh92124d20e3e3e80p1f12c1jsn2284c37d74db"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)