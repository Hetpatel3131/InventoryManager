"""Manage supplies in a campus IT Help Desk hardware locker.

Author: Student Name
Course: Course Name
Date: MM/DD/YYYY
"""

import os


INVENTORY_FILE = "inventory.txt"


def display_menu():
    """Print the available inventory options."""
    print("\nInventory Manager")
    print("1. View inventory")
    print("2. Add an item")
    print("3. Update an item quantity")
    print("4. Remove an item")
    print("5. Search inventory")
    print("6. View inventory summary")
    print("7. Exit")


def load_inventory(filename):
    """Read inventory items from a file into a list of dictionaries."""
    inventory = []

    if not os.path.exists(filename):
        return inventory

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            line = line.strip()
            parts = line.split("|")

            # Skip lines that do not have all three fields.
            if len(parts) != 3:
                continue

            name = parts[0].strip()
            category = parts[1].strip()

            try:
                quantity = int(parts[2])
            except ValueError:
                # Skip this item if its quantity is not a whole number.
                continue

            inventory.append({
                "name": name,
                "category": category,
                "quantity": quantity
            })

    return inventory


def save_inventory(inventory, filename):
    """Write each inventory item to the file using pipe separators."""
    with open(filename, "w", encoding="utf-8") as file:
        for item in inventory:
            name = item["name"]
            category = item["category"]
            quantity = item["quantity"]
            file.write(f"{name}|{category}|{quantity}\n")


def view_inventory(inventory):
    """Display all inventory items in a numbered list."""
    if not inventory:
        print("No inventory items found.")
        return

    print("Inventory:")
    for number, item in enumerate(inventory, 1):
        print(f"{number}. {item['name']} | {item['category']} | Quantity: {item['quantity']}")


def add_item(inventory):
    """Validate a new item, add it to the inventory, and save it."""
    name = input("Enter the item name: ").strip()
    if not name:
        print("Item name cannot be empty.")
        return

    if "|" in name:
        print("Item name cannot contain the pipe character '|'.")
        return

    category = input("Enter the category: ").strip()
    if not category:
        print("Category cannot be empty.")
        return

    if "|" in category:
        print("Category cannot contain the pipe character '|'.")
        return

    quantity = input("Enter the quantity: ").strip()
    if not quantity.isdigit():
        print("Quantity must be a nonnegative whole number.")
        return

    for item in inventory:
        if item["name"].lower() == name.lower():
            print("An item with that name already exists.")
            return

    inventory.append({
        "name": name,
        "category": category,
        "quantity": int(quantity)
    })

    save_inventory(inventory, INVENTORY_FILE)
    print("Item added successfully.")


def update_quantity(inventory):
    """Find an item and change its quantity."""
    pass


def remove_item(inventory):
    """Find an item and remove it from the inventory."""
    pass


def search_inventory(inventory):
    """Search for inventory items by name or category."""
    pass


def display_summary(inventory):
    """Show inventory totals and items that are running low."""
    pass


def main():
    """Load the inventory and report how many items were loaded."""
    inventory = load_inventory(INVENTORY_FILE)
    print(f"Loaded {len(inventory)} items.")


if __name__ == "__main__":
    main()
