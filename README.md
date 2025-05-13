# Simple Banking API

A lightweight, in-memory banking API to handle deposits, withdrawals, and transfers without any data persistence. This project provides a minimal HTTP interface to manage account balances.

## Features

* **Account Balance Check:** Retrieve the current balance of an account.
* **Deposit:** Add funds to an account. If the account doesn't exist, it's created.
* **Withdraw:** Remove funds from an existing account.
* **Transfer:** Move funds from one existing account to another. If the destination account doesn't exist, it's created.
* **State Reset:** Clear all account data.

## Technologies Used

* Python 3.x
* Flask
* pytest (for testing)

## Project Structure

![image](https://github.com/user-attachments/assets/fe624a07-2a76-4901-8c8f-fc9939b19233)

## Setup and Installation

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
2.  **Running the Application:**
    ```bash
    python run.py
    ```
Running Tests

To run the automated tests using pytest:
```bash
pytest
```

This will discover and run all tests located in the tests/ directory.
