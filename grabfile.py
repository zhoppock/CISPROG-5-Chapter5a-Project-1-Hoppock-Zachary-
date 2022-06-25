def grabfile():
  fileName = input("Enter filename of numbers: ")
  f = open(fileName, 'r')

  numbers = []
  for line in f:
    words = line.split()
    for word in words:
      numbers.append(float(word))
  print("Your sequence of numbers from", fileName, "are\n", numbers)
  return numbers