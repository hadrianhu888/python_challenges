import random as rd 

a = 100
b = 2
c = 4 

print(a)
print(b)
print(c)

a = a | b

print(a)

b = b ^ a 

print(b)

c = c & b

print(c)

b = b >> 2 

print (b)

a = a << 2

print(a)

c = (((a | b) ^ c) | (~a ^ (b | ~c)))

print(c)

print (~c)

print ((~c)+ 1)

print((~a) + (~b))

