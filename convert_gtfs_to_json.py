import csv
import json
import os

def convert_gtfs_to_json(input_dir='gtfs_data', output_dir='gtfs_data_json'):
    os.makedirs(output_dir, exist_ok=True)

    for txt_file in [f for f in os.listdir(input_dir) if f.endswith('.txt')]:
        input_path = os.path.join(input_dir, txt_file)
        output_path = os.path.join(output_dir, txt_file.replace('.txt', '.json'))

        try:
            with open(input_path, 'r', encoding='utf-8-sig') as csvfile:  # Use utf-8-sig
                reader = csv.DictReader(csvfile)
                data = list(reader)

            with open(output_path, 'w', encoding='utf-8') as jsonfile:
                json.dump(data, jsonfile, indent=2, ensure_ascii=False)

            print(f"Converted {txt_file} to JSON format")

        except Exception as e:
            print(f"Error converting {txt_file}: {e}")

if __name__ == "__main__":
    convert_gtfs_to_json()