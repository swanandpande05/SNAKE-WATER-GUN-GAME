import random


def determine_winner(user_choice, computer_choice):
    """
    Determine the winner of the Snake-Water-Gun game.

    Returns:
        True  -> User wins
        False -> Computer wins
        None  -> Draw
    """

    if user_choice == computer_choice:
        return None

    winning_combinations = {
        ("s", "w"),  # Snake beats Water
        ("w", "g"),  # Water beats Gun
        ("g", "s")   # Gun beats Snake
    }

    return (user_choice, computer_choice) in winning_combinations


def main():
    choices = {
        "s": "Snake",
        "w": "Water",
        "g": "Gun"
    }

    print("=" * 40)
    print("       SNAKE - WATER - GUN")
    print("=" * 40)

    print("\nChoose one:")
    print("s - Snake")
    print("w - Water")
    print("g - Gun")

    # Get and validate user's choice
    while True:
        user_choice = input("\nYour choice: ").strip().lower()

        if user_choice in choices:
            break

        print("Invalid choice! Please enter s, w, or g.")

    # Computer randomly selects a choice
    computer_choice = random.choice(list(choices.keys()))

    # Determine the result
    result = determine_winner(user_choice, computer_choice)

    # Display results
    print("\n" + "-" * 40)
    print(f"You chose      : {choices[user_choice]}")
    print(f"Computer chose : {choices[computer_choice]}")
    print("-" * 40)

    if result is None:
        print("Result         : It's a Draw!")
    elif result:
        print("Result         : You Win! 🎉")
    else:
        print("Result         : You Lost! 💻")

    print("=" * 40)


if __name__ == "__main__":
    main()