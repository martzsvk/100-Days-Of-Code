# Day 26: NATO Alphabet Converter 🔤

A text-to-phonetic-code converter that transforms any word into its NATO phonetic equivalent (e.g., "A" becomes "Alfa"). This project focuses on List and Dictionary Comprehension, which are the building blocks of clean, "Pythonic" code.

## What I Learned 🛠️
* **List Comprehension:** Replacing multi-line `for` loops with concise, one-line syntax: `[new_item for item in list if test]`.
* **Data Processing with Pandas:** Using `pandas.iterrows()` to loop through a DataFrame and build a lookup dictionary efficiently.

## How it Works ⚙️
1. The code reads a CSV file containing the NATO phonetic alphabet.
2. It uses Dictionary Comprehension to create a dictionary where keys are the letters (A, B, C...) and values are the phonetic words (Alpha, Bravo, Charlie...).
3. The user inputs a word, and the script converts it to a list of phonetic words using List Comprehension.

### This project requires to install the Pandas library 📦
* You can do that by typing this into your IDE console
* `pip install pandas`
