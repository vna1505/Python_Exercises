#Suppose you are given a square array
# (an array of n rows and n columns).
# you have to set elements of the main diagonal
# equal to 1 (that is, those elements a[i][j] for which i==j),
# to set elements above than that diagonal equal to 0, and
# to set elements below that diagonal equal to 2

n = 4
a = [0] * n
for i in range(n):
    a[i] = [2] * i + [1] + [0] * (n - i - 1)
for row in a:
    print(' '.join([str(elem) for elem in row]))