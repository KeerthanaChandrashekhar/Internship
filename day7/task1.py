name = input("Enter your name: ")
daily_goal = input("Enter your daily goal: ")

with open("journal.txt", "a") as file:
    file.write(f"Name: {name}, Daily Goal: {daily_goal}\n")
    