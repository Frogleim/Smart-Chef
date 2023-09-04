def two_sum_brute_force(nums, target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            print(nums[j])
            print(nums[i])
    #         if nums[i] + nums[j] == target:
    #             return [i, j]
    # return None

nums = [2, 7, 11, 15]
target = 9
result = two_sum_brute_force(nums, target)
if result:
    print("Indices:", result)
    print("Numbers:", nums[result[0]], nums[result[1]])
else:
    print("No solution found.")