def if_pythagoream(nums: list) -> bool:
    if len(nums) == 3:
        nums.sort()
        num1, num2, num3 = nums
        return (num1**2 + num2**2) == num3**2
    return False
        
print(if_pythagoream([5, 3, 4]))
print(if_pythagoream([3, 4, 5]))
print(if_pythagoream([13, 12, 5]))
print(if_pythagoream([100, 3, 999]))