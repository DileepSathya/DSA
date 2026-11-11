s = "A man, a plan, a canal: Panama"
s = "race a car"
s = " "

s=s.replace(",","")
s=s.replace(" ","")
s=s.replace(":","")
s=s.lower()

s_len=len(s)
left = 0
right = s_len - 1
is_palindrome = True

while(left < right):
    if s[left] != s[right]:
         is_palindrome = False
         break

    left +=1
    right -=1

print(is_palindrome)