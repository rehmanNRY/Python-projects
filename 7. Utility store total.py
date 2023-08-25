sum = 0
while(True):
    item = input("Enter item price or q to exit: ")
    if item != "q":
        sum = sum + int(item)
        print(f"Total now = {sum}")
    else:
        print(f"Your total is {sum}, Good Bye come soon")
        break