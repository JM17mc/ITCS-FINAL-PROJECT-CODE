user = input("ENTER YOUR NAME: ")
age = eval(input("Enter age: "))




if age >= 1 and age <= 7 :
	 print("You are a toddler! ")

elif age >= 8 and age <= 12 :
	 print("You are a pre teen! ")

elif age >= 13 and age <= 19 :
	 print("You are a teenager! ")

elif age >= 20 and  age <= 31 :
	 print("You are an early adulthood! ")

elif age >= 32 and age <= 45 :
	 print("You are a mid adult. ")

elif age >= 46 and age <= 59 :
	 print("You are a mid adult. ")

elif age >= 60 and age <= 1000 :
	 print(f"Hi, {user} You are a mid adult. ")

else: 
	 print("INVALID AGE")