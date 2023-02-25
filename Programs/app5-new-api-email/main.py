import requests
from send_email import send_email



key = "715f2e1394254e7baeba8eb87fddab91"
url = "https://newsapi.org/v2/everything?q=tesla&from=" \
      "2023-01-25&sortBy=publishedAt&apiKey=715f2e1394254e7baeba8eb87fddab91"

request = requests.get(url)
content = request.json()

#message = """\
#Subject: News headers and descriptions

#"""
"""message = []
for index,i in enumerate(content["articles"]):
    text = f"{index+1} {i['title']} \n {i['description']}"
    new_text = text.split("\n")
    message.append(new_text)
print(message)"""

message = ""
for index,i in enumerate(content["articles"]):
    #Below is for case when the tile of article is kept as None, which will cause error.
    if i["title"] is not None:
        message += f"{index+1} {i['title']} \n{i['description']} \n\n"


final_message = """\
Subject: Email from API, topics and description

""" + message

print(final_message)

# Need to encode due to code error on str format
send_email(final_message.encode("utf-8"))



