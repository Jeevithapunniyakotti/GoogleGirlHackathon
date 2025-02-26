from model import predict_complexity

def test_complexity():
    assert predict_complexity("A & B") == 1
    assert predict_complexity("(A & B) | C") == 2
    assert predict_complexity("~A & (B | C)") == 3
    print("✅ All tests passed!")

if __name__ == "__main__":
    test_complexity()
