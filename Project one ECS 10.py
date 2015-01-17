#
# Name: Geoffrey Mohn
# ID : 912568148
# Date: 1/13/15
#
import math
Dollars = int(input('Enter subtotal dollars> '))
Cents = int(input('Enter subtotal cents  >'))
Dollarcents = Dollars *100 #converting dollars into cents
Subtotal = (Dollarcents + Cents) /100 #Converting Dollars and Cents into one value

print('Subtotal: ', '$',Subtotal, sep='') #Print the two numbers next to each other

tax8 = '%.2f' %((Subtotal) * .08 ) #Multiplying for tax value
tip10 = '%.2f' %((Subtotal) * .10)
tip15 = '%.2f' %((Subtotal) * .15)
tip20 = '%.2f' %((Subtotal) * .20)

print('Tax     :', '$',tax8, sep='')
print('Total   :','%.2f' % (Subtotal *1.08), sep='')
print('Tip 10%:', '$',tip10, sep='')
print('Tip 15%:', '$',tip15, sep='')
print('Tip 20%:', '$',tip20, sep='')

PayDollar = int(input('Enter payment dollars>' ))
Paycents = int(input('Enter payment cents>' ))
Convertdollar = PayDollar *100
Total = (Convertdollar + Paycents)/100 #convert payment into one value
change = Total - (Subtotal *1.08) 
Changelist = [100, 50, 20 , 10 , 5, 1, .25 , .10, .05, .01] #list for change
Namelist = ['$100 Bill(s):', ' $50 Bill(s):',' $20 Bill(s):', ' $10 Bill(s):','  $5 Bill(s):','  $1 Bill(s):', '  Quarter(s):','     Dime(s):', '   Nickel(s):', '  Penny(ies):']
amount = []
for money in Changelist:
            holdingchange = change
            change=change//money
            amount.append(change)
            change = holdingchange%money
            
for i in range(len(Changelist)):
    print( Namelist[i],int(amount[i]))

