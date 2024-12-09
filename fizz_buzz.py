# Prints numbers 1-100.
# For multiples of 3 prints Fizz and for multiples of 5 prints Buzz.
# For numbers which are multiples of both three and five print “FizzBuzz”.


for x in range(1, 101):
    string = ""
    if x % 3 == 0:
        string += "Fizz"
    if x % 5 == 0:
        string += "Buzz"
    if x % 5 != 0 and x % 3 != 0:
        string += str(x)
    print(string)