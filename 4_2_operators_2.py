#Identity Operators

x = [1,2]
y = [1,2]

z = x
print(x is z)
print(x is y)
print(x is not y)

#Membership Operators

x = [1,2,3,4]
print(2 in x)
print(5 not in x)


#Bitwise Operators

a = 5
b = 3

# 0101
# 0011
# 0001 = 1

# 0101
# 0011
# 0111 = 7

print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<1)
print(a>>1)

print(10+3-2)
print((10+2)*3)