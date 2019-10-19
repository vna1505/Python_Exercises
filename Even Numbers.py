
n=[]
l=int(input("Enter the number of elements in the sequence: "))
c=0
x=0
print("Enter a sequence :")
for i in range(0,l):
    seq= int(input())
    n.append(seq)
print ('The sequence is ', n)
for i in range(len(n)):
    try:
        if((n[i]%10)==0):
            c+=1
    except:
        pass
print('The numbers ending with 0 are:' , c)