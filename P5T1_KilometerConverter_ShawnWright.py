# Convert kilometers to miles
# 9/28/18
# CTI-110 P5T1_KilometerConverter 
# Shawn Wright
#



# This program converts kilometers to miles.
CONVERSION_FACTOR = 0.6214


# The main function gets a distance in kilometers and calls
# the show_miles function to converts it

def main():
    # Get the distance in kilometers.
    kilometers = float(input('Enter a distance in kilometers: ') )

    # Display the distance converted to miles
    show_miles(kilometers)


# The show_miles functions converts the parameter km form
# kilometers to miles and displays the result

def show_miles(km):
    # Calculate miles
    miles = km * CONVERSION_FACTOR

    # Display the miles
    print(km, 'kilometers equals', miles, 'miles.')

# Call the main function
main()
