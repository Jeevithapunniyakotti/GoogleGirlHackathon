import random

ops = ["&", "|", "^", "~"]
variables = ["A", "B", "C", "D", "E"]

def generate_expression():
    """Generates a random combinational logic expression."""
    expr = f"({random.choice(variables)} {random.choice(ops)} {random.choice(variables)})"
    if random.random() > 0.5:
        expr = f"({expr} {random.choice(ops)} {random.choice(variables)})"
    return expr

if __name__ == "__main__":
    for _ in range(5):
        print(generate_expression())
