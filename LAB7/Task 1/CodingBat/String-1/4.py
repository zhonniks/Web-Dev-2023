def non_start(a, b):
    word = ''
    for i in range(1,len(a)):
        word+=a[i]
    for i in range(1,len(b)):
        word+=b[i]
    return word