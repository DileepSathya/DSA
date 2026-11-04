import time

start_time = time.perf_counter_ns()
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
k = 5
# desired Output: [2.2, 2.8, 2.4, 3.6, 2.8]
res=[]

fist_avg = sum(arr[0:k])/k
res.append(fist_avg)

for i in range(k,len(arr)):
    sub_set_sum = float(res[-1])*k
    sub_set_avg = (sub_set_sum - arr[i-k] + arr[i])/k
    res.append(sub_set_avg)

end_time = time.perf_counter_ns()

print(res)
print("time_taken = ", end_time - start_time)