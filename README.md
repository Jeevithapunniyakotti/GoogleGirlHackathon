# GoogleGirlHackathon
Combinational Complexity Predictor

Overview
This project predicts the combinational complexity/depth of Boolean expressions to help identify timing violations in digital circuits.

Installation
1. Clone this repository:
git clone https://github.com/your-username/GoogleGirlHackathon.git
cd GoogleGirlHackathon

2. Run tests to verify functionality:
python testmodel.py

Usage
Use the predict_complexity() function to analyze Boolean expressions:
from model import predict_complexity
expression = "(A & B) | C"
complexity = predict_complexity(expression)
print(f"Predicted Complexity: {complexity}")

Project Structure
GoogleGirlHackathon
 ├── model.py         # Main logic for complexity prediction
 ├── testmodel.py     # Unit tests for the model
 ├── README.md        # Project documentation

 Acknowledgements
 Developed as part of the Google Girl Hackathon 2025
