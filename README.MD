# ☕ Coffee Machine (Python)

A simple **console-based coffee machine simulation** written in Python.  
This project allows users to order drinks, check available resources, insert coins, and receive change — just like a real coffee machine.

---

## 📌 Features
- Order **espresso**, **latte**, or **cappuccino**
- View current machine resources using the `resources` command
- Coin-based payment system (quarters, dimes, nickels, pennies)
- Automatic resource deduction after each successful order
- Checks for sufficient ingredients before making a drink
- Continuous operation using a `while` loop
- Option to turn off the machine using `off`

---

## 🧠 Concepts Used
- Python dictionaries
- `while` loops
- Conditional statements (`if / elif / else`)
- User input handling
- Resource management logic
- Basic arithmetic and rounding
- Modular code using external data files

---

## 🗂 Project Structure
coffee-machine/
│
├── coffiemachine.py # Main program
├── data.py # Menu and resources data
└── README.md # Project documentation

yaml
Copy code

---

## ▶️ How to Run
1. Make sure Python is installed
2. Clone the repository:
   ```bash
   git clone <your-repo-url>
Run the program:

bash
Copy code
python coffiemachine.py
⌨️ Available Commands
Command	Action
espresso	Order espresso
latte	Order latte
cappuccino	Order cappuccino
resources	View available resources
off	Turn off the machine

🧪 Example
pgsql
Copy code
What is the drink you want to order (espresso/latte/cappuccino): latte
Please insert coins.
How many quarters?: 10
How many dimes?: 0
How many nickels?: 0
How many pennies?: 0
Here is $0.5 in change.
Here is your latte. Enjoy ☕
🚀 Learning Goal
This project is part of my Python learning journey and focuses on:

Writing clean logic

Understanding program flow

Practicing real-world problem solving

📚 Inspired By
100 Days of Code: Python by Dr. Angela Yu
