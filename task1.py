def even_nums(nums):
    return [num for num in nums if num % 2 == 0]

def min_num(nums):
    min = nums[0]
    for i in range (1, len(nums)):
        if nums[i] < min:
            min = nums[i]
    return min

def max_num(nums):
    max = nums[0]
    for i in range (1, len(nums)):
        if nums[i] > max:
            max = nums[i]
    return max

def sort_nums(nums):
    if len(nums) <= 1:
        return nums
    
    point = nums[len(nums) // 2] 
    left = [x for x in nums if x < point]
    middle = [x for x in nums if x == point]
    right = [x for x in nums if x > point]
    
    return sort_nums(left) + middle + sort_nums(right)

nums = list(map(int, input().split(',')))
print('Четные числа: ', even_nums(nums))
print('Максимальное число: ', max_num(nums))
print('Минимальное число: ', min_num(nums))
print('Отсортированный список: ', sort_nums(nums))