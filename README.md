# Python Password Generator

A lightweight, command-line password generator written in Python using only built-in standard libraries. It creates randomized passwords combining lowercase letters, uppercase letters, numbers, and special symbols.

## Features

* **Zero External Dependencies:** Uses only Python's native `random` and `string` modules.
* **Custom Password Length:** Prompts the user to specify their desired password length.
* **Built-in Input Validation:**
  * Enforces a minimum length of **6 characters** if a smaller number is entered.
  * Gracefully handles non-numeric inputs by defaulting to **8 characters**.
* **High Character Variety:** Draws from all standard ASCII printable characters (`a-z`, `A-Z`, `0-9`, and punctuation symbols).

## Prerequisites

* Python 3.6 or higher

## Usage

1. Save the script as `password_generator.py`.
2. Open your terminal or command prompt and navigate to the script's directory.
3. Run the script:

```bash
python password_generator.py
