
numbers=[12,23,14,10,111,1]
c=0
for i in range(len(numbers)):
    try:
        if(numbers[i+1]>numbers[i]):
            if(numbers[i+1]>numbers[i+2]):
                c+=1
    except:
        pass
print('The numbers that are greater than its neighbours are ', c)