# Credit Card Validator (Luhn Algorithm)

This project demonstrates how to validate credit card numbers using the
**Luhn Algorithm**, a checksum formula used to validate various
identification numbers, most commonly credit card numbers.

------------------------------------------------------------------------

## 📌 Features

-   Removes spaces and dashes from card number inputs automatically
-   Implements the Luhn algorithm for validation
-   Provides a simple interface to check if a card is **VALID** or
    **INVALID**

------------------------------------------------------------------------

## 📝 How It Works

The program: 1. Reverses the card number. 2. Splits digits into odd and
even positions (from the right). 3. Adds odd-position digits directly to
the sum. 4. Doubles even-position digits. If doubling results in two
digits (e.g., 16), their sum is added (1 + 6 = 7). 5. Adds both sums
together. 6. If the total modulo 10 equals 0, the card is considered
**VALID**.

------------------------------------------------------------------------

## 🚀 Usage

### 1. Clone or copy the code into a Python file:

``` bash
card_validator.py
```

### 2. Run the script:

``` bash
python card_validator.py
```

### 3. Example output:

    VALID!

------------------------------------------------------------------------

## 📂 Example Card Number

The included test case is:

    4111-1111-4555-1142

-   After processing, the program will output whether it is **VALID** or
    **INVALID**.

------------------------------------------------------------------------

## 📖 Luhn Algorithm Reference

The Luhn algorithm is widely used for validating: - Credit card
numbers - IMEI numbers - Other identification numbers

------------------------------------------------------------------------

## 🛠 Requirements

-   Python 3.x

No additional dependencies are required.

------------------------------------------------------------------------

## 👨‍💻 Author

Created as a simple demonstration of the Luhn algorithm in Python.
