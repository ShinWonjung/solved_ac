n = int(input())
arr = list(map(int, input().split()))
total = 0
max = max(arr)
for i in arr:
    total += i/max*100
print(total/n)