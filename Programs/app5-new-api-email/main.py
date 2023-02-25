import requests



key = "715f2e1394254e7baeba8eb87fddab91"
url = "https://newsapi.org/v2/everything?q=tesla&from=" \
      "2023-01-25&sortBy=publishedAt&apiKey=715f2e1394254e7baeba8eb87fddab91"

request = requests.get(url)
content = request.json()

for index,i in enumerate(content["articles"]):
    print(index+1, i["title"])
    print(i["description"])
