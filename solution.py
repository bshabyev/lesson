def twosum(nums, target):
    check = {}
    for i in range(len(nums)):
        if target - nums[i] in check:
            return [i, check[target - nums[i]]]
        else:
            check[nums[i]] = i

print(twosum([2,7,11,15], 9))
