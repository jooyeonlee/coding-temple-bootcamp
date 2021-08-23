#!/usr/bin/env python3

import sys

def hello_name(user_name):
    print("hello_" + user_name)

def odd_numbers():
    count = 0
    for n in range(1, 200):
        if n % 2 == 1:
            count += 1
            print("Number {}: ".format(count) + str(n))

def max_num_in_list(a_list):
    temp_max = a_list[0]
    for num in a_list:
        if temp_max < num:
            temp_max = num
    return temp_max

def is_leap_year(a_year):
    if (a_year % 4 == 0) and (a_year % 100 != 0):
        return True
    elif a_year % 400 == 0:
        return True
    else:
        return False

def is_consecutive(a_list):
    return sorted(a_list) == list(range(min(a_list), max(a_list)+1))

def main(argv):
    hello_name(input("Input username:"))
    odd_numbers()
    num_list = [25, 60, 14, 35, 88, 2]
    print(max_num_in_list(num_list))
    print(is_leap_year(int(input("Input a year in YYYY format:"))))
    test_list = [1, 3, 2, 5, 9]
    print(is_consecutive(test_list))

if __name__ == "__main__":
    main(sys.argv)