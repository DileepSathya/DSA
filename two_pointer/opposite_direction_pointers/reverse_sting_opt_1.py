import time
start_time =time.process_time_ns()

input_str = ["H","a","n","n","a","h"]
in_len = len(input_str)
left = 0
right = in_len - 1

while left < right:
    input_str[left],input_str[right] = input_str[right],input_str[left]
    left +=1
    right -=1

print(input_str)
end_time=time.process_time_ns()
print("time_taken" , end_time - start_time)