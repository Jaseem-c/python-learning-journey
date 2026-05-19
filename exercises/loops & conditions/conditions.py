age = 20
if age >= 18:
  print("You are an adult")
  print("You can vote")
  print("You have full legal rights")
print("-"*20)

is_logged_in = True
if is_logged_in:
  print("Welcome back!")
print("-"*20)

a=10
if a>5:
  print("a is greater than 5")
elif a==5:
  print("a is equal to 5")
else:
  print("a is less than 5")

#short hand if
if a > 5: print("a is greater than 5")
print("a is greater than 5") if a > 5 else print("a is not greater than 5")

#pass
a = 10
if a > 5:
    pass
else:
    print("a is not greater than 5")
print("a is greater than 5")