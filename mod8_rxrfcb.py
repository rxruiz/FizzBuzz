def fizz_buzz():
  for x in range(1,101):
    if x%5 != 0 and x%3 != 0:
      print(x)
    else:
      if x%3 == 0:
        print("Fizz")
      if x%5 == 0:
        print("Buzz")
