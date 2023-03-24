def caught_speeding(speed, is_birthday):
    if speed <= 60: return 0
    elif 61 <= speed <= 80 and is_birthday == False: return 1
    elif speed >= 81 and is_birthday == False: return 2