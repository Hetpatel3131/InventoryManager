# AI Usage Report

**Student:** Het Patel  
**Course:** CPS 310  
**Project:** Campus IT Help Desk Hardware Locker (Inventory Manager)

## Tools Used

- ChatGPT (used as a debugging and troubleshooting reference while writing my code and testing edge cases)

## How AI Was Used

I wrote the core functions and structure for `inventory_manager.py` myself across my daily commits and used ChatGPT when I ran into specific errors or needed to double-check edge cases against the rubric. Specifically, I used it to:
- Troubleshoot a `NameError: name 'os' is not defined` when checking if `inventory.txt` existed at startup.
- Check the cleanest way to validate user inputs so non-numeric strings (`"abc"`), negative numbers (`"-2"`), and out-of-range item selections would not crash the program.
- Debug why `Peripherals` and `peripherals` were showing up as two separate categories in `display_summary()`.
- Review my edge-case test plan to make sure I did not miss any required validation checks (such as blocking the `|` pipe character in item names and categories).

## Example Prompts Used

1. *"I am getting `NameError: name 'os' is not defined` inside `load_inventory()` when checking `os.path.exists(filename)`. Why is this happening?"*
2. *"In Python, how can I make sure user input for quantity rejects negative numbers, decimals, and words like 'three' without crashing?"*
3. *"In my `display_summary()` dictionary, 'Peripherals' and 'peripherals' are being counted separately. How do I combine their counts regardless of capitalization?"*

## Suggestions Accepted

- **Adding `import os` at the top of the file:** Fixed the startup crash when `load_inventory()` checked whether `inventory.txt` existed.
- **Using `.strip()` and `.isdigit()` for input validation:** Used `.strip()` to clean extra spaces and `.isdigit()` to verify that item numbers and quantities are nonnegative whole numbers before converting them with `int()`.
- **Normalizing category keys with `.lower()`:** In `display_summary()`, converting `item["category"].lower()` before updating the `category_counts` dictionary allowed mixed-case categories to group together properly.

## Suggestions Rejected or Modified

- **First `display_summary()` approach:** When I first asked about summarizing low-stock items, ChatGPT suggested printing a separate numbered list of low-stock items and left out the category breakdown. I rejected that approach and wrote `display_summary()` to match the rubric by counting unique items, total quantity, the number of low-stock items (below 5), and the item count per category.
- **Advanced Python shortcuts:** ChatGPT occasionally suggested one-line list comprehensions or `collections.Counter` for counting categories. I rejected those because we are only using introductory Python loops, dictionaries, and standard `if/elif/else` statements in this course.

## Verification & Testing

Every time I fixed a bug or adjusted an input check, I tested it directly in the VS Code terminal before committing:
- Verified that starting the program without `inventory.txt` prints `Loaded 0 items.` and opens the menu safely.
- Tested all 14 required test cases and 10 additional validation checks using the controlled 5-item dataset (including invalid menu options, out-of-range item numbers, duplicate names with different capitalization, and pipe characters).
- Confirmed that changes made in `add_item()`, `update_quantity()`, and `remove_item()` persist in `inventory.txt` after exiting with option 7 and restarting the program.
- Recorded all 24 passing test observations in `TESTING.md`.

## Code Understanding (`update_quantity` Walkthrough)

In my own words, here is how `update_quantity(inventory)` works step by step:

1. **Empty Check:** First, `if not inventory:` checks whether the inventory list is empty. If there are no items, it prints `"No inventory items found."` and returns to the main menu right away instead of asking for an item number.
2. **Display & Select:** It calls `view_inventory(inventory)` so the user can see the numbered list of items, then prompts the user to enter the item number they want to update (using `.strip()` to remove extra spaces).
3. **1-Based to 0-Based Index Check:** It checks `selection.isdigit()` to make sure the user typed a valid positive number, then subtracts 1 (`index = int(selection) - 1`) because Python lists start at index `0` while the displayed list starts at `1`. It then verifies `0 <= index < len(inventory)` so numbers like `0` or `999` are rejected as out of range.
4. **Validate New Quantity:** Next, it asks for the new quantity and checks `quantity.isdigit()`. Because `.isdigit()` only returns `True` for characters `0–9`, it automatically blocks words (`"eight"`), decimals (`"2.5"`), and negative numbers (`"-1"`).
5. **Update & Save:** Once validated, it converts the quantity to an integer, updates `inventory[index]["quantity"]` in memory, calls `save_inventory(inventory, INVENTORY_FILE)` so `inventory.txt` is immediately updated on disk, and prints a confirmation message with the item's name and new quantity.