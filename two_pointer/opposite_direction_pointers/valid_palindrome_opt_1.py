s = "A man, a plan, a canal: Panama"

left = 0
right = len(s) - 1

is_palindrome = True

while left < right:

    # Skip non-alphanumeric characters from the left
    if not s[left].isalnum():
        left += 1
        continue

    # Skip non-alphanumeric characters from the right
    if not s[right].isalnum():
        right -= 1
        continue

    # Compare characters without considering case
    if s[left].lower() != s[right].lower():
        is_palindrome = False
        break

    # Move both pointers inward
    left += 1
    right -= 1

print(is_palindrome)