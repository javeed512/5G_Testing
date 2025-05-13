
import pandas as pd

def json_to_csv(json_filepath, csv_filepath):
    """
    Converts a JSON file to a CSV file.

    Args:
        json_filepath (str): The path to the input JSON file.
        csv_filepath (str): The path to the output CSV file.
    """
    try:
        df = pd.read_json(json_filepath)
        df.to_csv(csv_filepath, index=False, encoding='utf-8')
        print(f"Successfully converted '{json_filepath}' to '{csv_filepath}'")
    except FileNotFoundError:
         print(f"Error: JSON file '{json_filepath}' not found.")
    except ValueError:
        print(f"Error: Invalid JSON format in '{json_filepath}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    json_file_path = "input.json"
    csv_file_path = "output.csv"
    json_to_csv(json_file_path, csv_file_path)