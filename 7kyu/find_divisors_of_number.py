"""
Find the divisors!

Description:
Create a function named divisors/Divisors that takes an integer n > 1 and returns an array with all of the integer's divisors(except for 1 and the number itself), from smallest to largest. If the number is prime return the string '(integer) is prime' (null in C#, empty table in COBOL) (use Either String a in Haskell and Result<Vec<u32>, String> in Rust).

Examples:
divisors(12) --> [2, 3, 4, 6]
divisors(25) --> [5]
divisors(13) --> "13 is prime"
"""

def divisors(integer):
    div_list = []
    for i in range(1, integer):
        #print(i)
        if i == 1:
            pass
        elif integer % i == 0:
            div_list.append(i)
            #print("inside if", i)
    if not div_list:
        return f"{integer} is prime"
    return div_list