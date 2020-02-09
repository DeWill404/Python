import math
# * Function for checking valid number type
def checkValid(select, n):
  if (select == 1): # Binary
    while (n > 0):
      d = n % 10
      if(d!=0 and d!=1):
        return 0
      n //= 10
    return 1
  elif (select == 3): # Octal
    while (n > 0):
      d = n % 10
      if(d > 7):
        return 0
      n //= 10
    return 1
  elif (select == 4): # Hexadecomal
    n = n.lower()
    lists = list(str(n))
    for i in range(len(lists)):
      if((lists[i] >= '0' and lists[i] <= '9') or (lists[i] >= 'a' and lists[i] <= 'f')):
        continue
      else:
        return 0;
    return 1

# * Functions to convert to other number system
# To convert to decimal
def toDecimal(n, base):
  decimal, power = 0, 0
  while (n > 0):
    d = n % 10
    decimal += d*math.pow(base,power)
    power += 1
    n //= 10    
  return int(decimal)
# To convert to binary
def toBinary(n):
  string = bin(n)
  return string[2:]
# To convert to octal
def toOctal(n):
  octal = str(oct(n))
  return octal[2:]
# To convert to hexadecimal
def toHex(n):
  hexadecimal = str(hex(n))
  return hexadecimal[2:]

# * Fuctions For respective no system
# Binary Number System
def binary():
  number = int(input("Enter the Binary No. : "))
  if (checkValid(1, number)):
    number = toDecimal(number, 2)
    print("\t -> Decimal Equivalent is", number)
    print("\t -> Octal Equivalent is", toOctal(number))
    print("\t -> Hexadecimal Equivalent is", toHex(number))
  else:
    print("\t\tEnter a Binary no....")
    binary()
# Decimal Number System
def decimal():
  number = int(input("Enter the Decimal No. : "))
  print("\t -> Binary Equivalent is", toBinary(number))
  print("\t -> Octal Equivalent is", toOctal(number))
  print("\t -> Hexadecimal Equivalent is", toHex(number))
# Octal Number System
def octal():
  number = int(input("Enter the Octal No. : "))
  if (checkValid(3, number)):
    number = toDecimal(number, 8)
    print("\t -> Binary Equivalent is", toBinary(number))
    print("\t -> Decimal Equivalent is", number)
    print("\t -> Hexadecimal Equivalent is", toHex(number))
  else:
    print("\t\tEnter a Octal no....")
    octal()
# Hexadecimal Number System
def hexadecimal():
  number = str(input("Enter the Hexadecimal No. : "))
  if (checkValid(4, number)):
    number = int(number, 16)
    print("\t -> Binary Equivalent is", toBinary(number))
    print("\t -> Decimal Equivalent is", number)
    print("\t -> Octal Equivalent is", toOctal(number))
  else:
    print("\t\tEnter a Hex no....")
    hexadecimal()

# ! Driver function
menu ='''
********* MENU *********
    1) Binary
    2) Decimal
    3) Octal
    4) Hexadecimal
************************
Enter : '''
continu = 1
while (continu == 1):
  # Creating a menu
  print(menu, end='')
  # Take input
  select = int(input())
  # Call respective function
  if (select == 1):
    binary()
  elif (select == 2):
    decimal()
  elif (select == 3):
    octal()
  elif (select == 4):
    hexadecimal()
  else:
    print("Please, Enter correct input.......")
  continu = int(input("Enter '1' to continue : "))