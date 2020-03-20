#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'sortRoman' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY names as parameter.
#

def sortRoman(names):
    # Write your code here
    name_list = []
    rom_letter = {"I":1, "V":5, "X":10, "L":50} ### create dictionary for roman letters
    new_name = []
    diction = {}
    res = []

    for name in names:
        temp = name.split(" ") ### convert string into list
        name_list.append(temp)
    
    for name in name_list:
        for index, letter in enumerate(name[1]):
            if index == 0: 
                number = rom_letter[letter]
                preLetter = letter
            elif rom_letter[letter] <= rom_letter[preLetter]: ## look at the previous letter, if value is less than, do addition operation
                number += rom_letter[letter]
                preLetter = letter
            else: ## look at the previous letter, if value is larger than, do minus operation
                number = rom_letter[letter] - number
                preLetter = letter
        new_name.append((name[0], number))
        diction[(name[0], number)] = ' '.join(name)
    print("new name is ", new_name)
    print(diction) 
        #for i in temp:
        #    print(i)
    new_name.sort(key=lambda x: (x[0], x[1]))
    for name in new_name:
        print(diction[(name)])
        res.append(diction[(name)])
    #name_list.sort(key=lambda x: (x[0], x[1]))
    print(new_name)
    print(res)
    #print(names)

    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    names_count = int(input().strip())

    names = []

    for _ in range(names_count):
        names_item = input()
        names.append(names_item)

    result = sortRoman(names)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
