import time

start_time = time.perf_counter_ns()

# Your program
arr = [2, 1, 5, 1, 3, 2]


k = 3
max_sum=sum(arr[0:k])
sub_sum=max_sum
for i in range(k,len(arr)):
    sub_sum=sub_sum - arr[i-k] + arr[i]
    if sub_sum>max_sum:
        max_sum=sub_sum

end_time = time.perf_counter_ns()

execution_time = end_time - start_time

print("Maximum sum:", max_sum)
print(f"Execution time: {execution_time} nanoseconds")