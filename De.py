import requests

data = {

   "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.106 Safari/537.36 OPR/38.0.2220.41"

}

ri = requests.get("https://www.google.com/", data=data)

print(ri.text)
