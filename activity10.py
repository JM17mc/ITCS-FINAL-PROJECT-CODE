name = input("Enter your name: ")
isStudent = input("Are you a current student of DLL (yes/no): ")

if isStudent.lower() == "yes":
    yearLevel = input("What year are you currently enrolled? \nF - Freshmen \nS - Sophomore \nJ - Junior \nR - Senior  \nPlease input your answer here --> ")
    if yearLevel.lower() == "F":
        print(f"Hi, {name} a Freshmen, welcome to DLL! ")
    elif yearLevel.lower() == "S":
        print(f"Hi, {name} a Sophomore, welcome to DLL! ")
    elif yearLevel.lower() == "J":
        print(f"Hi, {name} a Junior, welcome to DLL! ")
    elif yearLevel.lower() == "S":
        print(f"Hi, {name} a Senior, welcome to DLL! ")
else:
    print("Thank you for using the program! ")