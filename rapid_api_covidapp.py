import requests

url = "https://covid-19-data.p.rapidapi.com/country/code"

querystring = {"code":"it"}

headers = {
    'x-rapidapi-host': "covid-19-data.p.rapidapi.com",
    'x-rapidapi-key': "eb9d30db74msh92124d20e3e3e80p1f12c1jsn2284c37d74db"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)