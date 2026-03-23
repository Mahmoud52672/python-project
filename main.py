import tkinter as tk
from tkinter import ttk, messagebox
import csv
import os

FILE_NAME = "assets.csv"

# دالة لإضافة البيانات وتحديث الجدول
def save_data():
    asset_id = entry_id.get().strip()
    name = entry_name.get().strip()
    
    if asset_id and name:
        with open(FILE_NAME, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([asset_id, name])
        update_table()
        entry_id.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        messagebox.showinfo("Success", "Asset added successfully!")
    else:
        messagebox.showwarning("Input Error", "Please fill in all fields")

# دالة لتحديث الجدول عند فتح البرنامج
def update_table():
    for item in table.get_children():
        table.delete(item)
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as f:
            reader = csv.reader(f)
            for row in reader:
                if row: table.insert("", "end", values=row)

# إعداد الواجهة
root = tk.Tk()
root.title("Lab Asset Manager System")
root.geometry("450x450")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack(fill=tk.BOTH, expand=True)

tk.Label(frame, text="Asset ID:").pack(anchor="w")
entry_id = tk.Entry(frame, width=40)
entry_id.pack(pady=5)

tk.Label(frame, text="Asset Name:").pack(anchor="w")
entry_name = tk.Entry(frame, width=40)
entry_name.pack(pady=5)

btn_save = tk.Button(frame, text="Add to Inventory", command=save_data, bg="#4CAF50", fg="white")
btn_save.pack(pady=15)

# الجدول
table = ttk.Treeview(frame, columns=("ID", "Name"), show="headings", height=8)
table.heading("ID", text="Asset ID")
table.heading("Name", text="Asset Name")
table.column("ID", width=100)
table.column("Name", width=200)
table.pack(pady=10)

update_table()
root.mainloop()