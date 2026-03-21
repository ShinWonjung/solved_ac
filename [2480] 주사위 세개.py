a, b, c = map(int, input().split())

n = 0
num = 0

if a == b:
    n += 1
    num = a
if a == c:
    n += 1
    num = a
if b == c:
    n += 1
    num = b

if n >= 2:
    print(10000 + num * 1000)
elif n == 1:
    print(1000 + num * 100)
elif n == 0:
    arr = [a,b,c]
    max = max(arr)
    print(max * 100)