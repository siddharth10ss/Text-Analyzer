# 📝 Text Analyzer Project

This Python project allows you to **analyze the contents of any text file**. It reads the file, processes the text, and provides detailed statistics including:

- ✅ Total number of words  
- ✅ Total number of characters  
- ✅ Average word length  
- ✅ Number of sentences  
- ✅ Most frequent word  
- ✅ Longest word

---

## 🚀 How It Works

When you run the script, a file dialog will pop up. Simply select a `.txt` file from your system, and the script will analyze its contents and display the results in the terminal.

---

## 🛠 Features

- File picker using `tkinter`
- Handles any `.txt` file
- Ignores punctuation during word analysis
- Uses `Counter` from `collections` for frequency stats

---

## 📦 Requirements

No external libraries needed! It uses built-in Python modules:
- `tkinter`
- `collections`
- `string`

---

## ▶️ How to Run

1. Open your terminal or PowerShell.
2. Navigate to the project directory.
3. Run the script:
   ```bash
   python Word_Counter.py
