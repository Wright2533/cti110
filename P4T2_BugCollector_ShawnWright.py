# Bug Collector
# 9/25/18
# CTI-110 P4T2 - Bug Collector
# Shawn Wright
#


# Number of Bugs collected for 5 days ( 0 Bugs )
totalDays = 5
totalNumberOfBugs = 0

# 5 day loop that shows how many bugs were collected each day
# Finally shows the total number of bugs collected for all 5 days
for currentDay in range( 1, totalDays + 1 ):
    bugsCollected = int( input( "How many bugs were collected on day " + \
                                str( currentDay ) + ": " ) )
    totalNumberOfBugs += bugsCollected
print()
print( "The total number of bugs collected for all", totalDays, "days is", \
       totalNumberOfBugs )
