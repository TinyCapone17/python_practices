import os
import csv
import json


def csv_to_json(csv_file, json_file):
    # Check if the input CSV file exists
    if not os.path.exists(csv_file):
        print(f"Error: {csv_file} not found")
        return

    # Open the CSV file for reading
    with open(csv_file, "r") as f:
        # Read the CSV data into a list of dictionaries
        data = []
        reader = csv.DictReader(f)
        for row in reader:
            # Infer the correct data types for each value
            row = {k: infer_type(v) for k, v in row.items()}
            data.append(row)

    # Check if the file is empty
    if not data:
        print("Error: input file is empty")
        data = []

    # Open the JSON file for writing
    with open(json_file, "w") as f:
        # Write the JSON data in pretty format
        json.dump(data, f, indent=4)


def infer_type(value):
    """Infer the correct data type for a value"""
    try:
        return int(value)
    except ValueError:
        try:
            return float(value)
        except ValueError:
            return value if value != "" else None


def test_csv_to_json():
    # Test with a valid input file
    csv_to_json("input.csv", "output1.json")
    expected_output = """[
    {
        "id": 1,
        "name": "Ivan",
        "birth": 1980,
        "salary": 150000,
        "department": 1
    },
    {
        "id": 2,
        "name": "Alex",
        "birth": 1960,
        "salary": 200000,
        "department": 5
    },
    {
        "id": 3,
        "name": "Ivan",
        "birth": null,
        "salary": 130000,
        "department": 8
    }
]"""
    with open("output1.json") as f:
        assert f.read() == expected_output

    # Test with a file that does not exist
    assert csv_to_json("invalid.csv", "output.json") is None

    # Test with an empty input file
    csv_to_json("empty.csv", "output2.json")
    with open("output.json") as f:
        assert f.read() == "[]"
