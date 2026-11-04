import time

start_time = time.perf_counter_ns()

arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
# desired Output: [2.2, 2.8, 2.4, 3.6, 2.8]
res=[]
for i in range(0,len(arr)):
    sub_arr = arr[i:i+k]
    if len(sub_arr)==k:
        avg_list=sum(sub_arr)/k
        res.append(avg_list)
    else:
        break



end_time = time.perf_counter_ns()

print(res)
print("time_taken = ", end_time - start_time)