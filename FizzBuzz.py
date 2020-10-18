"""FizzBuzz Project
if a number is divisible by 3 output Fizz, if number is divisible by 5 output Buzz if both
output FizzBuzz otherwise output the number"""


def fizz_buzz(x, y):  # Creating a FizzBuzz function, for numbers from x to y
    for i in range(x, y + 1):  # For numbers between x to y:
        out = ""  # Default output value
        if i % 3 == 0:  # If i is a multiple of 3
            out += "Fizz"  # Append Fizz to out
        if i % 5 == 0:  # If i is a multiple of 5
            out += "Buzz"  # Append Buzz to out
        if out == "":  #  If nothing has been appended to out
            out = str(i)  # Set out to string representation of i
        print(out)  # print the value of out


fizz_buzz(1, 100)  # perform the FizzBuzz function for numbers between 1 and 100
