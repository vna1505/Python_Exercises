#Suppose you are given a square array
# (an array of n rows and n columns).
# you have to set elements of the main diagonal
# equal to 1 (that is, those elements a[i][j] for which i==j),
# to set elements above than that diagonal equal to 0, and
# to set elements below that diagonal equal to 2

n = 4
a = [[0] * n for i in range(n)]
for i in range(n):
    for j in range(0, i):
        a[i][j] = 2
    a[i][i] = 1
    for j in range(i + 1, n):
        a[i][j] = 0
for row in a:
    print(' '.join([str(elem) for elem in row]))