def fibonacci_recur(n):
    if n<=0:
        return 0
    if n==1:
        return 1
    return(fibonacci_recur(n-1)+ fibonacci_recur(n-2))

for i in range(7):
    print(fibonacci_recur(i). end=" ")
print()

def fibonacci_loop(n):
    a,b=0,1
    if n