
n=int(input('Enter the dimension of the array: '))
# a=[[0]*n] * n

a=[]
for i in range(n):
    a.append([0]*n)

for i in range(n):
    for j in range(n):
        if (i==j):
            a[i][j]=1
        if(i>j):
            a[i][j]=0
        if (i<j):
            a[i][j]=2

for i in range(n):
    print(a[i])


