# a부터 z까지 -1로 초기화한 배열
arr = [-1] * (ord('z')-ord('a')+1)

s = input()
cnt = 0

for i in range(len(s)):
    n = ord(s[i]) - ord('a')
    if arr[n] == -1:
        arr[n] = cnt
    cnt += 1

for a in arr:
    print(a, end=' ')