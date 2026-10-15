"""Manage supplies in a campus IT Help Desk hardware locker.

Author: Het Patel
Course: CPS 310
Date: 05/31/2006


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
    """Update an item's quantity and save the inventory."""
    if not inventory:
        print("No inventory items found.")
        return

    view_inventory(inventory)

    selection = input("Enter the item number to update: ").strip()
    if not selection.isdigit():
        print("Please enter a valid item number.")
        return

    try:
        index = int(selection) - 1
    except ValueError:
        print("Please enter a valid item number.")
        return

    if not (0 <= index < len(inventory)):
        print("Item number is out of range.")
        return

    quantity = input("Enter the new quantity: ").strip()
    if not quantity.isdigit():
        print("Quantity must be a nonnegative whole number.")
        return

    try:
        new_quantity = int(quantity)
    except ValueError:
        print("Quantity must be a nonnegative whole number.")
        return

    item = inventory[index]
    item["quantity"] = new_quantity

    save_inventory(inventory, INVENTORY_FILE)
    print(f"{item['name']} quantity updated to {new_quantity}.")


def remove_item(inventory):
    """Remove a selected item and save the inventory."""
    if not inventory:
        print("No inventory items found.")
        return

    view_inventory(inventory)

    selection = input("Enter the item number to remove: ").strip()
    if not selection.isdigit():
        print("Please enter a valid item number.")
        return

    try:
        index = int(selection) - 1
    except ValueError:
        print("Please enter a valid item number.")
        return

    if not (0 <= index < len(inventory)):
        print("Item number is out of range.")
        return

    removed_item = inventory.pop(index)

    save_inventory(inventory, INVENTORY_FILE)
    print(f"Item removed: {removed_item['name']}")

def search_inventory(inventory):
    """
    Search for inventory items by name using case-insensitive partial matching.
    Rejects empty or whitespace-only search queries.
    """
    query = input("Enter search term: ").strip()

    # Reject whitespace or empty searches per rubric requirement
    if not query:
        print("Search term cannot be empty.")
        return

    matches = []
    for item in inventory:
        if query.lower() in item["name"].lower():
            matches.append(item)

    if not matches:
        print("No inventory items matched your search.")
        return

    print("Search Results:")
    for number, item in enumerate(matches, 1):
        print(f"{number}. {item['name']} | {item['category']} | Quantity: {item['quantity']}")

def display_summary(inventory):
    """Show inventory totals and items with fewer than five units."""
    if not inventory:
        print("No inventory items found.")
        return

    total_quantity = 0
    low_stock_items = []

    for item in inventory:
        total_quantity += item["quantity"]

        if item["quantity"] < 5:
            low_stock_items.append(item)

    print("\nInventory Summary")
    print(f"Total item types: {len(inventory)}")
    print(f"Total units: {total_quantity}")

    print("\nLow-stock items (fewer than 5 units):")
    if not low_stock_items:
        print("No low-stock items.")
    else:
        for item in low_stock_items:
            print(f"{item['name']} | Quantity: {item['quantity']}")


def main():
    """Load inventory and handle menu choices until the user exits."""
    inventory = load_inventory(INVENTORY_FILE)
    print(f"Loaded {len(inventory)} items.")

    while True:
        display_menu()
        choice = input("Enter your choice (1-7): ").strip()

        if choice == "1":
            view_inventory(inventory)
        elif choice == "2":
            add_item(inventory)
        elif choice == "3":
            update_quantity(inventory)
        elif choice == "4":
            remove_item(inventory)
        elif choice == "5":
            search_inventory(inventory)
        elif choice == "6":
            display_summary(inventory)
        elif choice == "7":
            save_inventory(inventory, INVENTORY_FILE)
            print("Inventory saved. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()
