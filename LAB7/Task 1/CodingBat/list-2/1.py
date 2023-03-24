def count_evens(nums):
    list = []
    sum = 0
    for num in nums:
        if num % 2 == 0: sum += 1
    return sum