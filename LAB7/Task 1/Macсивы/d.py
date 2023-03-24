x = int(input())
a = input().split()
sum = 0
for i in range(1, x):
    if int(a[i]) > int(a[i - 1]):
        sum += 1
print(sum)