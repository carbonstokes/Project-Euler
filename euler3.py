"""The prime factors of 13195 are 5, 7, 13 and 29. What is the largest prime factor of the number 600851475143 ?"""
#find how many prime factors there are in the number given
#list those numbers
#find the biggest prime number that factors into this
#print the list of the prime numbers for it and then print the highest one
#each number has a certain, unique number of prime numbers it is a product of, so we just need to find the largest one out of that series!


import math

maxvalue = 600851475143

def primefactor():
    """returns a list of the prime number factors for a given number"""

    primecheck = 2
    primeanswer = maxvalue
    while primecheck < primeanswer:
        if (primeanswer%primecheck == 0):
            primeanswer = primeanswer/primecheck
            print(primecheck)
        else:
            primecheck = primecheck + 1
    print(primecheck)



primefactor()
