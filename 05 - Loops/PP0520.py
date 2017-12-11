'''
5.20 (Display four patterns using loops) Use nested loops that display the following
patterns in four separate programs:
Pattern A
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
1 2 3 4 5 6
Pattern B
1 2 3 4 5 6
1 2 3 4 5
1 2 3 4
1 2 3
1 2
1
Pattern C
          1
        2 1
      3 2 1
    4 3 2 1
  5 4 3 2 1
6 5 4 3 2 1
Pattern D
1 2 3 4 5 6
  1 2 3 4 5
    1 2 3 4
      1 2 3
        1 2
          1
'''

print("Pattern A")
for i in range(1, 6 + 1):
    for j in range(1, i + 1):
        print(j, end = " ")
    print()


print("Pattern B")
for i in range(1, 6 + 1):
    for j in range(1, 7 - i + 1):
        print(j, end = " ")
    print()

print("Pattern C")
for i in range(1, 6 + 1):

    for j in range(6 - i, 0, -1):
        print("  ", end="")

    for j in range(i, 0, -1):
        print(j, end=" ")

    print()



print("Pattern D")
for i in range(1, 6 + 1):

    for j in range(i, 1, -1):
        print("  ", end="")

    for j in range(1, 6 + 1 - i + 1):
        print(j, end=" ")

    print()