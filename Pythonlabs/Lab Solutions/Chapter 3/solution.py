# And Truth Table
a = 1
b = 0
if (a == 1 and b == 1):
    print('1')
elif ((a == 1 and b == 0) or (a == 0 and b == 1)):
    print('0')
elif (a == 0 and b ==0):
    print('0')
else:
    print('Invalid Input')
    
# OR truth table

a = 1
b = 0
if (a == 1 and b == 1):
    print('1')
elif ((a == 1 and b == 0) or (a == 0 and b == 1)):
    print('1')
elif (a == 0 and b ==0):
    print('0')
else:
    print('Invalid Input')
    
# Not truth table

a = 0
if(a == 1):
    print('0')
elif(a == 0):
    print('1')
else:
    print('Invalid Input')
    
# Main Challenge:

a = 1
b = 0
c = 1

if(b == 1):
    bHolder = 0
elif(b==0):
    bHolder = 1
    
if(a == 1 and bHolder == 1):
    firstBracketHolder = 1
else:
    firstBracketHolder = 0
if(firstBracketHolder == 1 or c == 1):
    print('Q = 1')
else:
    print('Q = 0')