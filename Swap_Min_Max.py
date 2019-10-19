
numbers=[12,23,14,10,111,1,9]
c=0
a=max(numbers)
print('Maximum value is :',a)
b=min(numbers)
print('Minimum value is :',b)

for i in range(len(numbers)):
    try:
        if(a==numbers[i]):
            
        numbers[i+1]=numbers[i]
        numbers[i]=c
    except:
        pass
print('The swapped list is :',numbers)

