strng = "aabcbaa"
palindromeBool = True

# One of the approach is to fix to loop the string and check each character
# stringBreak = len(strng)/2;
# for i in range(0, int(stringBreak)):
#     if(strng[i] != strng[(stringLength-1)- i]):
#         palindromeBool = False
# if(palindromeBool):
#     print("Given string is palindrome")
# else: 
#     print("Given string is not a palindrome")


# Approach 2: use reverse function to check if both side of string is same  
strngReverse = strng[::-1];
if(strng  == strngReverse):
    print("Given string is palindrome")
else:
    print("Given string is not palindrome")
