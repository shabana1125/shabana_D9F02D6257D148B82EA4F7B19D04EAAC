

"""
1! = 1 x 1
2! =2 x 1! --->2 x 1
3! = 3 x 2! ---> x 2 x 1
.
.
10! = 10 x 9!  --->10 x9 x8 x... x 1

formula - n x (n-1)
"""


def fact_rec(n):
   if n==0 or n==1:
     return 1
   else:
      return n*fact_rec(n-1)

number = 4
res = fact_rec(number)

print("The factorial of {} is {}.".format(number,res))