# Tuition Increase
# 9/26/18
# CTI-110 P4HW3 - Tuition Increase
# Shawn Wright
#

# Made a loop that displays the tuition amount for the next 5 years
currentTuition = 8000

print( "Year\tTuition\n-----\t--------" )
for currentYear in range( 1,6 ):
    currentTuition += (3 / 100) * currentTuition
    print( currentYear, "\t$", format( currentTuition, ".2f" ), sep = "" )
