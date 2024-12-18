num = True
sum = 0

while num == True:
    ans = eval(input("Please enter a number --->  "))
    
    if ans == 0 :
        print("Loop Terminated! ")
        print(f"The sum of all the numbers is {sum}.")
        break
    else:
         print("Please continue entering a number")
         
         sum += ans
         
         continue