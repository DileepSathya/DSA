import time
start_time = time.perf_counter_ns()

input_str = ["h","e","l","l","o"]
input_str = ["H","a","n","n","a","h"]
len_ip = len(input_str)
left = 0
right = len_ip - 1



for i in range(len_ip//2):
    input_str[left],input_str[right] = input_str[right],input_str[left]
    left +=1
    right-=1




print(input_str)
end_time = time.perf_counter_ns()
print("time_taken = ", end_time - start_time)