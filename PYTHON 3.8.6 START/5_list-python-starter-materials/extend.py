# my_list = [2,1, 4, 3]
# max_elem = my_list[0]
# for elem in my_list:
#     if elem > max_elem:
#         max_elem = elem
# print(max_elem)

# number = 0
# str_ = "Enter a positive integer: "
# while number >= 0:
#     number = int(input(str_))
#     print("You have entered", number)
#
# response = ""
# while response != "exit":
#     response = input()
# for number in range(1, 11):
#     if number % 2 != 0:
#         continue
#     print("Current number is", number)
# for i in range(10):
#     print(i)

for row in range(5):
    char = "*"
    for column in range(4):
        char += " *"
    print(char)
