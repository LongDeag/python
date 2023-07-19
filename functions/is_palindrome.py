def reverse_string(str):
    word_length = len(str)
    if word_length == 0:
        return ""
    else:
        return reverse_string(str[1:]) + str[0]
def is_palindrome(str):
    reverse_str = reverse_string(str).replace(" ", "")
    new_str = str.replace(" ", "")
    if reverse_str == new_str:
        return "YES"
    else:
        return "NO"

print(is_palindrome("borrow or rob"))