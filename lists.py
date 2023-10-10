# part1 Change a List

numbers = [1, 2, 3, 4, 5, 99, 2600, 300]

reversed_list = list(
    reversed(numbers)
)  # reversed does not make a list, but also does not mutate original list

print(numbers)
print(reversed_list)


# part2 String to List

my_string = "abcdEFGHijkLmNOP"
my_list = []

for letter in my_string:
    my_list.append(letter)

reversed_my_list = my_list.reverse()

print(my_list)

new_string = ""

new_string = "".join(my_list)

print(new_string)


# part 3 List + Conditional

dunder_list = ["michael", "jim", "pam", "dwight", "kevin", "creed", "andy", "angela"]
user_entry = input("Pick a name from The Office: ")

if user_entry in dunder_list:
    print("Exists")
    dunder_list.remove(user_entry)
    print(dunder_list)
else:
    dunder_list.append(user_entry)
    print(dunder_list)
