#!/usr/bin/env python3
#=======================================================================
#
# level_20.py
# -----------
# Solution to 0xfat, level 20.
#
#=======================================================================

import hashlib

#-------------------------------------------------------------------
#-------------------------------------------------------------------
def get_input(filename):
    l = []
    with open(filename,'r') as f:
        for line in f:
            l.append(line.strip())
    return l


#-------------------------------------------------------------------
#-------------------------------------------------------------------
def find_hash(expected_digest):
    my_input = get_input("wordlist.txt")
    for i in range(len(my_input)):
        for j in range(len(my_input)):
            istr = my_input[i]
            jstr = my_input[j]
            my_str = istr + jstr
            digest = hashlib.md5(my_str.encode('utf-8')).hexdigest()

            if digest == expected_digest:
                print(my_str)
                return


#-------------------------------------------------------------------
#-------------------------------------------------------------------
print("0xfat level 20")
print("==============")
find_hash("52aab0d1b8b688817ba69d629004b25b")

#=======================================================================
#=======================================================================
