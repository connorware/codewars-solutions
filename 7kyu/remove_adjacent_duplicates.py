"""
Stones on the Table 

Description:
There are some stones on Bob's table in a row, and each of them can be red, green or blue, indicated by the characters R, G, and B.

Help Bob find the minimum number of stones he needs to remove from the table so that the stones in each pair of adjacent stones have different colors.

Examples:

"RGBRGBRGGB"   => 1
"RGGRGBBRGRR"  => 3
"RRRRGGGGBBBB" => 9
"""

def solution(stones):
    count = 0
    for i in range(len(stones)-1):
            # print(i)
            if stones[i+1] == stones[i]:
                # new_stones = stones.replace(stones[i], "")
                count = count + 1

    return count