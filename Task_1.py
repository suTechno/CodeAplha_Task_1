import tkinter as tk
from tkinter import messagebox

def fibonacci(n):
    if n < 0:
        messagebox.showerror("Input Error", "Please enter a positive integer.")
        return []
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[-1] + fib_seq[-2])
    return fib_seq[:n]

def format_fibonacci_sequence(fib_sequence):
    formatted_sequence = []
    for i in range(2, len(fib_sequence)):
        formatted_sequence.append(f"{fib_sequence[i-2]} + {fib_sequence[i-1]} = {fib_sequence[i]}")
    return "\n".join(formatted_sequence)

def display_fibonacci_sequence():
    try:
        n = int(entry.get())
        fib_sequence = fibonacci(n)
        formatted_sequence = format_fibonacci_sequence(fib_sequence)
        text_widget.delete("1.0", tk.END)
        text_widget.insert(tk.END, formatted_sequence)
    except ValueError:
        messagebox.showerror("Input Error", "Please enter a valid integer.")

root = tk.Tk()
root.title("Fibonacci Sequence Generator")

label = tk.Label(root, text="Enter the number of terms:")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=5)

button = tk.Button(root, text="Generate", command=display_fibonacci_sequence)
button.pack(pady=10)

text_widget = tk.Text(root, height=10, width=50)
text_widget.pack(pady=10)

root.mainloop()
