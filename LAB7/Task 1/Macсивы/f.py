x = int(input())
a = input().split()
cnt = 0
for i in range(1 , x - 1) :
	n1 = int(a[i])
	n2 = int(a[i - 1])
	n3 = int(a[i + 1])
	if n2 < n1 and n3 < n1 :
		cnt += 1
print(cnt)