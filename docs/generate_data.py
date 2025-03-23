# generate_data.py
import json
import random
import os

# Ensure root directory (for GitHub Action output) exists
os.makedirs("docs", exist_ok=True)

# Generate example data with random values
data = {
    "results": [
        {"label": f"Item {i+1}", "value": random.randint(1, 100)} for i in range(10)
    ]
}

with open("docs/output.json", "w") as f:
    json.dump(data, f, indent=4)

print("Data generated and saved to docs/output.json")
