# if ("hello" == "hello" or 3 == 8 or "brighticorn" == "code"):
#     print "welcome to class today!"
# else:
#     print "nothing is equal"


# x = 3
# if x == 3:
#         x = 4
#         if x == 4:
#                 print "x is 4"
# else:
#     x = 10
#     print "x is 10"


# input = raw_input("Do you know who Brighticorn is?")

# if (str.lower(input) == "yes"):
#     print "Great! She is a wonderful mascot"
# else:
#     print "Brighticorn is the Part Time Course Mascot!"


# "Defining" the function
# def my_function(name):
#     return "This is " + name + "'s function!"
# # "Calling" the function
# print my_function("Brighticorn")
# print my_function("Molly")

# def find_average(num1, num2):
#     total = num1 + num2
#     average = total / 2
#     return average


# def add(num1, num2):
#     return num1 + num2

# def average(num1, num2):
#     return add(num1, num2) / 2
# print average(5, 7)


# def average(num1, num2):
#     return add(num1, num2) / 2

# def add(num1, num2):
#     return num1 + num2

# print average(5, 7)


# def calculate_tip(bill_amount, percentage):
#     tip = bill_amount * percentage * 0.1
#     return tip

# def bill_splitter(bill_amount, tip_percentage, number_guests):
#     tip_amount = calculate_tip(bill_amount, tip_percentage)
#     bill_total = bill_amount + tip_amount
#     cost_per_person = bill_total / number_guests
#     return cost_per_person

# cost_per_guest = bill_splitter(138.46, 18, 4)
# print "Amount per person is: " + str(cost_per_guest)


def sum(number1, number2):
    return number1 + number2

print sum(2,3)

