"""
String end with ?

Description:
Complete the solution so that it returns true if the first argument(string) passed in ends with the 2nd argument (also a string).

Examples:

Inputs: "abc", "bc"
Output: true

Inputs: "abc", "d"
Output: false

"""

def solution(text, ending):
    end_len = len(ending)
    reverse = text[-end_len:]
    
    if reverse == ending:
        return True
    else:
        return False