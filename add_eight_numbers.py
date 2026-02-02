#!/usr/bin/env python3
"""
Script to add 8 numbers entered by the user.
"""

def main():
    """
    Prompts the user for 8 numbers and displays their sum.
    """
    print("This program will add 8 numbers.")
    print("-" * 40)
    
    numbers = []
    
    # Get 8 numbers from the user
    for i in range(1, 9):
        while True:
            try:
                num = float(input(f"Enter number {i}: "))
                numbers.append(num)
                break
            except ValueError:
                print("Invalid input! Please enter a valid number.")
    
    # Calculate the sum
    total = sum(numbers)
    
    # Display results
    print("-" * 40)
    print(f"The 8 numbers you entered: {numbers}")
    print(f"Sum of all numbers: {total}")
    
if __name__ == "__main__":
    main()
