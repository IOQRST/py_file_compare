import tkinter as tk
import logic
from tkinter import filedialog

root = tk.Tk()
root.title("File compare tool")


def compare_files():
    lines = logic.get_unique_lines(filedialog.askopenfilenames(filetypes=[("Text files", "*.txt")]))
    path = filedialog.asksaveasfilename(filetypes=[("Text Files", "*.txt")])
    logic.save_results(lines, path)

open_button = tk.Button(root, text="Compare text files", command=compare_files)
open_button.pack()

root.mainloop()