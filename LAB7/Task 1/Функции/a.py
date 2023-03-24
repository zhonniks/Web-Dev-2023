def min4(a , b , c ,d ):
    return min(min(min(a, b), c), d)
 
m = input().split()
a = int(m[0])
b = int(m[1])
c = int(m[2])
d = int(m[3])
print(min4(a, b, c, d))