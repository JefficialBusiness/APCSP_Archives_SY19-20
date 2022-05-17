#   a117_grades.py
#   This code is incomplete.
my_courses = ["English", "Math", "CS"]

check_grades = True
while (check_grades):
    for m in my_courses:
        points = int(input("What grade do you have in " + m + "?")) # prompts user to input number of points
        if points >= 90:
            print("You got an A in " + m + ".")
        elif points >= 80 and points < 90:
            print("You got a B in " + m + ".")
        elif points >= 70 and points < 80:
            print("You got a C in " + m + ".")
        elif points <= 69:
            print("You got a D in " + m + ".")
    
    recheck = input("Do you want to recheck your grades? Input y or n.") # prompts user to choose to recheck grades
    if recheck == ("y"):
        check_grades = True
    elif recheck == ("n"):
        check_grades = False
        print("Goodbye") # dismisses program
        