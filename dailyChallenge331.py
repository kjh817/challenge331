# ------------------------------------
# Daily Programming Challenge #331
# File Name: dailyChallenge.py
# Author: Kassell Harris
# Published: June 2017
#
# Goal: Create a calculator using only
# addition.
# Instructions found in instructions.txt
# ------------------------------------


# ------------------------------------
# add function
# takes two int inputs and returns sum
# ------------------------------------
def add(num1, num2):
    return num1 + num2


# ------------------------------------
# subtract function
# takes two int inputs and returns difference
# ------------------------------------
def subtract(num1, num2):
    answer = 0
    if num1 > num2:
        while num2 < num1:
            answer += 1
            num2 += 1

    elif num2 > num1:
        while num1 < num2:
            answer += 1
            num1 += 1
        answer = int("-" + str(answer))
    return answer


# ------------------------------------
# sign change function
# takes one int input and reverse
# the sign (+ -> -) or (- -> +)
# ------------------------------------
def signChange(num):
    if num < 0:
        answer = 0  # type: int
        while num != 0:
            num += 1
            answer += 1
        return answer

    return int("-" + str(num))


# ------------------------------------
# multiply function
# takes two int inputs and returns product
# ------------------------------------
def multiply(num1, num2):
    answer = 0  # type: int
    count = 0  # type: int
    if num1 == 0 or num2 == 0:
        return answer

    elif num1 < 0 and num2 < 0:
        num1 = signChange(num1)
        num2 = signChange(num2)
        count = 0  # type: int

        while count < num2:
            answer = num1 + answer
            count = count + 1

        return answer

    elif num1 > 0 and num2 > 0:
        while count < num2:
            answer = num1 + answer
            count = count + 1
        return answer

    else:
        if num1 < 0:
            num1 = signChange(num1)
        else:
            num2 = signChange(num2)
        while count < num2:
            answer = num1 + answer
            count = count + 1
        return signChange(answer)


# ------------------------------------
# divide function
# takes two int inputs and returns quotient
# ------------------------------------
def divide(num1, num2):
    answer = 0
    count = 0

    if num2 == 0:
        return "Not-defined"

    elif num1 == 0:
        return 0

    elif num1 == num2:
        return 1

    elif (num1 > 0 and num2 > 0) or (num1 < 0 and num2 < 0):
        if num1 < 0:
            num1 = signChange(num1)
            num2 = signChange(num2)

        while count < num1:
            count = count + num2
            answer = answer + 1

        if multiply(answer, num2) == num1:
            return answer
        else:
            return "Non-integral answer"

    elif num1 < 0 or num2 < 0:
        if num1 < 0:
            num1 = signChange(num1)
        else:
            num2 = signChange(num2)

        while count < num1:
            count = count + num2
            answer = answer + 1

        if multiply(answer, num2) == num1:
            return signChange(answer)
        else:
            return "Non-integral answer"


# ------------------------------------
# exponent function
# takes two int inputs, where num1 is
# is raised to the power of num2
# ------------------------------------
def exponent(num1, num2):
    if num2 < 0:
        return "Non-integral answer"

    elif num2 == 0:
        return 1

    elif num2 == 1:
        return num1

    else:
        answer = 1
        count = 0
        while count < num2:
            answer = multiply(answer, num1)
            count = count + 1

        return answer



# test code

# print("12 + 25 = " + str(add(12, 25)))
# print("-30 + 100 = " + str(add(-30, 100)))
#
# print("100 - 30 = " + str(subtract(100, 30)))
# print("100 - -30 = " + str(subtract(100, -30)))
# print("-25 - 29 = " + str(subtract(-25, 29)))
# print("-41 - -10 = " + str(subtract(-41, -10)))
#
# print("9 * 3 = " + str(multiply(9, 3)))
# print("9 * -4 = " + str(multiply(9, -4)))
# print("-4 * 8 = " + str(multiply(-4, 8)))
# print("-12 * -9 = " + str(multiply(-12, -9)))
#
# print("100 / 2 = " + str(divide(100, 2)))
# print("75 / -3 = " + str(divide(75, -3)))
# print("-75 / 3 = " + str(divide(-75, 3)))
# print("7 / 3 = " + str(divide(7, 3)))
# print("0 / 0 = " + str(divide(0, 0)))
#
#
# print("5 ^ 3 = " + str(exponent(5, 3)))
# print("-5 ^ 3 = " + str(exponent(-5, 3)))
# print("-8 ^ 3 = " + str(exponent(-8, 3)))
# print("-1 ^ 1 = " + str(exponent(-1, 1)))
# print("1 ^ 1 = " + str(exponent(1, 1)))
# print("0 ^ 5 = " + str(exponent(0, 5)))
# print("5 ^ 0 = " + str(exponent(5, 0)))
# print("10 ^ -3 = " + str(exponent(10, -3)))


# ------------------------------------
# getinput function
# gets a single number input from user
# and returns the number
# ------------------------------------
def getInput():
    num = input("Please enter a number:")
    if  num == "q" or num == "Q":
        quit()
    while num.isalpha():
        num = input("Please enter a number:")
        if num == "q" or num == "Q":
            quit()
    num = int(num)
    return num

# ------------------------------------
# get operator function
# gets a single mathematical operation
# from user and returns the operator
# ------------------------------------
def getOperation():
    op = input("Please enter an operator:")
    if op == "q" or op == "Q":
        quit()
    while op != "+" and op != "-" and op != "*" and op != "/" and op != "^":
        op = input("Please enter an operator:")
        if op == "q" or op == "Q":
            quit()
    return op

# ------------------------------------
# compute function
# computes user inputs
# ------------------------------------
def compute():
    num1 = getInput()
    num2 = getInput()
    operator = getOperation()

    if operator == "+":
        answer = add(num1, num2)
    elif operator == "-":
        answer = subtract(num1, num2)
    elif operator == "*":
        answer = multiply(num1, num2)
    elif operator == "/":
        answer = divide(num1, num2)
    elif operator == "^":
        answer = exponent(num1, num2)

    print(str(answer))


# ------------------------------------
# main calculator loop
# ------------------------------------
print("Enter 'q' or 'Q' to quit")
while True:
    compute()