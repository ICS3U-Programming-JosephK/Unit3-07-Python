#!/usr/bin/env python3

# Created by: Joseph Kwon
# Created on: Oct 18, 2022
# This program checks if the user is eligible in dating the computer's grandchild


def main():
    # this function uses a try statement

    # asks the user for input (their age)
    print("Are you eligible to date my grandchild?")
    # had to remove "int" or "float" when asking for input here
    user_age = input("What is your age: ")

    # process and output
    try:
        user_age = int(user_age)
        # check if the user's age is between 25 and 45
        if user_age >= 25 and user_age <= 40:
            print("You can date my grandchild")

        # else, if the user's age is too young or old
        else:
            print(
                f"You are not eligible in dating my grandchild, your age is {user_age}"
            )
    # similar to an else statement, if an integer is not inputted...
    except:
        print(f"{user_age} is not a valid age. Please enter a valid age")


if __name__ == "__main__":
    main()
