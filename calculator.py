def add(n1, n2):
    return n1 + n2

# TODO 1: Write out the other 3 functions - subtract, divide, multiply.

def subtract (n1, n2):
    return n1 - n2

def divide (n1, n2):
    return n1 / n2

def multiply (n1, n2):
    return n1 * n2

# TODO 2: Add these 4 values to the dictionary. Example: key: "+", "-", "*"..
# Takto bez variables v závorce nevyvolávám funkci, ale pouze ji ukládám pod jiným jménem
operations = {"+": add,
              "-": subtract,
              "*": multiply,
              "/": divide}

#TODO 3: Use the dictionary operations to perform the calculation. Multiply 4 * 8 using dictionary

# vyvolá mi to z dict. operations pod klíčovým slovem "*" funkci multiply,
# přičemž jsou na pevno nastavené parametry 4 a 8
#print((operations ["*"])(4,8))

# Kalkulátor začíná zde!

import art
print(art.logo)
num1 = float(input("Jaké je první číslo?: "))
while 0 < 1:
    print("+\n-\n*\n/")
    operator = input("Vyber operaci z nabídky výše: ")
    num2 = float(input("Jaké je druhé číslo?: "))
    equality = round(operations [operator](n1 = num1, n2 = num2),3)
    print(f'{num1} {operator} {num2} = {equality}')
    continue_with_prev = input(f"Napiš 'y' pro pokračování výpočtu s {equality} "
                           f"nebo napiš 'n' pro zcela nový výpočet: ")
    if continue_with_prev == "y":
        num1 = equality
    else:
        print("\n" * 50)
        print(art.logo)
        num1 = float(input("Jaké je první číslo?: "))