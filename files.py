import csv
import os

# Stores the last used file path — None until a file is saved or loaded
path = None


def save_csv(inventary, archivo="database.csv"):
    """
    Export the current inventory to a CSV file.

    If the file already exists, asks the user whether to overwrite it.
    Skips saving if the user declines or enters an invalid response.

    Args:
        inventary (list): List of product dictionaries to save.
        archivo (str): Output file path. Defaults to 'database.csv'.
    """
    # Warn the user if the file already exists
    if os.path.exists(archivo):
        overwrite = input(f" '{archivo}' already exists. Overwrite it? (yes/no): ").strip().lower()

        # Validate confirmation — only accept 'yes' or 'no'
        if overwrite not in ("yes", "no"):
            print(" Please type 'yes' or 'no'. Save cancelled.")
            return
        if overwrite == "no":
            print(" Save cancelled. Existing file was not modified.\n")
            return

    with open(archivo, "w", newline="") as csvfile:
        fieldnames = ["name", "price", "quantity"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader() # Write the column names as the first row
        for product in inventary:
            writer.writerow(product) # Write each product as a CSV row

    print(f" Inventory saved to: {archivo}\n")
