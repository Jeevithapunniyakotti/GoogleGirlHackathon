import re

def predict_complexity(signal_expression):
    """
      to estimate the combinational complexity of a signal.
    - Counts the number of logic gates/operators in the expression.
    """
    operations = ["&", "|", "^", "~"]  # AND, OR, XOR, NOT
    count = sum(signal_expression.count(op) for op in operations)
    
    # Adjust complexity based on parentheses depth
    depth = signal_expression.count("(")
    
    return count + depth

if __name__ == "__main__":
    test_signal = "(A & B) | (C & D)"
    print(f"Predicted Complexity: {predict_complexity(test_signal)}")
