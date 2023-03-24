def left2(str):
    word = ''
    n = len(str)
    for i in range(2,n):
        word+= str[i]
    return word+str[:2]
