#remarks : O(n^2) time complexity , not a O(1) space complexity and its not a two pointer approach
nums = [1, 1, 2]
arr_len = len(nums)
n_d=[]

for i in range(arr_len):
        if nums[i] not in n_d:
            n_d.append(nums[i])

print(len(n_d))