import time

start_time = time.perf_counter_ns()

# Your program
arr = [2, 1, 5, 1, 3, 2]
arr = [-5, -2, -8, -1, -3]

k = 3
max_sum = 0

for i in range(len(arr)):
    sub_set = arr[i:i+k]

    if len(sub_set) < k:
        break

    subset_sum = sum(sub_set)

    if subset_sum > max_sum:
        max_sum = subset_sum

end_time = time.perf_counter_ns()

execution_time = end_time - start_time

print("Maximum sum:", max_sum)
print(f"Execution time: {execution_time} nanoseconds")