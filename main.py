from model import predict_complexity

# Example signal inputs (Modify based on your dataset)
signals = ["A & B", "A | B", "(A & B) | (C & D)"]

# Predict complexity
for signal in signals:
    complexity = predict_complexity(signal)
    print(f"Signal: {signal} → Complexity: {complexity}")
