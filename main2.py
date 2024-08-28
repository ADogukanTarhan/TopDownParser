from methods import *


def lex(count,next_token):
    file = open("input.txt", "r")
    data = file.read().split()
    count += 1

    next_token += data[count-1]
    return data[count-1]

# get remaining inputs
def unconsumed_input(count):
    file = open("input.txt", "r")
    data = file.read().split()

    elements = data[count:-1]
    elementString =""
    for i in elements:
        elementString += i + " "
    if elementString == "":
        return "$"
    else:
        return elementString


# start grammar  G -> E
def G(count, error,next_token,tree):
    print("Remaining input : " + unconsumed_input(count))
    print("Next token : " + next_token)
    print("G -> E")
    E(count,error,next_token,tree)
    if next_token == "$" and not(error) :
        print("Success")
    else:
        lex(count,next_token)

# check  E -> T R
def E(count, error,next_token,tree):
    if error:
        return "error"
    print("E -> T R")
    if next_token == "+" or next_token == "-":
        R(count, error, next_token,tree)
    else:
        T(count,error,next_token,tree)


# check  R -> + T R | - T R | e
def R(count, error,next_token,tree):
    if error:
        return "error"
    if next_token == "+":
        print("R -> + T R")
        if (data[count-1] == "0" or data[count-1] == "1" or data[count-1] == "2" or data[count-1] == "3") and (data[count+1] == "0" or data[count+1] == "1" or data[count+1] == "2" or data[count+1] == "3"):
            tree.append([data[count-1], "+", data[count+1]])
            lex(count, next_token)
            print(tree)
        elif data[count+1] == "(":
            tree.append([data[count-1], "+",  data[count+1], data[count+2], data[count+3], data[count+4], data[count+5]])
            print(tree)
        else:
            pass

    elif next_token == "-":
        print("R -> - T R")
        if (data[count-1] == "0" or data[count-1] == "1" or data[count-1] == "2" or data[count-1] == "3") and (data[count+1] == "0" or data[count+1] == "1" or data[count+1] == "2" or data[count+1] == "3"):
            tree.append([data[count-1], "-", data[count+1], data[count+2], data[count+3], data[count+4]])
            lex(count, next_token)
            print(tree)
        elif data[count+1] == "(":
            tree.append([data[count-1], "+",  data[count+1], data[count+2], data[count+3], data[count+4], data[count+5]])
            print(tree)
        else:
            pass

    elif next_token == "$":
        pass
    else:
        print("R -> e")

# check T -> F S
def T(count, error, next_token,tree):
    if error:
        return "error"

    print("T -> F S")
    if next_token == "*" or next_token == "/":
        S(count, error, next_token,tree)
    else:
        F(count,error, next_token,tree)


# check S -> * F S | / F S | e
def S(count, error, next_token,tree):
    if error:
        return "error"
    if next_token == "*":
        print("S -> * F S")
        if (data[count-1] == "0" or data[count-1] == "1" or data[count-1] == "2" or data[count-1] == "3") and (data[count+1] == "0" or data[count+1] == "1" or data[count+1] == "2" or data[count+1] == "3"):
            tree.append([data[count-1], "*", data[count+1]])
            lex(count, next_token)
            print(tree)
        elif data[count+1] == "(":
            tree.append([data[count-1], "*", data[count+1], data[count+2], data[count+3], data[count+4], data[count+5]])
            print(tree)
        else:
            pass


    elif next_token == "/":
        print("S -> / F S")
        if (data[count - 1] == "0" or data[count - 1] == "1" or data[count - 1] == "2" or data[count - 1] == "3") and (
                data[count + 1] == "0" or data[count + 1] == "1" or data[count + 1] == "2" or data[count + 1] == "3"):
            tree.append([data[count - 1], "/", data[count + 1]])
            lex(count, next_token)
            print(tree)
        elif data[count + 1] == "(":
            tree.append([data[count - 1], "/", data[count + 1], data[count + 2], data[count + 3],
                         data[count + 4], data[count+5]])
            print(tree)
        else:
            pass

    elif next_token == "$":
        pass
    else:
        print("S -> e")


# check F -> ( E ) | N
def F(count,error, next_token,tree):
    file = open("input.txt", "r")
    data = file.read().split()

    left_para = 0
    right_para = 0

    for i in data:
        if i == "(":
            left_para += 1
        elif i == ")":
            right_para += 1

    if error:
        return "error"
    elif next_token == "a" or next_token == "b" or next_token == "c" or next_token == "d":
        print("F -> M")
        M(count, error, next_token,tree)
    elif next_token == "0" or next_token == "1" or next_token == "2" or next_token =="3":
        print("F -> N")
        N(count, error, next_token,tree)

    elif next_token == "(":
        if ")" in data:
            print("F -> (E)")
            count += 1
            new_next_token = lex(count, next_token)
            lex(count, next_token)
            E(count,error,new_next_token,tree)
        else:
            print("Failure: Expected ')' ")
            exit()
    elif next_token == ")":
        if "(" not in data:
            print("Failure: Expected '(' ")
            exit()
        else:
            count += 1
            lex(count,next_token)
    elif left_para != right_para:
        print("Failure : Parantheses don't match!")
        exit()
    elif next_token == "$":
        pass
    else:
        error = True
        print("Error: Unexpected Token --> " + next_token)
        print("Unconsumed Input --> " + unconsumed_input(count))
        exit()

# check M -> a | b | c | d *
def M(count, error, next_token,tree):
    if error:
        return "error"
    if next_token == "a" or next_token == "b" or next_token == "c" or next_token == "d":
        print("M -> " + next_token)
        lex(count, next_token)
    elif next_token == "$":
        pass
    else:
        error =True
        print("Error: Unexpected Token --> " + next_token)
        print("Unconsumed Input --> " + unconsumed_input(count))

# check N -> 0 | 1 | 2 | 3
def N(count, error, next_token,tree):
    if error:
        return "error"
    if next_token == "0" or next_token == "1" or next_token == "2" or next_token =="3":
        print("N -> " + next_token)

        lex(count, next_token)
    elif next_token == "$":
        pass
    else:
        error =True
        print("Error: Unexpected Token --> " + next_token)
        print("Unconsumed Input --> " + unconsumed_input(count))



file = open("input.txt", "r")
data = file.read().split()

error = False
next_token = ''
count = 0
tree = []

while count < len(data):
    next_token = data[count]
    G(count, error, next_token,tree)
    count += 1
print(tree)