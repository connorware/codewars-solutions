"""
Vowel Count 

Description:
Return the number (count) of vowels in the given string.

We will consider a, e, i, o, u as vowels for this Kata (but not y).

The input string will only consist of lower case letters and/or spaces.
"""

def get_count(sentence):
    vowels = ["a", "e", "i", "o", "u"]

    vowel_count = 0
    for vowel in vowels:
        if vowel in sentence:
            vowel_count = vowel_count + sentence.count(vowel) 
    return vowel_count

