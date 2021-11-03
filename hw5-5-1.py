# Ryan Lugo: RJL 11/2/21

the_string = str(input("What word do you want to be split in half?:" ))
string_halfed = len(the_string) // 2

print("First half of the string", the_string[0:string_halfed])
print("Second half of the string", the_string[string_halfed:len(the_string)])