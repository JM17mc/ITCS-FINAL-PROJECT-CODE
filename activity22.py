#function

import os
def activity1():
    print("Hello, World")

def activity2():
    num1 = int(input("Enter a number:   "))
    num2 = int(input("Enter a number:   "))


    print (num1, " divided to", num2, "=" , num1//num2)

def activity3():
    #BIODATA

    Fullname = input("Enter your name: ")
    Age = input("Age: ")
    Birthdate = input("Birthdate: ")
    Birthplace = input("Birthplace: ")
    Gender = input("Gender: ")
    Nationality = input("Nationality: ")
    Marital_Status = input("Marital Status: ")
    Religion = input("Religion: ")
    Address = input("Address: ")
    Contact_No = input("Contact Number: ")
    Email_Address = input("Email Address: ")
    Skills = input("Skills: ")
    Languages = input("Languages Spoken: ")
    Hobbies = input("Hobbies: ")

    print("\nBio-Data Information")
    print("==========================================")
    print("My name is" + Fullname + "I was born on" + Birthdate + " in " + Birthplace + " . I am " + Gender + " . Also I am  " + Marital_Status + " . I follow the " + Religion + " religion. I live in "  + Address + " . You can contact me with my number " + Contact_No + " and " + Email_Address + " . My skills and hobbies are " + Skills + ". I enjoy " + Hobbies + " . " )

def activity4():
    num1 = eval(input("Enter a number:  "))
    num2 = eval(input("Enter a number:  "))
    answer = num1 + num2

    print ("The sum of", num1, " and ", num2, "is" ,answer)

def activity5():
    #FARENHEIT TO CELSIUS

    print("FARENHEIT TO CELSIUS CONVERTER PROGRAM")
    farenheit = eval(input("Enter the temperature in Farenheit: "))
    celsius = ((farenheit - 32) * 5) /9
    print(f"{farenheit}, degrees Farenheit converter to celsius is {round(celsius, 2)} degrees. ")

def activity6():
    #problem (code scenario)
    #let say we have variable
    #activity number 6


    x = 5

    print(x)

    x = x + 10

    print(x)

    x = x + 15

    print(x)

    x = x + 20

    print(x)

    x = x + 25

    print(x)

    x = x + 30 

    print(x)

    x = x + 35

    print(x)

    x = x + 40

    print(x)

    x = x + 45

    print(x)

    x = x + 50

    print(x)

    x = x + 55

    print(x)

    x = x + 60

    print(x)

    x = x + 65

    print(x)

    x = x + 70

    print(x)

    x = x + 75

    print(x)

    x = x + 80

    print(x)

    x = x + 85

    print(x)

    x = x + 90

    print(x)

    x = x + 95

    print(x)

    x = x + 100

    print(x)

    x = x + 105

    print(x)

    x = x + 110

    print(x)

    x = x + 115

    print(x)

    x = x + 120

    print(x)

    x = x + 125

    print(x)

    x = x + 130

    print(x)

    x = x + 135

    print(x)

    x = x + 140

    print(x)

isContinue = True
while isContinue:
    ask = input("Select the python file you want to open: \n1. activity1 \n2. activity2 \n3. activity3 \n4. activity4 \n5. activity5 \6. exit \nInput: ")
    os.system('cls')
    if ask == "1":
        print("Program is running")
        activity1()
    elif ask == "2":
        print("Program is running")
        activity2()
    elif ask == "3":
        print("Program is running")
        activity3()
    elif ask == "4":
        print("Program is running")
        activity4()
    elif ask == "5":
        print("Program is running")
        activity4()
    elif ask == "6":
        break
    else:
        continue