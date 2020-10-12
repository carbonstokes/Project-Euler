#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.#
#Limit the range of numbers that can be tested
#see if that number can be reversed






def answer():
    palindrome = 0 #define your first variable
    for i in range(999, 99, -1):  # 100 to 1000 in incredmental -1 steps
        for j in range(999, 99, -1):
            product = str(i * j) #make the numbers strings
            if product == str(i * j)[::-1]: #then reverse the string! :)
                palindrome = max(palindrome, i * j) #this then checks for the max value between i and j 
    return palindrome
print (answer())
