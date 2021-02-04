passed = '82914656273523:a4edFea2786DGex'

data = passed.split(':')

id = data[0]
key = data[1]
if(id.isdigit()):
    # Number is numeric.
    if(len(id) == 14):
        #Length of 14
        if(len(key) > 10 and len(key) < 20):
            print('ID and Key are valid')
        else:
            print('Key Length isn\'t valid')
    else:
        print('ID wrong length')
else:
    print('ID isn\'t a digit')