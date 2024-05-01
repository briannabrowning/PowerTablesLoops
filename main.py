number = int(input("Enter an integer: "))
print("Number  Squared  Cubed")
print("======= =======  ======")
for i in range(1, number + 1):
    square = i ** 2
    cube = i ** 3
    print(f"{i:<7}  {square:<7}  {cube}")

while True:
    another_numb = input("Would you like to enter another number? y/n ")
    if another_numb == "y":
        number = int((input("Please enter another integer: ")))
        print("Number  Squared  Cubed")
        print("======= =======  ======")
        for i in range(1, number + 1):
            square = i ** 2
            cube = i ** 3
            print(f"{i:<7}  {square:<7}  {cube}")
    elif another_numb == "n":
        break