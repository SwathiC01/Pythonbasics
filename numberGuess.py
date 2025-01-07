from random import randint

l_range, u_range = 1,10
random_num=randint(l_range,u_range)
guesses=0
while True:
    if guesses>2:
        print("Couldn't guess the number")
        break
    try:
        user_guess = int(input("Enter a number: "))
    except ValueError as e:
        print("Invalid number. Enter a valid number")
        continue

    if user_guess>random_num:
        print(f"Guess the number less than {user_guess}")
        guesses+=1
    elif user_guess<random_num:
        print(f"Guess the number greater than {user_guess}")
        guesses+=1
    else:
        print("You guessed the number!!")
        break