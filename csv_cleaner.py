import csv
import sys


def clean_csv(input_file, output_file):
    with open(input_file, "r", encoding="utf-8-sig", newline="") as infile:
        reader = csv.DictReader(infile)

        if not reader.fieldnames:
            raise ValueError("CSV file has no header.")

        rows = []
        seen = set()

        for row in reader:
            # Skip completely empty rows
            if not any(str(value).strip() for value in row.values()):
                continue

            # Remove duplicate rows
            row_key = tuple(str(row.get(field, "")).strip() for field in reader.fieldnames)

            if row_key in seen:
                continue

            seen.add(row_key)
            rows.append(row)

    with open(output_file, "w", encoding="utf-8", newline="") as outfile:
        writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    print(f"Cleaned report saved to: {output_file}")
    print(f"Original/processed records: {len(rows)}")


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python csv_cleaner.py input.csv output.csv")
        sys.exit(1)

    clean_csv(sys.argv[1], sys.argv[2])
