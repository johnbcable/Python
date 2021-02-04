data = [8,7,12,4,9,6,5]
N = len(data)
swapped = True
while (swapped == True or N != 1):
    swapped = False
    position = 0
    
    while (position < N - 1):
        if (data[position] > data[position + 1]):
            temp = data[position]
            data[position] = data[position + 1]
            data[position + 1] = temp
            swapped = True
        position = position + 1
    N = N - 1
    
print(data)