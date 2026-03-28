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

def load_csv(inventary, archivo="database.csv"):
    """
    Import products from a CSV file into the inventory.

    Reads the file line by line, skipping the header and any empty lines.
    Each valid row is parsed into a product dictionary and added to the
    inventory only if it doesn't already exist (duplicate check on all three fields).

    Args:
        inventary (list): The inventory list to load products into.
        archivo (str): Path to the CSV file to read. Defaults to 'database.csv'.

    Raises:
        FileNotFoundError: Caught internally — notifies user if file doesn't exist.
        Exception: Caught internally — handles any unexpected parsing errors.
    """
    try:
        with open(archivo, "r", encoding="utf-8") as file:
            next(file) # Skip the header line (name, price, quantity)

            for line in file:
                line = line.strip()
                if not line: # Skip blank lines between rows
                    continue

                # Unpack the three expected CSV columns
                name, price, quantity = line.split(",")
                price = float(price)
                quantity = int(quantity)

                # Check if this exact product already exists in the inventory
                exists = False
                for product in inventary:
                    if (product["name"] == name and
                        product["price"] == price and
                        product["quantity"] == quantity):
                        exists = True
                        break # No need to keep checking once a match is found

                # Only append if no duplicate was found
                if not exists:
                    inventary.append({
                        "name": name,
                        "price": price,
                        "quantity": quantity
                    })

        print(f" Inventory loaded from: {archivo}\n")

    except FileNotFoundError:
        # Expected on first run — no CSV exists yet
        print(f" No file found at '{archivo}', starting with empty inventory.\n")

    except Exception as e:
        # Catches malformed rows, wrong column count, bad type conversions, etc.
        print(f" Error loading CSV: {e}\n")
