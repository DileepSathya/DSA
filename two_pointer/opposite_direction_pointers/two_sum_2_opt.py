numbers = [2, 7, 11, 15]
target = 26
arr_len=len(numbers)
left=0
right = arr_len -1
res=[]

while left<right:
    current_sum = numbers[left]+numbers[right]
    if current_sum == target:
        res.append(left+1)
        res.append(right+1)
        break

    elif current_sum > target:
        right -=1

    else:
        left+=1


print(res)
    