a, n = input().split() 
a, n, p, s = float(a), int(n), 1, 1 
for i in range(n): 
    p *= a 
    s += p 
print(s)
