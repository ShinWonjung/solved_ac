arr = ['','','','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
voca = input()
r = 0

for v in range(len(voca)):
    for s in arr:
        if s.find(voca[v]) != -1:
            r += arr.index(s)
            break

print(r)