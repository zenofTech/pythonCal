"""
Created by: ZenOfTech
Date: 23-01-2023
Email: amuktar064@gmail.com
site: amuktar.github.io/muktar
"""

# This print function is to print the coder
print("\n","\t"*4,"Created","\n","\t"*3,"\\"*25, "\n","\t"*4,"   By","\n","\t"*4,"Zenoftech\n", "\t"*3,"\\"*25)

# Here are the instructions the user to follow
print("""
    Use the arithemetic signs below for your calculation:
    +   For addition
    -   For subtraction
    *   For multiplication
    /   For division
    //  For integer (division without decimal point value)
    %   For Modulus

    """)


# this variable will accept the user input
Number = eval(input("Enter the numbers you want to calculate: "))

# Here we print the result of the operation
print("\n\t","*"*4, "The result is: ", Number ,"*"*4, "\n\t")
# The input below is to keep the program waiting after evaluating the user input and printing the result.
input("Press the enter key to exit... ")

