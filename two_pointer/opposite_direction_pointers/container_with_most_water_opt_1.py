height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
water_cap = 0
arr_len = len(height)

left = 0
right = arr_len -1

while left<right:
    area = min(height[left],height[right]) * (right-left)
    if area > water_cap: water_cap = area
    if height[left] < height[right]:
        left +=1
    else:
        right-=1

print(water_cap)