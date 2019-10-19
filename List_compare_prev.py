
numbers=[12,23,14,10,111,1,1000]
c=0
for i in range(len(numbers)):
    try:
        if(numbers[i+1]>numbers[i]):
            print(numbers[i+1])
            c+=1
    except:
        pass
print('There are ',c, 'numbers that are greater than the previous ones' )