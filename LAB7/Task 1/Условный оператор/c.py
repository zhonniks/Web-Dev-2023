a = str(input())
ans = int(input())
if((a == reversed(a) and ans == 1) or (a != reversed(a) and ans != 1)):
    print("YES")
else:
    print("NO") 