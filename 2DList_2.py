#Given two numbers n and m. Create a two-dimensional
# array of size (n×m) and populate it with the
# characters "." and "*" in a checkerboard pattern.
# The top left corner should have the character "." .

n, m = [int(i) for i in input().split()]
a = []
for i in range(n):
    a.append([])
    for j in range(m):
        if (i + j) % 2 == 0:
            a[i].append('.')
        else:
            a[i].append('*')
for row in a:
    print(' '.join(row))