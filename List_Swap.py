'''
numbers=[12,23,14,10,111,1,9]
c=0

for i in range(0,len(numbers)-1,2):

        c=numbers[i+1]
        numbers[i+1]=numbers[i]
        numbers[i]=c

print('The swapped list is :',numbers)
'''

a = [int(i) for i in input().split()]
for i in range(1, len(a), 2):
    a[i - 1], a[i] = a[i], a[i - 1]
print(' '.join([str(i) for i in a]))

