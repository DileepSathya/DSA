height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
water_cap = 0
arr_len = len(height)


for left in range(arr_len):
    for right in range(arr_len-1,left,-1):
        area = min(height[left],height[right]) * (right-left)
        if area > water_cap:
            water_cap = area

print(water_cap)