

def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

def isPalindrome(palindrome):
    if palindrome == palindrome[::-1]:
        return 'yes'
    return 'no'