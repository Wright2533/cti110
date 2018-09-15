# CTI-110 
# P3HW2 - Shipping Charges 
# Shawn Wright
# 9/14/18
#

# Input the weight of a package
userWeightOfPackage = int( input( "please enter the weight of the package:") )

# If the weight of the package is less than or equal to 2 the shipping charge is $1.50
# If the weight of the package is greater than 2 pounds but no more than 6 punds the shipping charge is $3.00
# If the weight of the package is greater than 6 pounds but no more than 10 punds the shipping charge is $4.00
# If the package is over 10 pounds the shipping charge is $4.75

if userWeightOfPackage <= 2:
    shippingCharges = 1.50
elif userWeightOfPackage < 7:
    shippingCharges = 3.00
elif userWeightOfPackage < 11:
    shippingCharges = 4.00
else:
    shippingCharges = 4.75

print( "\nFor a package weighing " + str( userWeightOfPackage ) + \
       ", you'll pay $" + format( shippingCharges, ",.2f" ) + " per pound." )
 
