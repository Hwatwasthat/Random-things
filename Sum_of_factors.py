<<<<<<< HEAD
# Formula based Python3 code to find 
# sum of all divisors of n.
import math as m
 
# Returns sum of all factors of n.
def sumofFactors(n):
     
    # Traversing through all
    # prime factors
    res = 1
    for i in range(2, int(m.sqrt(n) + 1)):
        count = 0
        curr_sum = 1
        curr_term = 1
         
        while n % i == 0:
            count = count + 1
            n = n / i;
 
            curr_term = curr_term * i;
            curr_sum += curr_term;
            print(f'Count: {count}\n i: {i} n: {n}, Curr_term: {curr_term}, curr_sum: {curr_sum}\n')
             
        res = res * curr_sum
     
    # This condition is to handle the 
    # case when n is a prime number 
    # greater than 2
    if n > 2:
        res = res * (1 + n)
 
    return res;
 
# driver code    
sum = sumofFactors(200)
print ("\nSum of all divisors is: ",sum)
=======
# Formula based Python3 code to find 
# sum of all divisors of n.
import math as m
 
# Returns sum of all factors of n.
def sumofFactors(n):
     
    # Traversing through all
    # prime factors
    res = 1
    for i in range(2, int(m.sqrt(n) + 1)):
        count = 0
        curr_sum = 1
        curr_term = 1
         
        while n % i == 0:
            count = count + 1
            n = n / i;
 
            curr_term = curr_term * i;
            curr_sum += curr_term;
            print(f'Count: {count}\n i: {i} n: {n}, Curr_term: {curr_term}, curr_sum: {curr_sum}\n')
             
        res = res * curr_sum
     
    # This condition is to handle the 
    # case when n is a prime number 
    # greater than 2
    if n > 2:
        res = res * (1 + n)
 
    return res;
 
# driver code    
sum = sumofFactors(200)
print ("\nSum of all divisors is: ",sum)
>>>>>>> 7e1264f782abda423dc21c11e901e4507678a674
