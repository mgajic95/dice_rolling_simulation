import random

def roll_dice(sides=6):
    return random.randint(1, sides)

def roll_multiple_dice(num_dice, sides=6):
    return [roll_dice(sides) for _ in range(num_dice)]

def main():
    print("Welcome to the Advanced Dice Rolling Simulator!")

    total_score = 0

    while True:
        try:
            num_dice = int(input("Enter the number of dice to roll: "))
            sides = int(input("Enter the number of sides for each dice: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        rolls = roll_multiple_dice(num_dice, sides)
        total = sum(rolls)

        print(f"You rolled: {', '.join(map(str, rolls))}")
        print(f"Total: {total}")

        total_score += total
        print(f"Total Score: {total_score}")

        play_again = input("Do you want to roll again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

    print(f"Thanks for using the Dice Rolling Simulator! Your Final score is: {total_score}")

if __name__ == "__main__":
    main()
