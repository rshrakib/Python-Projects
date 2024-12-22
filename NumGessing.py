import random
def num():
    print("Welcome to Number guessing game!!")
    target_num = random.randint(1,100)
    try:
            user_guess = int(input("Enter you Number (1-100): "))
            if user_guess == target_num:
                print(f"You are correct!!!")
            # elif user_guess < target_num:
            #     print("The guess is smaller than original number.")
            # elif user_guess > target_num:
            #     print("The guess is greater than the original number.")
            else:
                print(f"OPPs!!! The number is {target_num}")
    except ValueError:
        print("Error: Please give the correct input.")
        num()

while True:
    num()
