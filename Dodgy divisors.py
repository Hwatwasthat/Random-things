def divisors(Num):
    list_divisors = 0
#iterate over numbers in range
    for i in range(1, int(Num /2) + 1):
  
  #check if number is divisor by checking if number modulo it is 0
        if Num % i == 0:
    
    #add number to list if divisor
            list_divisors += 1
      
    return list_divisors

def main():
    div_num = 0
    i = 500500507
    while div_num < 2 ** 500500:
        i += 1
        div_num = divisors(i)
        print(i, div_num)

    print(f"\n{div_num}")
    print(f"\n{i}")
    print(f"\n{i % 500500507}")

main()
