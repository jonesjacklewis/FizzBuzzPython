"""FizzBuzz Project
if a number is divisible by 3 output Fizz, if number is divisible by 5 output Buzz if both
output FizzBuzz otherwise output the number"""
def FizzBuzz(x, y):#Creating a FizzBuzz function, for numbers from x to y
    for i in range(x, y+1):#For numbers between x to y:
        out=""
        if i%3!=0 and i%5!=0:#if i is not a multiple of 3 or 5
            out+=str(i)#append the string form if i to out
        else:#otherwise
            if i%3==0:#if i is a multiple of 3
                out+="Fizz"#append the string Fizz to out
            if i%5==0:#if i is a multiple of 5
                out+="Buzz"
        print(out)#output the value of out

FizzBuzz(1,20)#perform the FizzBuzz funcrion for numbers between 1 and 100
