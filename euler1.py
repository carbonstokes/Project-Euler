

#If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

#Find the sum of all the multiples of 3 or 5 below 1000.


#find a way of adding all the muliples of 3 together under 1000#

#find a way of adding all the muliples of 5 together under 1000#
#this has to be between 0 and 999 not including 0 or 1000#

def eulerproblem1():
 maxval = 1000
  for i in range(maxval):
       if (i % 3 == 0):
        print(i)


eulerproblem1()
