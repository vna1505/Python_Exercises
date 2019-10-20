
numbers = [12,233,14,10,111,1,9]
c = 0
a=max(numbers)
ind_max=numbers.index(a)
print('Maximum value is :',a,'and index is ', ind_max)
b=min(numbers)
ind_min=numbers.index(b)
print('Minimum value is :',b, 'and index is ', ind_min)

for i in range(len(numbers)):
    try:
        if(i==ind_max):
            c=numbers[i]
        elif (i==ind_min):
            d=numbers[i]

        numbers[ind_max]=d
        numbers[ind_min]=c

    except:
        pass
print('The swapped list is :',numbers)

