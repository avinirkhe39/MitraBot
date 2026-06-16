# Main Chat Bot
import json
import pyttsx3

from datetime import datetime

engine = pyttsx3.init()

with open("telecom_data.json", "r") as file:
    telecom_data = json.load(file)

name = "Avinash"

while True:
    user = input(f"{name}: ")

    if user.lower() in ["hi", "hello"]:
        reply = "Namaskar Avinash!"
     
    elif "time" in user.lower():
        reply = datetime.now().strftime("Ata vel %H:%M ahe")

    elif "date" in user.lower():
        reply = datetime.now().strftime("Aajchi tarikh %d-%m-%Y ahe")    

    elif user.lower() in telecom_data:
        reply = telecom_data[user.lower()]


    elif user.lower() == "bye":
        reply = "Bye Avinash!"
        print("Mitra:", reply)
        engine.say(reply)
        engine.runAndWait()
        break

    else:
        reply = "Mi ajun shiktoy, punha vichar."

    print("Mitra:", reply)
    engine.say(reply)
    engine.runAndWait()