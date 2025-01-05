import random

def simulate_dice_rolls(trials, target):
    """
    Simulate dice rolls and estimate the probability of a target outcome.
    trials: number of rolls
    target: target face (1 to 6)
    """
    success = 0
    for _ in range(trials):
        roll = random.randint(1, 6)
        if roll == target:
            success += 1
    return success / trials

# Simulate 10000 dice rolls and estimate the probability of rolling a 3
print(f"Simulated Probability: {simulate_dice_rolls(10000, 3):.4f}")
