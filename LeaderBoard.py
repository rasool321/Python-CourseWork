import random

# Initialize the leaderboard with random scores
leaderboard = [random.randint(100, 500) for _ in range(5)]

# Game loop
while True:
    print("\n--- Game Leaderboard Management ---")
    print("1. Add a New Score")
    print("2. Remove a Score")
    print("3. Sort Leaderboard (High to Low)")
    print("4. Sort Leaderboard (Low to High)")
    print("5. Reverse Leaderboard")
    print("6. Find Player Rank")
    print("7. Show Highest & Lowest Score")
    print("8. Count a Score")
    print("9. Clear Leaderboard")
    print("10. Exit")

    choice = input("Enter your choice (1-10): ")

    # 1. Add a score
    if choice == "1":
        score = int(input("Enter new score: "))
        leaderboard.append(score)
        print("Score added.")

    # 2. Remove a score
    elif choice == "2":
        score = int(input("Enter score to remove: "))
        if score in leaderboard:
            leaderboard.remove(score)
            print("Score removed.")
        else:
            print("Score not found.")

    # 3. Sort High to Low
    elif choice == "3":
        leaderboard.sort(reverse=True)
        print("Leaderboard sorted (high to low).")

    # 4. Sort Low to High
    elif choice == "4":
        leaderboard.sort()
        print("Leaderboard sorted (low to high).")

    # 5. Reverse order
    elif choice == "5":
        leaderboard.reverse()
        print("Leaderboard order reversed.")

    # 6. Find rank
    elif choice == "6":
        score = int(input("Enter score to find rank: "))
        sorted_board = sorted(leaderboard, reverse=True)
        if score in sorted_board:
            rank = sorted_board.index(score) + 1
            print(f"Score {score} is ranked #{rank}.")
        else:
            print("Score not found.")

    # 7. Show highest and lowest
    elif choice == "7":
        if leaderboard:
            print("Highest score:", max(leaderboard))
            print("Lowest score:", min(leaderboard))
        else:
            print("Leaderboard is empty.")

    # 8. Count a score
    elif choice == "8":
        score = int(input("Enter score to count: "))
        count = leaderboard.count(score)
        print(f"Score {score} appears {count} times.")

    # 9. Clear leaderboard
    elif choice == "9":
        leaderboard.clear()
        print("Leaderboard cleared.")

    # 10. Exit
    elif choice == "10":
        print("Exiting program.")
        break

    else:
        print("Invalid choice, try again.")