# generate_data.py
import json
import random
import os

# Ensure data directory exists
os.makedirs("data", exist_ok=True)

# Example data generation: list of random numbers with labels
data = {
    "results": [
        {"label": f"Item {i+1}", "value": random.randint(1, 100)} for i in range(10)
    ]
}

with open("data/output.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data generated and saved to data/output.json")
