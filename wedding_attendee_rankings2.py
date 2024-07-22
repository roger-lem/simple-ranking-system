import numpy as np
import random

# List of items to be ranked
items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

# Initialize comparison matrix
num_items = len(items)
comparison_matrix = np.zeros((num_items, num_items), dtype=int)

# Function to get random pair of items for comparison
def get_random_pair():
    i, j = random.sample(range(num_items), 2)
    return i, j

# Simulate pairwise comparisons
number_of_comparisons_needed = 10  # Replace with your desired number of comparisons
print("Please choose between the following pairs:")

for _ in range(number_of_comparisons_needed):
    i, j = get_random_pair()
    print(f"{items[i]} or {items[j]}?")
    while True:
        try:
            choice = int(input(f"Enter your choice (1 or 2): "))
            if choice == 1:
                comparison_matrix[i][j] += 1
                break
            elif choice == 2:
                comparison_matrix[j][i] += 1
                break
            else:
                print("Invalid choice. Please enter 1 or 2.")
        except ValueError:
            print("Invalid input. Please enter 1 or 2.")

# Aggregate ranks using Rank Centrality method
rank_scores = np.sum(comparison_matrix, axis=1)

# Sort items based on rank scores
ranked_items_indices = np.argsort(rank_scores)[::-1]

# Generate ranked list
ranked_items = [items[i] for i in ranked_items_indices]

# Output the ranked list
print("\nRanked List of Items:")
for rank, item in enumerate(ranked_items, start=1):
    print(f"{rank}. {item}")
