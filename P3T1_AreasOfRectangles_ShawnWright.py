
# Areas of Rectangles
# 9/14/18
# CTI-110 P3T1 - Areas of Rectangles
# Shawn Wright
#

# Input the length and width of rectangle 1.
# Input the length and width of rectangle 2.
# Caculate the area of rectangle 1.
# Caculate the area of rectangle 2.
# If area1 > area2
    #Display "rectangle 1 has the greatest area."
# If area2 > area1
    #Display "rectangle 2 has the greatest area."
# Else
    # Display "Both rectangles have the same area"

    
# Get the dimensions of rectangle 1.
length1 = int(input('Enter the length of rectangle 1: '))
width1 = int(input('Enter the width of rectangle 1: '))


# Get the dimensions of rectangle 2.
length2 = int(input('Enter the length of rectangle 2: '))
width2 = int(input('Enter the width of rectangle 2: '))


# Caculate the areas of the rectangle.
area1 = length1 * width1
area2 = length2 * width2


# Determine which has the greater area
if area1 > area2:
    print('rectangle 1 has the greater area.')
elif area2 > area1:
    print('rectangle 2 has the greater area. ')
else:
    print('Both have the same area')


