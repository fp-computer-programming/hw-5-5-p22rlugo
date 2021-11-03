# Ryan Lugo: RJL 11/2/21

string_entered = str(input("Enter a string that might be Palindromed: "))

if string_entered[::-1] == string_entered:
    print("The word is a palindrome")
else:
     print("The word is not a palindrome")