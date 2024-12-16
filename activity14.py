#washing machine

for x in range(0, 11):
    #print("*", end = " ") 
    #another washing machine
    print(x, end = "  ")
    for y in range(x, 11):
        print("*", end = "   ")
    print()

for x in range(0, 11):
    print(x, end = "  ")
    for y in range(0, x):
        print("*", end = "  ")
    print()
