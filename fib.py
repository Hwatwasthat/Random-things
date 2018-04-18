import random

# function to generate required fibonacci sequence
def fibonacci():
  sum = 0
  # intiate counter
  i = 1
  sum_of = 0
  
  # intiate list to iterate on
  main_list = [0, 1]
  
  # while loop to operate on list until highest number is less than 4 million
  while main_list[i] < 4000000:
    # add next number to end of list by addition of previous two numbers in list
    main_list.append(main_list[i] + main_list[i-1]) 
    i += 1
  
  # remove holding 0 from list
  main_list.remove(0)

  # remove all even integers from the list of fibonacci numbers (should remove to seperate function)
  sum = [x for x in main_list if x % 2 == 0]

  # adds up all of the numbers
  for i in range(len(sum)):
      sum_of += sum[i]
  return sum_of
  
print (str(fibonacci()))
