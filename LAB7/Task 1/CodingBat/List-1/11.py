def sum2(nums):
    if len(nums) <= 2:
        sum = 0
        for i in nums:
            sum += i
        return sum
    else :
        sum = nums[0] + nums[1]
        return sum
