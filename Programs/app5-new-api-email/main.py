import requests
from send_email import send_email
from datetime import date
today = date.today()

topic = "engineering"

key = "715f2e1394254e7baeba8eb87fddab91"
url = f"https://newsapi.org/v2/everything?q={topic}&from={today}&" \
      "sortBy=publishedAt&apiKey=715f2e1394254e7baeba8eb87fddab91&language=en"


request = requests.get(url)
content = request.json()

message = ""
for index,i in enumerate(content["articles"][:25]):
    #Below is for case when the tile of article is kept as None, which will cause error.
    if i["title"] is not None:
        message += f"{index+1}--{i['title']}\n{i['description']}\n{i['url']}\n\n"


final_message = f"""\
Subject: Email from API Topic: {topic.capitalize()}

""" + message


# Need to encode due to code error on str format
send_email(final_message.encode("utf-8"))



