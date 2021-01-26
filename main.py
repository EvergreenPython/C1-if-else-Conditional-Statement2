'''
01/25/2021

------------------------------------------------------------------
Homework - data type

name = input("Enter your name: ")
age = int(input("Enter your age: "))
drink = input("Enter your favorite drink: ")
grade = input("Enter your grade: ")

print ("I am " + name + ".\nI am " + str(age) + " years old.\nMy favorite drink is " + drink + ".\nI am " + grade + " grade.")

print ("hi\t|\tbye")

------------------------------------------------------------------

Review - Operators

1. Math Operators (Arithmetic Opeartors)
  addition, +
  subtraction, -
  multiplication, *
  division, / (Exact answer)
  division, // (Quotient)
  modulo, % (Remainder)
  exponent, **

  5 / 2 = 2.5
  5 // 2 = 2
  5 % 2 = 1
  9 % 10 = 9
  8 % 2 = 0

2. Assignment Operators
  = assignment

  += Addition Assignment
  -= Subtract Assignment
  *=
  /=
  //=
  %=
  **=

  Rule:
  A variable must be declared before using assignment operators

  a = 0
  a += 4 >> a = a + 4


3. Comparison Operators
  == equal to
  != not equal to
  < less than
  <= less than or equal to
  > greater than
  >= greater than or equal to

  5 == 4  False
  6 >= 4  True
  0 != int("0") 


if/else conditional statement

if (CONDITION):
  BODY
else:
  BODY

if (CONDITION):
  BODY
if (CONDITION):
  BODY
if (CONDITION):
  BODY
if (CONDITION):
  BODY

'''

x = y = 32

if (x % 4 == 0):  # 32 % 4 = 0 == 0
  print ('I am hungry')

if (y % 16 == 0):  # 32 % 16 = 0 == 0
  print ('I want to play')
