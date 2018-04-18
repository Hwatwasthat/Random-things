from math import sqrt
def is_prime(n):
    
    if n % 2 == 0 and n > 2:
        return
    for i in range(3, int(sqrt(n)) + 1, 2):
        if n % i == 0:
            return
    return n

def divisors(Num):
    #Ensure number is positive
    if Num <= 0:
      print("Number must be positive")
      quit()

    #create list for all divisors
    list_divisors = []

    #iterate over numbers in range
    for i in range(2,int(sqrt(Num)+1)):
  
      #check if number is divisor by checking if number modulo it is 0
      if Num % i == 0:
    
        #add number to list if divisor
        list_divisors.append(i)

    return(list_divisors)

def main(n):
    divisors2 = []
    primes = []
    divisors2 = divisors(n)
    for i in range(1, len(divisors2)):               
        primes.append(is_prime(divisors2[i]))
    print(primes)

main(600851475143)
