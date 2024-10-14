def tally(nums: list[int]) -> int:
    total = 0
    for num in nums:
        total = total + num
#idx 0: num = 4, total = 4
#idx 1: num = 9, total = 13
#idx 2: num = 2, total = 15
#idx 3: num = 1, total = 16
    return total

#result = tally([4, 9, 2, 1])

##################################################################################################

def copy(nums:list[int]) -> list[int]:
    new_list = []
    for idx in range(len(nums)):
        new_list.append(nums[idx])
#idx 0, new_list = [4]
#idx 1, new_list = [4, 9]
#idx 2, new_list = [4, 9, 2]
#idx 3, new_list = [4, 9, 2, 1]
    return new_list    #This loop creates a list instead of adding them all together

#result = copy([4, 9, 2, 1])
#print (result)

##################################################################################################

def increment_all(nums:list[int]) -> list[int]:
    new_list = []
    for value in nums:
        new_list.append(value + 1)
#value = 4, new_list = [5]
#value = 9, new_list = [5, 10]
#value = 2, new_list = [5, 10, 3]
#value = 1, new_list = [5, 10, 3, 2]
    return new_list

result = increment_all([4, 9, 2, 1])