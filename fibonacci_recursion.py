def fibonacci_recur(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    return(fibonacci_recur(n-1)+fibonacci_recur(n-2))

for i in range(7):
    print(fibonacci_recur(i), end=" ")
print()

def fibonacci_loop(n):
    a,b=0,1
    if n==1:
        print(1,end=" ")
    for i in range(n):
        print(a, end=" ")
        a,b=b,a+b

fibonacci_loop(7)