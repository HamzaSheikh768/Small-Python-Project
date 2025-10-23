# def table(n):
#     for i in range(1, 13):
#         print(f"{n} x {i} = {n * i}")
# table(5)    #Method 1

# def table(n):
#     for i in range(1, 13):
#         result = n *i
#         print(f"{n} x {i} = {result}")
# table(5)   #Method 2


# def table(n):
#     for i in range(1, 13):
#         result = n *i
#         print(f"{n} x {i} = {result}")

# num1 = input ("Enter a number: ")
# table(num1)  # Method 1


def table(n):
    for i in range(1, 13):
        result = n * i
        print(f"{n} x {i} = {result}")

def user_input():
    while True:
        num1 = input("Enter a number: ")
        if num1.isdigit():
            return int(num1)
        else:
            print("Please enter a valid number.")

num1 = user_input()
table(num1)              