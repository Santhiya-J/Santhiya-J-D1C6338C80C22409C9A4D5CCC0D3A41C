def fact(n):
  if n == 0 or n == 1:
    return 1
  else:
    return n * (fact(n - 1))


number = int(input("Enter a number: "))
result = fact(number)
print("The factorial of ", number, "is", result)
