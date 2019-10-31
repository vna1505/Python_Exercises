
numbers=[12,23,14,10,111,1,1000,1]
c=0
for i in range(1,len(numbers)-1):
    if(numbers[i-1] < numbers[i] > numbers[i+1]):
            #print(numbers[i+1])
            c+=1    

print('There are ',c, 'numbers that are greater than the previous ones' )

