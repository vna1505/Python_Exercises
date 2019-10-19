
numbers=[12,23,14,10,111,1,9]
c=0
#if len(numbers)%2==0:
for i in range(0,len(numbers),2):
    try:
        c=numbers[i+1]
        numbers[i+1]=numbers[i]
        numbers[i]=c
    except:
        pass
print('The swapped list is :',numbers)

