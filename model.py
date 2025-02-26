import re

def predict_complexity(expression: str) -> int:
    # Remove spaces for consistency
    expression = expression.replace(" ", "")

    # Define the logical operators
    operators = {"&": 1, "|": 1, "^": 1, "~": 1}

    # Count the number of operators in the expression
    complexity = sum(expression.count(op) for op in operators)

    return complexity
