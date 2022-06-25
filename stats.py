import statistics

def median(numbers):
  numbers.sort()
  midpoint = len(numbers) // 2
  print("\nThe median is ", end = "")
  if len(numbers)% 2 == 1:
    print(numbers[midpoint])
  else: 
    print((numbers[midpoint] + numbers[midpoint - 1])/ 2)

def mode(numbers):
  numbers.sort()
  m = statistics.mode(numbers)
  print("\nThe mode is", m)

def mean(numbers):
  numbers.sort()

  sum = 0
  for value in numbers:
    sum += value
  mean = sum/(len(numbers))
  print("\nThe mean is", mean)