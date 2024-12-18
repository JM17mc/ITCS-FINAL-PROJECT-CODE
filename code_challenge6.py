#Grade for Prelim, Midterm, Semi-Final, Final, Quiz, and Project.
#Final Grade: FG = (prelim x .15) + (midterm x .15 (semi-final x .15) + (final x .15) + (quiz x .25) + (project x .15)

name = input("What is your name? : ")

prelim = eval(input("Enter your Prelim Grade -->  : "))
midterm = eval(input("Enter your Midterm Grade -->  : "))
semi_final = eval(input("Enter your Semi-final Grade -->  : "))
final = eval(input("Enter your Final Grade -->  : "))
quiz = eval(input("Enter your Quiz Grade -->  : "))
project = eval(input("Enter your Project Grade -->  : "))

if (prelim >= 65 and prelim <= 100) and (midterm >= 65 and midterm <= 100) and (semi_final >= 65 and semi_final <= 100) and (final >= 65 and final <= 100) and (quiz >= 65 and quiz <= 100) and (project >= 65 and project <= 100):
 
    fg = (prelim * 0.15) + (midterm * 0.15) + (semi_final * 0.15) + (final * 0.15) + (quiz * 0.25) + (project * 0.15)

    if fg >= 75:
        print("Wow! Congratulations. You passed the course / subject.")
 
    else:
        print("Sorry, you failed. Next time is your chance to shine, you've got this!")

else:
	print("Error.")


