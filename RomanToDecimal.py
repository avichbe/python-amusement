"""
author: avichay ben lulu 301088670
Roman to decimal function
"""

"""
input: num
output: num after validity check to roman_to_int()
goal: check validity
"""


def roman_validity(num):
    num = num.upper()
    roman_val = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    for i in range(len(num)):
        if num[i] not in roman_val:
            return print("please check your romance ")
    return roman_to_int(num)


"""
input: roman num
output: decimal number  
goal: return int from roman digits
"""


def roman_to_int(num):
    dictionary = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90,
                  "C": 100, "CD": 400, "D": 500, "MC": 900, "M": 1000}
    range_flag = 0
    if num == "":
        return
    for roman, decimal_nums in dictionary.items():
        # for the simple case
        if roman == num[-1] and len(num) == 1:
            return decimal_nums
        # if not - give me range - the most high value decimal in the dictionary and set it as "range_flag"
        if roman == num[-1]:
            range_flag = decimal_nums
    # new_num = num - the dictionary value of the roman flag
    new_num = num[:-1]
    # then return "range_flag" value + recursively the new_num
    return range_flag + roman_to_int(new_num)


print(roman_validity(input('please enter roman number')))