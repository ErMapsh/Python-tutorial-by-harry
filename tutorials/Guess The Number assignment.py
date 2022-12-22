#guess the number

import numpy as np
no = np.random.randint(100)
print("Guess No:",no)

guess_no = 10;#total guesses are 10 -1 = 9
try:
    for i in range(1, guess_no+1):
        user_input = int(input("Enter The No:"))
        if user_input == no:
            print("Guess no is correct");
            break
        elif user_input > no:
            print("Your Number is greater than Guess no...")
            print(f"You have left guesses: {guess_no - i}")
            print()
            continue
        elif user_input < no:
            print("Your Number is less than Guess no")
            print(f"You have left guesses: {guess_no - i}")
            print()
            continue
    else:
        print("---You Lose---")


except Exception as e:
    print(e)





