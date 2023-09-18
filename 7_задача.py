a = int(input())
b = list()

while a != 0:
    if a % 2 == 0:
        b.append(a)
        a -= 1
    else:
        a -= 1

print(sum(b))