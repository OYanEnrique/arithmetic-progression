# arithmetic-progression
A Python script that calculates and displays the first 10 terms of an Arithmetic Progression based on a user-provided first term and ratio.

# 📈 Arithmetic Progression (AP) Generator

This is a command-line Python program that generates and displays the first 10 terms of an Arithmetic Progression (AP).

The script prompts the user for the **first term** and the **common difference (ratio)** of the AP. It then uses a `for` loop to calculate each of the first 10 terms and displays them sequentially in a single line. 

## How to Use

1.  Make sure you have Python installed on your system.
2.  Save the code as a `.py` file (e.g., `arithmetic_progression.py`).
3.  Open your terminal or command prompt.
4.  Run the script with the following command:
    ```sh
    python arithmetic_progression.py
    ```
5.  Enter the first term of the AP and press Enter.
6.  Enter the ratio (common difference) of the AP and press Enter. The program will then display the first 10 terms of the progression.

## Program Logic

* **User Input:** The program captures the `first_term` and the `ratio` (common difference) of the progression.
* **Term Calculation:** A `for` loop iterates 10 times (using `range(0, 10)`). In each iteration, the general term formula for an AP is applied:
  `term = first_term + (n * ratio)`, where `n` is the term's position in the loop (from 0 to 9).
* **Formatted Output:** The `print()` function is used with the `end = '  ->  '` argument to ensure all terms are displayed on the same line, separated by an arrow, creating a clear visualization of the progression.
* **Dramatic Pause:** The `sleep(1)` function from the `time` module is used to create a short pause before displaying the results, improving the user experience.
