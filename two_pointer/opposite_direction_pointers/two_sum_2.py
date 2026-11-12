numbers = [2, 7, 11, 15]
target = 9
numbers = [2, 7, 11, 15]
target = 26
num_len=len(numbers)

res = []

for left in range(num_len):
    for right in range(num_len-1,left,-1):
#        print(left,right)
        if numbers[left]+numbers[right]==target:
            res.append(left+1)
            res.append(right+1)
            break

print(res)
