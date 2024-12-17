tuloy = True
count = 0
while tuloy == True:
    name = input("Please enter your name--> ")

    if name.lower() == "stop":
        print("Loop has now stopped")
        print(f"You have entered{count} numbers")
        break
        tuloy = False
    else:
        count 