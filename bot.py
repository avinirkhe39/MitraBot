name = "Avinash"

while True:
    user = input(f"{name}: ")

    if user.lower() in ["hi", "hello"]:
        print("Mitra: Namaskar Avinash!")

    elif "osa" in user.lower():
        print("Mitra: OSA mhanje Optical Spectrum Analyzer.")

    elif "bert" in user.lower():
        print("Mitra: BERT mhanje Bit Error Rate Tester.")

    elif user.lower() == "bye":
        print("Mitra: Bye Avinash!")


    elif "telecom" in user.lower():
        print("Mitra: Telecom madhe Fiber,DWDM, Routing ani Transmission yetat.")
        break

    else:
        print("Mitra: Mi ajun shiktoy, punha vichar.")