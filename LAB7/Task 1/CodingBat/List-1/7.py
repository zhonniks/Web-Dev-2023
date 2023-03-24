def max_end3(nums):
  if nums[0] > nums[-1]:
    max = nums[0]
    return [max,max,max]
  else :
    max = nums[-1]
    return [max,max,max]
