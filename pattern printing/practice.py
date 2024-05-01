n = 5
for i in range(n):
    for j in range(ord("A"), ord("A") + i + 1):
        print(chr(j), end=" ")
    print()

n = 5
for i in range(n):
    for j in range(ord("A"), ord("A") + n - i):
        print(chr(j), end=" ")
    print()