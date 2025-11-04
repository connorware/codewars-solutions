"""
Even and Odd

Description:
Given a number N, can you fabricate the two numbers NE and NO such that NE is formed by even digits of N and NO is formed by odd digits of N? Examples:

Example:
Input:  126453
Output: NE = 264, NO = 153

Input:  3012
Output: NE = 2, NO = 31

Input:  4628
Output: NE = 4628, NO = 0

0 is considered as an even number.

In C and JavaScript you should return an array of two elements such as the first is NE and the second is NO.
"""

def even_and_odd(n): 
    s = str(n)
    even_s, odd_s = "", ""
    for c in s:
        if int(c) % 2 == 0:
            even_s = even_s + c
        else:
            odd_s = odd_s + c

    int_even = int(even_s) if even_s else 0 
    int_odd = int(odd_s) if odd_s else 0

    return (int_even, int_odd)