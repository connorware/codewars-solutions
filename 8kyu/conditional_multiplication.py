"""
Simple Multiplication

Description:
This kata is about multiplying a given number by eight if it is an even number and by nine otherwise.
"""
def simple_multiplication(number) :
    if number % 2 == 0:
        answer = number * 8
    else:
        answer = number * 9
    return answer