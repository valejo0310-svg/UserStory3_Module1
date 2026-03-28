inventary = []


def add_products():
    """
    Prompt the user to add one or more products to the inventory.

    Each product requires a name (str), price (float > 0), and quantity (int >= 0).
    The function loops until the user types 'no' when asked to continue.
    Invalid inputs (non-numeric, negative, or empty values) are caught and re-prompted.
    """
    continuar = "yes"

    while continuar != "no":
        print("=" * 60)

        # Validate name — cannot be empty or contain numbers
        product_name = input("\nEnter the product name: ").strip()
        if not product_name:
            print(" Name cannot be empty.")
            continue
        if any(char.isdigit() for char in product_name):
            print(" Name cannot contain numbers.")
            continue

        # Validate price — must be a positive number
        try:
            product_price = float(input("Enter the product price: "))
            if product_price < 0:
                print(" Price cannot be negative.")
                continue
        except ValueError:
            print(" Please enter a valid number for the price.")
            continue

        # Validate quantity — must be a non-negative integer
        try:
            producto_quantity = int(input("Enter the product quantity: "))
            if producto_quantity < 0:
                print(" Quantity cannot be negative.")
                continue
        except ValueError:
            print(" Please enter a whole number for the quantity.")
            continue

        # Build a dictionary with the product's data and add it to the list
        products = {
            "name": product_name,
            "price": product_price,
            "quantity": producto_quantity
        }
        inventary.append(products)
        print(f" Product '{product_name}' added successfully!")

        continuar = input("\nDo you want to add another product? (yes/no): ").strip().lower()
        if continuar not in ("yes", "no"):
            print(" Please type 'yes' or 'no'. Returning to menu.")
            continuar = "no"


def show_inventary():
    """
    Print all products currently stored in the inventory.

    If the inventory is empty, notifies the user and returns early.
    Each product is displayed with its name, price, and quantity,
    separated by a dashed line.
    """
    if not inventary:
        print("No purchases recorded.\n")
        return # Stop here — no point iterating an empty list

    for products in inventary:
        print(f"""\nProduct : {products['name']}
Price   : ${products['price']:.2f}
Quantity: {products['quantity']}""")
        print("-" * 60)


def search_product():
    """
    Search for a product in the inventory by name (case-insensitive, partial match).

    Accepts a partial name — returns the first product whose name contains
    the search string. Prints the product details if found, or a not-found
    message if no match exists.

    Returns:
        dict: The matched product dictionary, or None if not found.
    """
    name = input("\nEnter the product name to search: ").strip().lower()

    # Validate search input — cannot be empty or contain numbers
    if not name:
        print(" Search term cannot be empty.")
        return None
    if any(char.isdigit() for char in name):
        print(" Product names do not contain numbers.")
        return None

    for products in inventary:
        if name in products["name"].lower(): # Partial, case-insensitive match
            print("\n Product found:")
            print(f""" Name     : {products['name']}
 Price    : ${products['price']:.2f}
 Quantity : {products['quantity']}""")
            return products # Return immediately on first match

    print(f" Product '{name}' not found.\n")
    return None


def update_product():
    """
    Update the price and/or quantity of an existing product.

    Searches for an exact name match (case-insensitive). If found, displays
    the current values and prompts for new ones. Fields left blank are skipped,
    keeping the original value. Negative numbers are rejected.
    """
    name = input("Enter the product to update: ").strip().lower()

    # Validate update target name
    if not name:
        print(" Name cannot be empty.")
        return
    if any(char.isdigit() for char in name):
        print(" Product names do not contain numbers.")
        return

    for products in inventary:
        if products["name"].lower() == name:

            # Show current values before asking for updates
            print(f"""
Current information:
  Name     : {products['name']}
  Price    : ${products['price']:.2f}
  Quantity : {products['quantity']}
""")
            updated_price = input("New price (leave blank to keep current): ").strip()

            # Only update price if the user typed something
            if updated_price:
                try:
                    new_price = float(updated_price)
                    if new_price < 0:
                        print(" Price cannot be negative.")
                    else:
                        products["price"] = new_price
                        print(" Price updated!")
                except ValueError:
                    print(" Invalid price.")

            updated_quantity = input("New quantity (leave blank to keep current): ").strip()

            # Only update quantity if the user typed something
            if updated_quantity:
                try:
                    new_quantity = int(updated_quantity)
                    if new_quantity < 0:
                        print(" Quantity cannot be negative.")
                    else:
                        products["quantity"] = new_quantity
                        print(" Quantity updated!")
                except ValueError:
                    print(" Invalid quantity.")

            return # Stop after updating the first match

    print(f" Product '{name}' not found.")


def delete_product():
    """
    Delete a product from the inventory by name after user confirmation.

    Searches for an exact name match (case-insensitive). Prompts for
    confirmation before removing. If the user cancels, inventory is unchanged.
    """
    name = input("\nEnter the name of the product to delete: ").strip().lower()

    # Validate delete target name
    if not name:
        print(" Name cannot be empty.")
        return
    if any(char.isdigit() for char in name):
        print(" Product names do not contain numbers.")
        return

    for product in inventary:
        if product["name"].lower().strip() == name:

            confirm = input(f" Are you sure you want to delete '{product['name']}'? (yes/no): ").strip().lower()

            # Validate confirmation — only accept 'yes' or 'no'
            if confirm not in ("yes", "no"):
                print(" Please type 'yes' or 'no'. Deletion cancelled.")
                return

            if confirm == "yes":
                inventary.remove(product)
                print(f" Product '{product['name']}' deleted successfully!\n")
            else:
                print(" Deletion cancelled.\n")
            return # Stop after finding the product, whether deleted or not

    print(f" Product '{name}' not found.\n")
    def calculate_statistics():
    """
    Compute and display summary statistics for the current inventory.

    Calculates:
        - Total units across all products.
        - Total inventory value (price × quantity per product).
        - The most expensive product by unit price.
        - The product with the highest stock quantity.
        - All products sorted by price (descending).
        - All products sorted by quantity (descending).

    If the inventory is empty, notifies the user and returns early.
    """
    if not inventary:
        print("  No products to calculate statistics.\n")
        return

    total_units = 0
    total_value = 0
    most_expensive = inventary[0] # Start with the first product as baseline
    most_stock = inventary[0]

    for product in inventary:
        total_units += product["quantity"]
        total_value += product["price"] * product["quantity"]

        # Update most expensive if current product has a higher price
        if product["price"] > most_expensive["price"]:
            most_expensive = product

        # Update highest stock if current product has more units
        if product["quantity"] > most_stock["quantity"]:
            most_stock = product

    # Sort copies of the list — does not modify the original inventory
    sorted_by_price    = sorted(inventary, key=lambda p: p["price"],    reverse=True)
    sorted_by_quantity = sorted(inventary, key=lambda p: p["quantity"], reverse=True)

    print("\n" + "=" * 60)
    print("  INVENTORY STATISTICS")
    print("-" * 60)
    print(f"  Total units in stock  : {total_units}")
    print(f"  Total inventory value : ${total_value:.2f}")
    print(f"  Most expensive product: {most_expensive['name']} (${most_expensive['price']:.2f})")
    print(f"  Highest stock product : {most_stock['name']} ({most_stock['quantity']} units)")

    print("\n--- Products sorted by price (high to low) ---")
    for product in sorted_by_price:
        print(f"  {product['name']} — ${product['price']:.2f}")

    print("\n--- Products sorted by quantity (high to low) ---")
    for product in sorted_by_quantity:
        print(f"  {product['name']} — {product['quantity']} units")

    print("=" * 60)
