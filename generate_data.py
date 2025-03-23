# generate_data.py
import json
import random

# Example data generation: list of random numbers
data = {"values": [random.randint(1, 100) for _ in range(10)]}

with open("data/output.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data generated and saved to data/output.json")
