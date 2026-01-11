import csv
import os
from collections import defaultdict
import re

tp1 = dict[str, list]

def split_csv(input_file: str, key: str) -> tp1:
    group = defaultdict(list)
    with open(input_file, 'r', newline='', encoding='utf-8') as f:
        global reader
        reader = csv.DictReader(f)
        if key not in reader.fieldnames:
            raise ValueError(f"The CSV file does not have a '{key}' column.")

        for row in reader:
            group[row[key]].append(row)

    return group

def save_csv(file: tp1, output_dir=None) -> None:
    output_dir = f"{os.getcwd()}\\split" if output_dir is None else output_dir
    os.makedirs(output_dir)

    for key, rows in file.items():
        file_name = re.match(r"\[\d+\]", key).group()[1:-1]

        output_file = os.path.join(output_dir, f"{file_name}.csv")

        with open(output_file, 'w', newline='', encoding='utf-8') as f:
            if rows:
                writer = csv.DictWriter(f, fieldnames=reader.fieldnames)
                writer.writeheader()
                writer.writerows(rows)

        print(f"Created file: {output_file} with {len(rows)} rows")
    print("CSV save completed successfully.")

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="This is a program that split csv file, usage: python split_csv.py <input_csv_file> [output_directory]")
    parser.add_argument("input_file", help="path of input csv file")
    parser.add_argument("output_file", help="path of input csv file", nargs='?', default=None)
    args = parser.parse_args()

    save_csv(split_csv(input_file=args.input_file, key="CITATION"), output_dir=args.output_file)
