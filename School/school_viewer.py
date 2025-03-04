import os
import tkinter as tk
from tkinter import filedialog, ttk, messagebox

# Set the base directory (your school structure)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Sets BASE_DIR to the "school" folder
  # Ensure this path is correct

# Function to list files/folders in the selected directory
def list_files(directory):
    file_list.delete(*file_list.get_children())  # Clear previous items
    try:
        for item in os.listdir(directory):
            full_path = os.path.join(directory, item)
            if os.path.isdir(full_path):
                file_list.insert("", "end", text=f"[Folder] {item}", values=(full_path,))
            else:
                file_list.insert("", "end", text=item, values=(full_path,))
    except Exception as e:
        messagebox.showerror("Error", f"Cannot access {directory}\n{str(e)}")

# Function to handle item selection (open folders or files)
def on_item_double_click(event):
    selected_item = file_list.selection()
    if selected_item:
        item_path = file_list.item(selected_item, "values")[0]
        if os.path.isdir(item_path):
            # Only allow browsing within the school folder
            if item_path.startswith(BASE_DIR):
                list_files(item_path)
            else:
                messagebox.showwarning("Warning", "You cannot go outside the school folder!")
        else:
            os.system(f'notepad "{item_path}"')  # Open files (Windows) – change for Linux/Mac

# Create GUI window
root = tk.Tk()
root.title("School Structure Browser")
root.geometry("600x400")

# Title Label
label = tk.Label(root, text="School File Browser", font=("Arial", 14, "bold"))
label.pack(pady=10)

# File List (Treeview)
file_list = ttk.Treeview(root, columns=("Path",), show="tree")
file_list.pack(expand=True, fill="both", padx=10, pady=5)

# Populate with initial school folder contents
list_files(BASE_DIR)

# Double-click to navigate
file_list.bind("<Double-1>", on_item_double_click)

# Run GUI
root.mainloop()
