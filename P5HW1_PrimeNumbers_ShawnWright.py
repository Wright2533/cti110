# Prime Numbers
# 9/28/18
# CTI-110 P5HW1 - Prime Numbers
# Shawn Wright
#

# Define isPrime as "userNumber"
def isPrime( userNumber ):
    evenDivisions = 0
    # If anything less or equl to one is not prime
    if userNumber <= 1:
        return False
    # make a range to divide the "current number by 1,2,3..etc
    for currentNumber in range( 1, userNumber + 1 ):
        if userNumber % currentNumber == 0:
            evenDivisions = evenDivisions + 1
            if evenDivisions > 2:
                return False
    return True

# Main function
def main():
    # Get a number from the user
    userNumber = int( input( "Please enter a number: ") )
    print()
    # If its prime program will say " is a prime number
    # If its not prime program will say "is NOT a prime number 
    if isPrime( userNumber ):
        print( userNumber, "is a prime number" )
    else:
        print( userNumber, "is NOT a prime number" )

# Call the main function
main()
