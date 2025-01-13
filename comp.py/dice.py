import random
from collections import Counter

def simulate_dice_rolls(trials, target=None):
    """
    Simulate dice rolls and estimate probabilities.
    
    Parameters:
    trials (int): Number of dice rolls to simulate.
    target (int, list, or None): Target face(s) to analyze (1 to 6).
                                If None, calculates probabilities for all faces.
    
    Returns:
    dict: Estimated probabilities for the specified target(s).
    """
    if target is not None:
        if isinstance(target, int):
            target = [target]  # Convert single integer to list
        if not all(1 <= t <= 6 for t in target):
            raise ValueError("Target faces must be between 1 and 6.")
    
    # Simulate dice rolls
    rolls = [random.randint(1, 6) for _ in range(trials)]
    counts = Counter(rolls)
    
    # Calculate probabilities
    if target is None:
        # Calculate probabilities for all faces
        probabilities = {face: counts[face] / trials for face in range(1, 7)}
    else:
        # Calculate probabilities for the specified target(s)
        probabilities = {t: counts[t] / trials for t in target}
    
    return probabilities

# Example Usage:
trials = 10000

# Simulate and display results for a single face
result_single = simulate_dice_rolls(trials, target=3)
print(f"Simulated Probability for face 3: {result_single[3]:.4f}")

# Simulate and display results for multiple faces
result_multiple = simulate_dice_rolls(trials, target=[2, 5])
print("Simulated Probabilities for faces 2 and 5:")
for face, prob in result_multiple.items():
    print(f"  Face {face}: {prob:.4f}")

# Simulate and display results for all faces
result_all = simulate_dice_rolls(trials)
print("Simulated Probabilities for all faces:")
for face, prob in result_all.items():
    print(f"  Face {face}: {prob:.4f}")
