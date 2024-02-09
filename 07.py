import random


def roll_dice():
    return random.randint(1, 6)


def simulate_dice_rolls(num_rolls):
    outcomes = [0] * 11
    for _ in range(num_rolls):
        roll_sum = roll_dice() + roll_dice()
        outcomes[roll_sum-2] += 1
    probabilities = [outcome / num_rolls for outcome in outcomes]
    return probabilities


def print_probabilities(probabilities):
    print(f"{'| Sum of rolls': <13} | {'Probability'}")
    print(f"| {'-'*12} | {'-'*12}")
    for i, prob in enumerate(probabilities, start=2):
        print(f"| { i: ^12} | {prob:.6f}")


if __name__ == "__main__":
    num_rolls = 1000000
    probabilities = simulate_dice_rolls(num_rolls)
    print_probabilities(probabilities)
