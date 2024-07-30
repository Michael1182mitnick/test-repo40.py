# Write a program to check if a given string is a palindrome.

def is_palindrome(text):
    
    length = len(text)

    for i in range(0, length // 2):
        if (text[i] != text[length - i - 1]):
            return False
    return True

input_text = input("enter any word: ")
result = is_palindrome(input_text)
print(result)