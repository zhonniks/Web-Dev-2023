n = int(input())
sum = 1
f = 1
for g in range(1,n + 1):
    f *= g
    sum += 1 / f
print(sum)