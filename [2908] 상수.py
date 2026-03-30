s1, s2 = input().split()
s1 = int(''.join(reversed(s1)))
s2 = int(''.join(reversed(s2)))
if s1 > s2:
    print(s1)
else:
    print(s2)
