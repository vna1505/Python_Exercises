#!/usr/bin/env python3

x=int(input("Enter the number of rows of the choc bar: "))
y=int(input("Enter the number of columns of the choc bar: "))
z=int(input("Enter the number of pieces:"))
if (x*y) < z:
    print("No")
elif (x%z == 0) or (y% == 0):
    print("Yes, it can be broken"+str(z)+"pieces")
else:
    print("Nooo")