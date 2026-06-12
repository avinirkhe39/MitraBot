# Main Chat Bot

import pyttsx3

from datetime import datetime

engine = pyttsx3.init()

name = "Avinash"

while True:
    user = input(f"{name}: ")

    if user.lower() in ["hi", "hello"]:
        reply = "Namaskar Avinash!"

    elif "osa" in user.lower():
        reply = "OSA mhanje Optical Spectrum Analyzer."

    elif "bert" in user.lower():
        reply = "BERT mhanje Bit Error Rate Tester."

    elif "time" in user.lower():
        reply = datetime.now().strftime("Ata vel %H:%M ahe")

    elif "date" in user.lower():
        reply = datetime.now().strftime("Aajchi tarikh %d-%m-%Y ahe")    

    elif "edfa" in user.lower():
        reply = "EDFA optical signal amplify karte."

    elif "sfp" in user.lower():
        reply = "SFP he optical transceiver module ahe."

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