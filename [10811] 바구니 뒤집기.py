n, m = map(int, input().split())
arr = list(range(1, n+1))

for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    while b > a:
        c = arr[a]
        arr[a] = arr[b]
        arr[b] = c
        a += 1
        b -= 1

for i in arr:
    print(i, end=' ')