import random

# 1) Independent Events

trials = 10000
count_heads_and_6 = 0

for _ in range(trials):
    coin = random.choice(["H", "T"])
    die = random.randint(1, 6)

    if coin == "H" and die == 6:
        count_heads_and_6 += 1

prob_heads_and_6 = count_heads_and_6 / trials

print("Independent Events:")
print("P(Heads and 6) ≈", prob_heads_and_6)
print("Theoretical value =", 1/12)
print()


# 2) Dependent Events

count_two_reds = 0

for _ in range(trials):
    bag = ["R"] * 5 + ["B"] * 5   # 5 Red, 5 Blue
    first = random.choice(bag)
    bag.remove(first)           # remove it (no replacement)
    second = random.choice(bag)

    if first == "R" and second == "R":
        count_two_reds += 1

prob_two_reds = count_two_reds / trials

print("Dependent Events:")
print("P(Two Reds) ≈", prob_two_reds)
print("Theoretical value =", 2/9)
