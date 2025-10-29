def maxArea(height: list[int]) -> int:
    max_amount = 0
    left, right = 0, len(height) - 1
    while left != right:
        min_height = min(height[left], height[right])
        amount = (right - left) * min_height
        max_amount = max(max_amount, amount)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return max_amount


print(maxArea([1,8,6,2,5,4,8,3,7]))
