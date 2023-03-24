def without_end(str):
    word = ''
    n = len(str)
    for i in range(1,n-1):
        word+= str[i]
    return word