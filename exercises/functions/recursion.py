# recursion- a function that calls itself
def countdown(n):
    if n <= 0:
        print("Done!")
    else:
        print(n)
        countdown(n - 1)


countdown(5)


def factorial(n):
    # base case
    if n == 0:
        return 1
    else:
        # recursive case
        return n * factorial(n - 1)


print(factorial(5))

# Base Case and Recursive Case
