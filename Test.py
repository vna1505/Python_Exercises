
#fibonacci series
# 0 1 1 2 3 5
n=int(input("Enter a number for fibonacci:"))
count=0
a=0
b=1
if n<0:
    print("Enter a positive value!!")
elif(n==0):
    print(n)
elif(n==1):
    print(a,',',b)
else:
     while(count<=n):
        print(a)
        c=a+b
        count+=1
        a=b
        b=c






