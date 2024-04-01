# Divadble by 3 = Fizz
# Divadble by 5 = Buzz
# Divadble by 3 and 5 = FizzBuzz


i = 0

while i < 100:
  
  i = i + 1
  if i % 3 == 0:

    if i % 5 == 0:
      print("FizzBuzz")
      continue

    print("Fizz")
    continue
  if i % 5 == 0:
    print("Buzz")
    continue

  print(i)
