f=1
def fact(n,f1):
    f=n
    for i in range((n-1)):
        f =  f * (n-1)
        return f

n=int(input('Enter the number of whose factorial is to be found:'))
fact(n,f)
print('The factorial is ', f )