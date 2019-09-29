
x=input("Enter the string with ..h..h..:")
fh=x.find('h')
lh=x.rfind('h')
print(fh)
print(lh)
print(x[0:fh]+x[lh+1:])