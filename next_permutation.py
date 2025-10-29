def nextPermutation(nums: list[int]) -> list[int]:
    if len(nums) == 1:
        return nums
    # find breakpoint
    breakpoint = -1
    for i in range(len(nums)-2, -1, -1):
        if nums[i] < nums[i+1]:
            breakpoint = i
            break
    # if breakpoint doesn't exist, just reverse the list and return
    if breakpoint == -1:
        nums.reverse()
        return
    # perform the switch of breakpoint with the smallest number to the right of breakpoint
    # that is still larger than breakpoint
    index_min = breakpoint + 1
    for j in range(breakpoint + 1, len(nums)):
        if nums[j] < nums[index_min] and nums[j] > nums[breakpoint]:
            index_min = j
    tmp = nums[breakpoint]
    nums[breakpoint] = nums[index_min]
    nums[index_min] = tmp
    # reverse the rest of the list after breakpoint
    nums[breakpoint+1:] = sorted(nums[breakpoint+1:])
    return nums


print(nextPermutation([2,3,1,3,3])) # [2,3,3,1,3]
