# part 1 Start/End

start_num = int(input("Enter positive starting number: "))
end_num = int(input("Enter a positive ending number: "))

# ORIGINAL ANSWER
# while start_num <= end_num:
#     print(start_num)
#     start_num += 1

# part 1 bonus

while start_num <= end_num:
    if start_num < 1 or start_num > 50 or end_num > 50 or end_num < 1:
        print("Pick a number 1-50")
        start_num = int(input("Enter positive starting number: "))
        end_num = int(input("Enter a positive ending number: "))
    else:
        print(start_num)
        start_num += 5


# part 2 Multi-Condition Check

sample = "The quick brown fox jumped over the lazy dog"
counter = 0

while counter < len(sample):
    if counter % 2 == 0 and sample[counter] != " ":
        print(sample[counter])
    counter += 1
