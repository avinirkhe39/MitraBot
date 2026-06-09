while True:
    text = input("Type something: ")

    if text.lower() == "bye":
        print("Program stopped")
        break

    print("You typed:", text)