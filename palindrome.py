def is_palindrome(s):
    s = s.lower()   #convert to lowercase
    reverse_s = s[::-1]  #Reverse the string
    return s== reverse_s  #Compare original and reversed strings
s= input('Enter any name: ')
print(is_palindrome(s))