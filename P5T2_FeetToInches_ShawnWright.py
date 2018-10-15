# Convert feet to inches
# 9/28/18
# CTI-110 P5T2_FeetToInches 
# Shawn Wright
#


# Constant for the number of feet from the user.
INCHES_PER_FOOT = 12

# main function

def main():
    # Get a number of feet from the user
    feet = int(input('Enter a number of feet: '))

    # Convert that to inches
    print(feet, 'equals', feet_to_inches(feet), 'inches')


# The feet_to_inches function converts feet to inches
def feet_to_inches(feet):
    return feet * INCHES_PER_FOOT

# Call the main function
main()

    
