# Calculator-in-python
🧮 Python Multi-Function Calculator
This is a simple yet versatile Python calculator that supports multiple operations, including basic arithmetic, hashing, multiplication tables, counting, and more. It runs in the terminal and allows users to repeatedly perform calculations until they choose to exit.

✨ Features
Basic Arithmetic:

Addition (+)

Subtraction (-)

Multiplication (*)

Division (/)

Exponentiation (**)

Modulus (%)

Extra Utilities:

Multiplication Table (t): Generates a multiplication table for a given number up to a specified limit.

Counting (c): Prints counting numbers from a starting point to an endpoint.

Hashing (#): Generates Python’s built-in hash for any alphanumeric string.

User-Friendly Input Handling: Ensures the user enters valid values before performing operations.

Looping Mode: After completing a calculation, the user can choose to perform another operation without restarting the program.

🔧 How It Works
The program prompts the user to select an action.

Based on the selected operation, it requests the necessary inputs.

Results are displayed instantly in a clean format.

The user can choose to perform additional operations or exit.

🖥️ Example Run
text
Copy
Edit
Calculator  
ctrl+c to terminate  
This Calculator is able to perform *, /, -, +, **, %, #, t for table, c for counting etc  
Now Enter the action You want to Perform: t  
Enter the number whose table you want: 5  
Enter the limit where it's going to be stop: 10  
5  *  1  =  5  
5  *  2  =  10  
...  
🚀 How to Run
bash
Copy
Edit
python calculator.py
📌 Notes
This script is for educational purposes and to demonstrate Python’s basic input handling and control flow using match-case.

Currently, advanced input validation and error handling for invalid operations (e.g., division by zero) are minimal.
