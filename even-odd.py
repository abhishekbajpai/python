# Ask the user for a number. 
# Depending on whether the number is even or odd, 
# print out an appropriate message to the user. 

numb = int(input("Please enter a number to check if even or odd: "))
if numb%2 == 0:
    print("Entered number is even. ")
else:
    print("You have enetered odd number")