import time
start_time = time.process_time_ns()

arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3

arr = [2, -3, 4, 5, -6, 7]
k = 2
negative_num = []
for i in range(len(arr)):
    sub_array = arr[i:i+k]

    if len(sub_array)==k:

        for j in range(len(sub_array)):
            negative_num_sub_array = 0
            if sub_array[j] < 0:
                negative_num_sub_array = sub_array[j]
                negative_num.append(negative_num_sub_array)
                break
            if j == k-1 and negative_num_sub_array == 0:
                negative_num.append(negative_num_sub_array)



print(negative_num)
end_time = time.process_time_ns()
print("Time taken : ", end_time-start_time)