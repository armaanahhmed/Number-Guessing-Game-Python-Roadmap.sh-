import random
import os
import time

guesses = 0
difficulty = ""
run1 = True
run2 = True
attempts = 0
prev_attempts = [9999]

def diffE():
    global guesses, difficulty
    difficulty = "easy"
    guesses = 10
    print("\nGreat! You have selected the Easy difficulty level.")

def diffM():
    global guesses, difficulty
    difficulty = "medium"
    guesses = 5
    print("\nGreat! You have selected the Medium difficulty level.")

def diffH():
    global guesses, difficulty
    difficulty = "hard"
    guesses = 3
    print("\nGreat! You have selected the Hard difficulty level.")

def play_game():
    global run1, run2, difficulty, guesses, attempts
    difficulty = ""
    guesses = 0 
    attempts = 0
    run1 = run2 = True

    time.sleep(1)
    print("Welcome to the Number Guessing Game!")
    x = random.randint(1, 100)
    time.sleep(1)
    print("I'm thinking of a number between 1 and 100.")
    time.sleep(1)
    print("You will get a different number of chances depending on difficulty.")
    print(" ")
    time.sleep(1)
    print("""Please select the difficulty level: 
            1. Easy (10 chances)
            2. Medium (5 chances)
            3. Hard (3 chances)
        """)
    
    while run1:
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                diffE()
                run1 = False
            elif choice == 2:
                diffM()
                run1 = False
            elif choice == 3:
                diffH()
                run1 = False
            else: 
                time.sleep(1)
                print("Enter A Valid Choice!")
        except ValueError:
            print("Invalid Choice!")
            time.sleep(1)
    
    print("Let's start the game!")
    time.sleep(1)
    start = time.time()
    print(" ") 
    while run2:
        print(" ")

        try:  
            time.sleep(1)
            guess = int(input("Enter Your Guess: "))
            attempts += 1
            
            if guess > x:
                time.sleep(1)
                print(f"Incorrect! The number is less than {guess}.")
                guesses -= 1
            elif guess < x:
                time.sleep(1)
                print(f"Incorrect! The number is greater than {guess}.")
                guesses -= 1
        
            if guess == x:
                if difficulty == "easy":
                    attempts = 10 - guesses
                elif difficulty == "medium":
                    attempts = 5 - guesses
                elif difficulty == "hard":
                    attempts = 3 - guesses

                if attempts < prev_attempts[0]:
                    prev_attempts[0] = attempts
                    print(f"New High Score : {attempts} Attempts!")
                
                end = time.time()
                rounded_len = round(end - start, 2)
                print(f"It Took You {rounded_len} seconds!")
                time.sleep(1)
                print(f"Congratulations! You've guessed the correct number in {attempts} attempts.")
                run2 = run1 = False

            if guesses == 0 and guess != x:
                print(f"You ran out of guesses! The number was {x}.")
                end = time.time()
                result = round(end - start, 2)
                print(f"It Took You {result} seconds!")
                run1 = run2 = False

            if guess != x:
                if difficulty == "easy" and guesses < 5:
                    low = max(1, x-10)
                    high = min(100, x+10)
                    print(f"Hint: It's between {low} and {high}.")
                elif difficulty == "medium" and guesses < 3:
                    low = max(1, x-10)
                    high = min(100, x+10)
                    print(f"Hint: It's between {low} and {high}.")
                elif difficulty == "hard" and guesses < 2:
                    low = max(1, x-10)
                    high = min(100, x+10)
                    print(f"Hint: It's between {low} and {high}.")
                     
        except ValueError:
            time.sleep(1)
            print("Invalid Integer!")

while True:
    play_game()
    try:
        time.sleep(1)
        again = int(input("Do You Want To Play Again?(Y=1/N=0): "))
        if again == 1:
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue
        elif again == 0:
            time.sleep(1)
            print("Thanks For Playing!")
            break
        else:
            time.sleep(1)
            print("Choose Either 1(Yes) or 0(No).")
    except:
        time.sleep(1)
        print("Invalid Input.")
