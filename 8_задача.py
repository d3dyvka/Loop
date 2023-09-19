a = int(input())
s = 0
res = 1

while a > 0:
    b = a % 10
    s += b
    res *= b
    a = a // 10

print("sum =", s,",", "umn = ", res)
