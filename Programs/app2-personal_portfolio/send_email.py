import smtplib,ssl

host = "smtp.gmail.com"
port = 465

username = "ilyan146@gmail.com"
password = "tlmqucfsavoeegpn"

receiver = "ilyan146@gmail.com"
context = ssl.create_default_context()

message = """\
Subject: Hi!
This is from your python app sending you emails
BYE!
"""


with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
