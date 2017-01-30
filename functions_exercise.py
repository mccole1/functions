#Functions Part 1:

def hello_print():
    print "hello"

#print hello_print() #prints hello /n None
#print hello_print(hi) #error: 'hi' not defined
#greeting = hello_print()
#print greeting #prints hello /n None


def hello_return():
    return "hello"

#print hello_return() #prints hello
#greeting = hello_return()
#print greeting #prints hello


def hello_name(name):
    print "hello," , name

#print hello_name() #error: needs argument
#print hello_name(molly) #error: molly not defined
# partner_name = "Molly"
# print hello_name(partner_name) #prints hello, Molly
# print hello_name() #error: needs argument


#Functions Part 2:


def add(num1, num2):
    return num1 + num2

#print add(4, 5) #prints 9


def subtract(num1, num2):
    return num1 - num2

#print subtract(4, 5) #prints -1


def multiply(num1, num2):
    return num1 * num2

#print multiply(4, 5) #prints 20


def divide(num1, num2):
    return num1 / num2

#print divide(4.0, 5.0) #prints 0.8


def modulo(num1, num2):
    return num1 % num2

#print modulo(4, 5) #prints 4


def power(base, exponent):
    return base ** exponent

#print power(4, 5) #prints 1024


def square(num):
    return power(num, 2)

#print square(4) #prints 16


def main():
    #(4+5) + (9-6)
    print add(4, 5) + subtract(9, 6) #prints 12

    #(12/2) - 60
    print divide(12, 2) - 60 #prints -54

    #1 + 2 + 3
    print add(add(1, 2), 3) #prints 6

    #(1+2) ^ 2
    print square(add(1, 2)) #prints 9

    #(3%4) / (9*9)
    print divide(modulo(3.0, 4.0), multiply(9, 9)) #prints 0.037

    #(1+2) - 3 * (4+5)
    print subtract(add(1, 2), multiply(3, add(4, 5))) #prints -24

    #3 ^ (2+3)
    print power(3, add(2, 3)) #prints 243


if __name__ == "__main__":
    main()









