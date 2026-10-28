#!/usr/bin/env python3

try:
    number = float(input("Give me a number: "))

    if number == int(number) :
      print("This number is an integer.")
    else: 
      print("This number is a decimal.")

except ValueError : 
    print("Input has to be numerical value")