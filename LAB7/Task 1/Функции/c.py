def xor(x: bool, y: bool) -> bool:
    return (x or y) and not (x and y)

x , y = input().split()

print(int(xor(int(x), int(y))))