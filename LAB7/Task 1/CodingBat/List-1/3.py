def reverse3(nums):
    a = nums[0]
    c = nums[2]
    nums[0] = c
    nums[2] = a
    return nums