##Leira Salene 1785752

import math

paintColor = {
    'red' : 35,
    'blue' : 25,
    'green' : 23
}

height = float(input('Enter wall height (feet):\n'))
width = float(input('Enter wall width (feet):\n'))
wallArea = height * width

print ('Wall area: {:.0f} square feet'.format(wallArea))
paint = wallArea/350

print ('Paint needed: {:.2f} gallons'.format(paint))
print ('Cans needed: {} can(s)'.format(math.ceil(paint)))

wallColor = input('\nChoose a color to paint the wall:\n')
print ('Cost of purchasing {} paint: $'.format(wallColor),end="")
print (paintColor[wallColor])