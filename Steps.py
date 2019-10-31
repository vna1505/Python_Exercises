
step=int(input('Enter the number of steps: '))
k=int(input('Enter a step number <9:'))
for i in range(1,step):

    if (i==k):
          for a in range(1,k+1):
            print(a,end='')
            a+=1
            if(a==k+1):
                print(' L') # why did it not go to a new line
    print(i * ' ','L')



