while True:
    gender = input('Gender: ')
    if(gender == 'M' or gender == 'm' or gender == 'f' or gender == 'F'):
        break
    else :
        print('Please try again')
    
print('You are: ',gender)