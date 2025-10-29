def canJump(nums: list[int]) -> bool:
    '''
    https://leetcode.com/problems/jump-game/description/
    '''
    if len(nums) == 1: return True

    must_reach = len(nums) - 1

    for i in range(len(nums)-2, -1, -1):
        if i + nums[i] >= must_reach:
            must_reach = i

    return must_reach == 0


print(canJump([2,3,1,1,4]))
print(canJump([3,2,1,0,4]))
