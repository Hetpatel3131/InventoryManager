# Inventory Manager Testing

**Student:** Het Patel  
**Course:** CPS 310  
**Project:** Campus IT Help Desk Hardware Locker  
**Test Date:** October 15, 2026  

## Test Environment

- **Operating System:** macOS
- **Language:** Python 3.12 (Standard Library only)
- **Interface:** VS Code Integrated Terminal

## Test Setup & Dataset

Before running my tests, I backed up my original `inventory.txt` file outside the project folder.

- For **Tests 1 and 2**, I removed `inventory.txt` from the project folder to verify how the program handles a missing file on startup.
- For **Tests 3 through 24**, I placed the following 5-item controlled dataset into `inventory.txt` (with mixed capitalization on `Peripherals` and `peripherals` to test case-insensitive category grouping):

USB Keyboard|Peripherals|12
USB Mouse|peripherals|8
HDMI Cable|Cables|4
Ethernet Cable|Cables|6
Screwdriver Set|Tools|2

**Baseline Summary Totals:**
- Unique items: 5
- Total quantity: 32
- Low-stock items (below 5): 2 (`HDMI Cable` and `Screwdriver Set`)
- Categories: `peripherals: 2`, `cables: 2`, `tools: 1`

---

## Required Tests (1–14)

| # | Feature | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|
| 1 | Missing inventory file | Removed `inventory.txt` from the folder and ran `python3 inventory_manager.py`. | Starts with empty inventory, reports 0 loaded items, and shows menu without crashing. | Printed `Loaded 0 items.` and displayed the main menu normally. | Pass |
| 2 | View empty inventory | Selected option `1` during the same run with no file. | Displays `"No inventory items found."` and returns to menu. | Printed `No inventory items found.` and returned to the menu. | Pass |
| 3 | Add a valid item | Loaded the 5-item baseline file, selected option `2`, and entered `Test Adapter`, `Adapters`, `3`. | Confirmation appears. `Test Adapter` has quantity 3 in memory and in `inventory.txt` (6 items, 35 units). | Printed `Item added successfully.` Option 1 showed item #6 (`Test Adapter`), and `inventory.txt` had `Test Adapter|Adapters|3` at the bottom. | Pass |
| 4 | Reject empty item name | Selected option `2` and pressed Enter without typing a name. | Displays empty-name error and returns to menu without adding an item. | Printed `Item name cannot be empty.` and returned to the main menu. | Pass |
| 5 | Reject duplicate name | Selected option `2` and entered `usb keyboard`, `Peripherals`, `1`. | Rejects duplicate name regardless of case; existing quantity stays 12. | Printed `An item with that name already exists.` `USB Keyboard` stayed at quantity 12. | Pass |
| 6 | Reject nonnumeric quantity | Selected option `2` and entered `Invalid Quantity Item`, `Tools`, `three`. | Displays whole-number error; no item is added or saved. | Printed `Quantity must be a nonnegative whole number.` Item was not added. | Pass |
| 7 | Reject negative quantity | Selected option `2` and entered `Negative Quantity Item`, `Tools`, `-2`. | Displays nonnegative whole-number error; no item is added. | Printed `Quantity must be a nonnegative whole number.` Item was not added. | Pass |
| 8 | Update a valid item | Selected option `3`, entered `6` (`Test Adapter`), and entered new quantity `8`. | Confirmation names `Test Adapter` and `8`. Updates memory and file (total units = 40). | Printed `Test Adapter quantity updated to 8.` Checked `inventory.txt` and confirmed `Test Adapter|Adapters|8`. | Pass |
| 9 | Reject invalid item number | Selected option `3` and tested `abc`, `0`, and `999`. | Rejects letters, `0`, and out-of-range numbers without crashing. | `abc` printed `Please enter a valid item number.` Both `0` and `999` printed `Item number is out of range.` | Pass |
| 10 | Remove an item | Selected option `4` and entered `6` (`Test Adapter`). | Confirmation names `Test Adapter`. Item is removed from memory and disk (back to 5 items, 32 units). | Printed `Item removed: Test Adapter`. Checked `inventory.txt` and confirmed it returned to the 5 baseline items. | Pass |
| 11 | Case-insensitive partial search | Selected option `5` and entered `cAbLe`. | Displays both `HDMI Cable` and `Ethernet Cable` with categories and quantities. | Printed `Search Results:` followed by `1. HDMI Cable` (qty 4) and `2. Ethernet Cable` (qty 6). | Pass |
| 12 | Search with no matches | Selected option `5` and entered `zzz-no-match`. | Displays `"No inventory items matched your search."` and returns to menu. | Printed `No inventory items matched your search.` and showed the menu. | Pass |
| 13 | Verify inventory summary | Selected option `6` with the 5 baseline items loaded. | Shows 5 unique items, 32 total units, 2 low-stock items, and combines `Peripherals` / `peripherals` into 2. | Displayed `Unique items: 5`, `Total quantity: 32`, `Low-stock items: 2`, and category counts `peripherals: 2`, `cables: 2`, `tools: 1`. | Pass |
| 14 | Restart and persistence | Added `Persistence Cable` (`Cables`, `7`), exited (`7`), and restarted. Then removed `Persistence Cable`, exited, and restarted again. | First restart loads 6 items (39 units) with `Persistence Cable`. Second restart loads 5 items (32 units). | First restart printed `Loaded 6 items.` and summary showed 39 units. After removing and restarting, printed `Loaded 5 items.` with 32 units. | Pass |

---

## Additional Validation Checks (15–24)

| # | Feature | Input or Action | Expected Result | Actual Result | Pass/Fail |
|---|---|---|---|---|---|
| 15 | Empty category | Selected option `2`, entered `Empty Category Item`, and typed only spaces for category. | Rejects category as empty after `.strip()`; no item added. | Printed `Category cannot be empty.` and returned to the menu. | Pass |
| 16 | Pipe in item name | Selected option `2` and entered `Test&#124;Cable` as the item name. | Displays pipe-character error and does not add item. | Printed `Item name cannot contain the pipe character '|'.` | Pass |
| 17 | Pipe in category | Selected option `2`, entered `Pipe Category Item`, and entered `Tools&#124;Cables` for category. | Displays pipe-character error and does not add item. | Printed `Category cannot contain the pipe character '|'.` | Pass |
| 18 | Empty search | Selected option `5` and pressed Enter, then repeated with spaces only. | Both attempts display `"Search term cannot be empty."` | Both attempts printed `Search term cannot be empty.` and returned to the menu. | Pass |
| 19 | Invalid menu input | Entered `9`, `abc`, and empty Enter at the main menu prompt. | Prints invalid-choice message and re-displays the menu. | Printed `Invalid choice. Please enter a number from 1 to 7.` for all three inputs. | Pass |
| 20 | Invalid removal selection | Selected option `4` and entered `abc`, then repeated with `0` and `999`. | Rejects all three safely without removing anything or crashing. | `abc` printed `Please enter a valid item number.` Both `0` and `999` printed `Item number is out of range.` | Pass |
| 21 | Invalid update quantity | Selected option `3`, chose `1` (`USB Keyboard`), and tried `eight`, `-1`, and `2.5`. | Rejects each invalid quantity; `USB Keyboard` remains at 12. | Printed `Quantity must be a nonnegative whole number.` each time. Quantity stayed at 12. | Pass |
| 22 | Whitespace and zero quantity | Added `  Zero Stock Item  ` in category `  Tools  ` with quantity `0`. Checked view, summary, and file, then removed it. | Trims spaces, accepts `0`, and counts it as low stock (6 items, 32 units, 3 low-stock). | Saved as `Zero Stock Item|Tools|0`. Summary showed 6 unique items, 32 units, and 3 low-stock items. Removed cleanly afterward. | Pass |
| 23 | Low-stock boundary | Updated `HDMI Cable` from `4` to `5`, checked summary, then updated it back to `4`. | At quantity 5, it is not low stock (1 low-stock item, 33 units). At 4, returns to 2 low-stock items (32 units). | At 5, summary showed `Low-stock items: 1` and `Total quantity: 33`. Restoring to 4 returned summary to `2` low-stock and `32` units. | Pass |
| 24 | Empty inventory update and removal | Tested options `3` and `4` using an empty `inventory.txt`. | Both print `"No inventory items found."` immediately without asking for an item number. | Both options printed `No inventory items found.` and returned to the menu. | Pass |

---

## Bug Fix & Retest Record

| Test # | Initial Problem Observed | Change Made | Retest Date | Actual Retest Result | Final Status |
|---|---|---|---|---|---|
| 13 | During my first test of `display_summary()`, `Peripherals` and `peripherals` were counted separately (`Peripherals: 1`, `peripherals: 1`) because dictionary keys are case-sensitive. | Converted the category string to lowercase using `item["category"].lower()` before adding to the category count dictionary. | 10/15/2026 | Summary combined both records under `peripherals: 2`. | Pass |

## Final Test Summary

- **Required tests completed:** 14 / 14
- **Additional validation checks completed:** 10 / 10
- **Total tests passed:** 24 / 24
- **Total tests failed:** 0
- **Original sample `inventory.txt` restored:** Yes (verified 5 items, 3 categories, and low-stock items present before final push).