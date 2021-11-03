# Ryan Lugo: RJL 11/2/21

first_string = str(input("First string?: "))
second_string = str(input("Second string?: "))
third_string = str(input("Third string?: "))

first = list(first_string)
print(sorted(first,key=str.lower))

second = list(second_string)
print(sorted(second,key=str.lower))

third = list(third_string)
print(sorted(third,key=str.lower))