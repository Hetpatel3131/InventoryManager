# Inventory Manager

**Author:** Het Patel  
**Course:** CPS 310  
**Theme:** Campus IT Help Desk Hardware Locker

## Project Description

Inventory Manager is a command-line Python program I built to track supplies in a campus IT Help Desk hardware locker, including keyboards, mice, cables, adapters, and screwdriver sets. 

While the program is running, all items are stored in memory as a list of dictionaries (`name`, `category`, and `quantity`). Changes are saved to `inventory.txt` using pipe (`|`) delimiters so the data stays updated after the program closes.

## Features

- Loads existing inventory from `inventory.txt` at startup (or starts with an empty list if the file does not exist yet).
- Displays all items in a numbered list.
- Adds new items while blocking empty inputs, pipe characters (`|`), and duplicate item names (case-insensitive).
- Updates item quantities and removes items by their list number.
- Searches for items by name using case-insensitive partial matching.
- Displays an inventory summary showing total unique items, total quantity in stock, low-stock items (quantity below 5), and item counts per category.
- Automatically saves changes to `inventory.txt` after adding, updating, or removing items.

## Requirements

- Python 3 (uses only the Python standard library; no external packages required)
- Terminal (macOS Terminal or VS Code terminal)
- Git

## Project Files

- `inventory_manager.py` – Main program containing the menu loop and all 10 inventory functions.
- `inventory.txt` – Pipe-delimited text file storing the inventory items (`Name|Category|Quantity`).
- `README.md` – Project overview and instructions for running the program.
- `TESTING.md` – Test cases, expected outputs, and actual test results.
- `AI_USAGE.md` – Notes on how I used AI to help debug errors and check edge cases.
- `.gitignore` – Ignores `__pycache__/`, `.venv/`, `.DS_Store`, and temporary files.

## How to Run the Program

1. Open the project folder in VS Code and open the integrated terminal.
2. Make sure you are in the project directory containing `inventory_manager.py` and `inventory.txt`.
3. Run the program:

```bash
python3 inventory_manager.py