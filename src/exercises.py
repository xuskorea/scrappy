
#Aqui lo que hago es hacer un bucle multiplicando el numero por el anterior hasta que el reultado es 1
def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

#Aqui calculo el inverso y comparo si es igual al normal
def isPalindrome(palindrome):
    if palindrome == palindrome[::-1]:
        return 'si'
    return 'no'