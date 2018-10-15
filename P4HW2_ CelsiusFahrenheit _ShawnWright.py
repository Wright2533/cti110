# Celsius to Fahrenheit Table
# Date
# CTI-110 P4HW2 - Celsius to Fahrenheit Table
# Shawn Wright
#

# Display the celsius temperatures in a range of 1-20
print( "Celsius temperature\tFahrenheit Equivalent" )
for currentCelsiusTemperature in range( 21 ):
    fahrenheitTemperatureEquivalent = (9 /5 ) * currentCelsiusTemperature + 32
    print( currentCelsiusTemperature,"\t\t\t\t", \
           format( fahrenheitTemperatureEquivalent, ".1f" ) )
