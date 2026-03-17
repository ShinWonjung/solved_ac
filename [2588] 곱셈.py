a = input()
b = input()

a = int(a)
#b = int(b)

#b100 = b//100
#b10 = b%100//10
#b1 = b%10

#print(a * b1)
#print(a * b10)
#print(a * b100)
#print(a * b)

for i in range(len(b)-1, -1, -1):
    bb = int(b[i])
    print(a*bb)

print(a*int(b))
