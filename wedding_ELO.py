import numpy as np
import pandas as pd
import random

# List of items to be ranked
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]
items = pd.read_csv('attendee sample.csv', header=None).values.tolist()[0]
num_items = len(items)

# Initialize Elo ratings for each item
elo_ratings = np.zeros(num_items, dtype=float)
K = 32  # Elo rating update parameter (adjust as needed)

# Function to get random pair of items for comparison
def get_random_pair():
    i, j = random.sample(range(num_items), 2)
    return i, j

def get_random_item():




# Function to calculate expected probability
def expected_probability(rating1, rating2):
    return 1 / (1 + 10 ** ((rating2 - rating1) / 400))


# Simulate pairwise comparisons
number_of_comparisons_needed = 3  # Replace with your desired number of comparisons
minumum_reps_per_entrant = 2

comparison_count_by_entrant = elo_ratings * 0
print("Please choose between the following pairs:")
# initial round robin
for _ in range(number_of_comparisons_needed):
    i, j = get_random_pair()
    comparison_count_by_entrant[i] += 1
    comparison_count_by_entrant[j] += 1
    print(f"{items[i]} or {items[j]}?")
    while True:
        try:
            choice = int(input(f"Enter your choice (1 or 2): "))
            if choice == 1:
                winner, loser = i, j
                break
            elif choice == 2:
                winner, loser = j, i
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")

    # Update Elo ratings
    expected_win = expected_probability(elo_ratings[loser], elo_ratings[winner])
    expected_loss = expected_probability(elo_ratings[winner], elo_ratings[loser])
    elo_ratings[winner] += K * (1 - expected_win)
    elo_ratings[loser] += K * (0 - expected_loss)

# giving everyone their min reps

for entrant_index, entrant_bout_count in enumerate(comparison_count_by_entrant):
    if entrant_bout_count < minumum_reps_per_entrant:
        i, j = get_random_pair()
        i = entrant_index
        print(f"{items[i]} or {items[j]}?")
        while True:
            try:
                choice = int(input(f"Enter your choice (1 or 2): "))
                if choice == 1:
                    winner, loser = i, j
                    break
                elif choice == 2:
                    winner, loser = j, i
                    break
                else:
                    print("Invalid choice. Please enter 1 or 2.")
            except ValueError:
                print("Invalid input. Please enter 1 or 2.")

        # Update Elo ratings
        expected_win = expected_probability(elo_ratings[loser], elo_ratings[winner])
        expected_loss = expected_probability(elo_ratings[winner], elo_ratings[loser])
        elo_ratings[winner] += K * (1 - expected_win)
        elo_ratings[loser] += K * (0 - expected_loss)

# Sort items based on Elo ratings
ranked_items_indices = np.argsort(elo_ratings)[::-1]

# Generate ranked list
ranked_items = [items[i] for i in ranked_items_indices]

# Output the ranked list
print("\nRanked List of Items:")
for rank, item in enumerate(ranked_items, start=1):
    print(f"{rank}. {item} (Elo Rating: {elo_ratings[items.index(item)]:.2f})")
