import math  
n = int(input('n ')) 
k = int(input('k ')) 
cnk = int(math.factorial(n) / (math.factorial(k) * math.factorial(n-k)))  
print('Cnk = ', cnk)