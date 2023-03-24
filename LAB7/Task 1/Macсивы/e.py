x = int(input())
a = input().split()
ok = 0
for i in range(1,x):
	if int(a[i]) > 0 and int(a[i - 1]) > 0:
		ok = 1
	elif int(a[i]) < 0 and int(a[i - 1]) < 0:
		ok = 1
if ok == 1 :
	print("YES\n")
else :
	print("NO\n")