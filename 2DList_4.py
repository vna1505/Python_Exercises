#Given a list of numbers, find and print the elements that
# appear in the list only once. The elements must be printed in
# the order in which they occur in the original list.
#In chess it is known that it is possible to place 8 queens on
# an 8×8 chess board such that none of them can attack another.
# Given a placement of 8 queens on the board,
# determine if there is a pair of queens that can attach each
# other on the next move. Print the word NO if no queen can
# attack another, otherwise print YES. The input consists of eight
# coordinate pairs, one pair per line, with each pair giving the
# position of a queen on a
#standard chess board with rows and columns numbered starting at 1.
n = 8
x = []
y = []
for i in range(n):
    new_x, new_y = [int(s) for s in input().split()]
    x.append(new_x)
    y.append(new_y)

correct = True
for i in range(n):
    for j in range(i + 1, n):
        if x[i] == x[j] or y[i] == y[j] or abs(x[i] - x[j]) == abs(y[i] - y[j]):
            correct = False

if correct:
    print('NO')
else:
    print('YES')