#
# Name: Geoffrey Mohn
# ID : 912568148
# Date: 1/13/15
#
import math
x= float(input('Enter X> '))
y= float(input('Enter Y> '))
z= float(input('Enter Z> '))
point1 = (x, y, z)
origin = (0,0,0)
Distancex = point1[0] - origin[0]
Distancey = point1[1] - origin[1]
Distancez = point1[2] - origin[2]
Distancesquared = math.sqrt(Distancex * Distancex + Distancey**2 + Distancez**2) #plugging in distance formula
print('Distance to', point1, ':',' ','%.3f' % (Distancesquared), sep='') #limit to 3 decimal places made sure to add a space between value and colon
Volume = 4/3*math.pi*Distancesquared**3 #plugging in Volume
print('Volume of sphere:', '%.3f' % Volume)
Area = 4*math.pi*Distancesquared**2 #plugging in Area
print('Area of sphere:', '%.3f' % Area)




