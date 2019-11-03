"""
author: avichay ben lulu 301088670
decimal to roman program
"""


"""
input: num
output: roman_num as string
goal: replace decimal number in roman number - using dictionary to pull out the right number

"""


def int_to_roman(num):
    dictionary = {"I": 1, "IV": 4, "V": 5, "IX": 9, "X": 10, "XL": 40, "L": 50, "XC": 90,
                  "C": 100, "CD": 400, "D": 500, "MC": 900, "M": 1000}
    range_flag = None
    for roman, decimal_nums in dictionary.items():
        # for the simple case
        if decimal_nums == num:
            return roman
        # if not - give me range - the most high value decimal in the dictionary and set it as "range_flag"
        if num > decimal_nums:
            range_flag = roman
    # new_num = num - the dictionary value of the roman flag
    new_num = num - dictionary[range_flag]
    # then return "range_flag" value + recursively the new_num
    return range_flag + int_to_roman(new_num)


print(int_to_roman(int(input(f'please enter decimal number'))))
