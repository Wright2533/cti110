# CTI-110 
# P3HW1 - Roman Numerals 
# Shawn Wright
# Date
#

# Input a interger from 1 to 10
# Program will print the number as a roman numeral
# If the interger is not 1 to 10 the program will display a error message

userNumber = int(input( "please enter a number") )
if userNumber == 1:
    print("I")
elif userNumber == 2:
    print("II")
elif userNumber == 3:
    print("III")
elif userNumber == 4:
    print("IV")
elif userNumber == 5:
    print("V")
elif userNumber == 6:
    print("VI")
elif userNumber == 7:
    print("VII")
elif userNumber == 8:
    print("VIII")
elif userNumber == 9:
    print("IX")
elif userNumber == 10:
    print("X")
else:
    print("Error: Restart program and enter a number between 1 and 10." )
