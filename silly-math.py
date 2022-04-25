#   Goals:
#   If even: X/2
#   If odd : 3x+1
inputStr = input("Number for solver:")
number = int(inputStr)
mathList = [number]


def solver3Nplus1(number):
    if number % 2 == 0:
        number2 = number/2
        number = number2
    else:
        number2 = 3*number+1
        number = number2
    if number2 in mathList:
        mathList.append(number2)
        return mathList
    else:
        mathList.append(number2)
        return (solver3Nplus1(number2))


print(solver3Nplus1(number))
