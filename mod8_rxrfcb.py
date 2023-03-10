
#Iterate 1 to 100. If x is a multiple of 3 and 5 print fizzbuzz, otherwise if 3 is a factor print fizz, if 5 is a factor then print buzz
for x in range(1,101):
  if x%5 == 0 and x%3 == 0:
    print("FizzBuzz")
  elif x%5 == 0:
    print("Buzz")
  elif x%3 == 0:
    print("Fizz")
  else:
    print(x)
      
