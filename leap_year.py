#!/usr/bin/env python3
# Created by: [Bestin]
# Created on: Nov 2025
# This program determines if a given year is a leap year.


def main():
    print("=== Leap Year Checker ===")
    try:
        year = int(input("Enter a year: "))

        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    print("Leap Year")
                else:
                    print("Not a Leap Year")
            else:
                print("Leap Year")
        else:
            print("Not a Leap Year")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    finally:
        print("Program finished.")


if __name__ == "__main__":
    main()
