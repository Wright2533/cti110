# Budget Analysis
# 9/25/18
# CTI-110 P4HW1 - Budget Analysis
# Shawn Wright
#

# Find out how much you budgeted for the month 
userBudget = float( input( "Please enter how much you've budgeted " + \
                           "for the month: "))
# "Y" means additional expense you have
moreExpenses = "y"
userTotalExpenses = 0

# Compare the expense in this loop to the first loop
while moreExpenses == "y":
    userExpense = float( input( "Enter an expense: " ) )
    userTotalExpenses += userExpense
    moreExpenses = input( " Do you have more expenses?: Type y "+ \
                          "for yes, any key for no: " )

# If total user expenses are over user budget, you are over the budget
# If user budget is over total expenses, you were under the budget
# If non of the situations meet the requirments, thhen you used exactly your budget
print()
if userTotalExpenses > userBudget:
    print( "You over your budget of","$" + format( userBudget, ",.2f" ), \
           "by","$" + format( userTotalExpenses - userBudget, ",.2f" ) )
elif userBudget > userTotalExpenses:
    print( "You were under your budget of","$" + format( userBudget, ",.2f"), \
           "by","$" + format( userBudget - userTotalExpenses, ",.2f" ) )
else:
    print( "You used exactly your budget", \
           "$" + format( userBudget , ",.2f"),".")
