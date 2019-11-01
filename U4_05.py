#!/usr/bin/env python3

# Created by: Khang Le
# Created on: Sep 2019
# This program does some calculation



def main():
    # comment
    su = 0

    user_input = input("Enter how many time u want to add numbers: ")
    print("")

    # process & output
    try:
        user_number = int(user_input)

        for loop_counter in range(user_number):
            us_entered_number = int(input("Enter a number to add:"))
            if us_entered_number < 0:
                continue
            else:
                su = su + us_entered_number
        print("The sum of numbers are:{}".format(su))
                
           
    except Exception:
        print("This is not an integer")


if __name__ == "__main__":
    main()
