
n=[]
l=int(input("Enter the number of elements in the sequence: "))
c=0
x=0
print("Enter a sequence :")
for i in range(0,l):
    seq= int(input())
    n.append(seq)
print(n)
print(len(n))
for x in range(len(n)):
    try:
        if(n[x+1]>n[x]):
            c+=1

    except:
        pass
print(" The neighbours greater are ",c )



