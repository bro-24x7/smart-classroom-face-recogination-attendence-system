import csv
import os
from tkinter import *
from tkinter import ttk, messagebox

class Attendace:
    def __init__(self, root):
        self.root = root
        self.root.title("Attendance Management")
        self.root.geometry("1000x600")

        self.attendance_data = []
        self.filename = "Attendancesheet.csv"

        Label(self.root, text="Attendance Details", font=("times new roman", 20, "bold")).pack(pady=10)
        Button(self.root, text="Load Attendance", command=self.load_csv, bg="#4CAF50", fg="white").pack(pady=5)
        Button(self.root, text="Save Attendance", command=self.save_csv, bg="#2196F3", fg="white").pack(pady=5)

        self.tree = ttk.Treeview(self.root, columns=("id", "name", "time", "date", "status"), show="headings")
        for col in self.tree["columns"]:
            self.tree.heading(col, text=col.upper())
            self.tree.column(col, width=150)
        self.tree.pack(fill=BOTH, expand=True)

    def load_csv(self):
        if not os.path.exists(self.filename):
            messagebox.showerror("Error", "No attendance file found.")
            return

        with open(self.filename, "r") as f:
            reader = csv.reader(f)
            self.tree.delete(*self.tree.get_children())
            for row in reader:
                self.tree.insert("", END, values=row)

    def save_csv(self):
        with open(self.filename, "w", newline="") as f:
            writer = csv.writer(f)
            for child in self.tree.get_children():
                writer.writerow(self.tree.item(child)["values"])
        messagebox.showinfo("Saved", "Attendance saved successfully!")
