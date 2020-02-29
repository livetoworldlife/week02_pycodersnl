
"""
the Fibonacci numbers, commonly denoted Fₙ form a sequence, called the Fibonacci sequence,
 such that each number is the sum of the two preceding ones, starting from 0 and 1. That is, and for n > 1
"""
use_int = int(input("Enter a number to find Fibonacci numbers until this number ; "))

    # first two numbers must be 0 and 1
nt, n1, n2 = 0, 0, 1
sto_list = [0,1]

    # check if the number is larger than 1
if use_int <= 1:
   print("Fibonacci sequence starts from 0 and 1 so Please Enter a number larger than 1 ; ")
else:
   while max(sto_list) <= use_int:
       nt = n1 + n2
       sto_list.append(nt)
       n1 = n2
       n2 = nt
   del sto_list[-1]
   sto_tuple = tuple(sto_list)
   print("Fibonacci sequence:", sto_tuple)

# ############################################################# The End 

