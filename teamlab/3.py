
def FB(n):
    if n % 3 == 0 and n % 5 == 0:
        return "FizzBuzz"
    elif n % 3 == 0:
        return "Fizz"
    elif n % 5 == 0:
        return "Buzz"
    else:
        return str(n)

total = sum([n for n in range(1, 50001) if len(FB(n)) == 4])
print(total)

# Output:526397003