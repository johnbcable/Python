string = '1211f3'

def checkType(string):
    string = str(string)
    if(string.isdigit()):
         return 'string is a Digit'
    elif(string.isalnum()):
        return 'String is Alpha Numeric'
    elif(string ==  True or string == False):
        return'String is boolean'
    else:
        return 'unknown String type'
    
print(checkType(string))