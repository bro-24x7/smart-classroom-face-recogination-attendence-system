import mysql.connector
from mysql.connector import Error
from tkinter import *
from tkinter import ttk, messagebox


class student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management")
        self.root.geometry("1050x600")

        # ---------- Variables ----------
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_sem = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()

        # ---------- Title ----------
        lbl_title = Label(self.root, text="STUDENT MANAGEMENT SYSTEM",
                          font=("times new roman", 25, "bold"),
                          bg="#5D6D7E", fg="white")
        lbl_title.pack(side=TOP, fill=X)

        # ---------- Frame ----------
        main_frame = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        main_frame.place(x=10, y=60, width=1030, height=530)

        # ---------- Left Frame (Form) ----------
        Left_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Details",
                                font=("times new roman", 15, "bold"), bg="white")
        Left_frame.place(x=10, y=10, width=480, height=500)

        # Department
        Label(Left_frame, text="Department", bg="white").grid(row=0, column=0, padx=10, pady=5, sticky=W)
        ttk.Combobox(Left_frame, textvariable=self.var_dep,
                     values=("Select Department", "Computer", "IT", "Civil", "Mechanical", "Electrical"),
                     state="readonly").grid(row=0, column=1, padx=10, pady=5, sticky=W)

        # Course
        Label(Left_frame, text="Course", bg="white").grid(row=1, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(Left_frame, textvariable=self.var_course, width=22).grid(row=1, column=1, padx=10, pady=5, sticky=W)

        # Year
        Label(Left_frame, text="Year", bg="white").grid(row=2, column=0, padx=10, pady=5, sticky=W)
        ttk.Combobox(Left_frame, textvariable=self.var_year,
                     values=("Select Year", "1", "2", "3", "4"),
                     state="readonly").grid(row=2, column=1, padx=10, pady=5, sticky=W)

        # Semester
        Label(Left_frame, text="Semester", bg="white").grid(row=3, column=0, padx=10, pady=5, sticky=W)
        ttk.Combobox(Left_frame, textvariable=self.var_sem,
                     values=("Select Semester", "1", "2", "3", "4", "5", "6", "7", "8"),
                     state="readonly").grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # Student ID
        Label(Left_frame, text="Student ID", bg="white").grid(row=4, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(Left_frame, textvariable=self.var_std_id, width=22).grid(row=4, column=1, padx=10, pady=5, sticky=W)

        # Name
        Label(Left_frame, text="Name", bg="white").grid(row=5, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(Left_frame, textvariable=self.var_std_name, width=22).grid(row=5, column=1, padx=10, pady=5, sticky=W)

        # Roll
        Label(Left_frame, text="Roll No", bg="white").grid(row=6, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(Left_frame, textvariable=self.var_roll, width=22).grid(row=6, column=1, padx=10, pady=5, sticky=W)

        # Gender
        Label(Left_frame, text="Gender", bg="white").grid(row=7, column=0, padx=10, pady=5, sticky=W)
        ttk.Combobox(Left_frame, textvariable=self.var_gender,
                     values=("Male", "Female", "Other"),
                     state="readonly").grid(row=7, column=1, padx=10, pady=5, sticky=W)

        # DOB
        Label(Left_frame, text="D.O.B", bg="white").grid(row=8, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(Left_frame, textvariable=self.var_dob, width=22).grid(row=8, column=1, padx=10, pady=5, sticky=W)

        # Email
        Label(Left_frame, text="Email", bg="white").grid(row=9, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(Left_frame, textvariable=self.var_email, width=22).grid(row=9, column=1, padx=10, pady=5, sticky=W)

        # Phone
        Label(Left_frame, text="Phone", bg="white").grid(row=10, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(Left_frame, textvariable=self.var_phone, width=22).grid(row=10, column=1, padx=10, pady=5, sticky=W)

        # Address
        Label(Left_frame, text="Address", bg="white").grid(row=11, column=0, padx=10, pady=5, sticky=W)
        ttk.Entry(Left_frame, textvariable=self.var_address, width=22).grid(row=11, column=1, padx=10, pady=5, sticky=W)

        # Buttons
        btn_frame = Frame(Left_frame, bg="white")
        btn_frame.grid(row=12, column=0, columnspan=2, pady=10)

        Button(btn_frame, text="Add", command=self.add_data, width=10, bg="#27AE60", fg="white").grid(row=0, column=0, padx=2)
        Button(btn_frame, text="Update", command=self.update_data, width=10, bg="#2980B9", fg="white").grid(row=0, column=1, padx=2)
        Button(btn_frame, text="Delete", command=self.delete_data, width=10, bg="#C0392B", fg="white").grid(row=0, column=2, padx=2)
        Button(btn_frame, text="Reset", command=self.reset_data, width=10, bg="#7D3C98", fg="white").grid(row=0, column=3, padx=2)

        # ---------- Right Frame (Table) ----------
        Right_frame = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Student Table",
                                 font=("times new roman", 15, "bold"), bg="white")
        Right_frame.place(x=510, y=10, width=510, height=500)

        scroll_x = Scrollbar(Right_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Right_frame, orient=VERTICAL)

        self.student_table = ttk.Treeview(
            Right_frame,
            columns=("dep", "course", "year", "sem", "id", "name", "roll", "gender", "dob", "email", "phone", "address"),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        for col in self.student_table["columns"]:
            self.student_table.heading(col, text=col.upper())
            self.student_table.column(col, width=100)

        self.student_table["show"] = "headings"
        self.student_table.pack(fill=BOTH, expand=True)
        self.student_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()

    
    # ---------- Database Connection ----------
    def connect_db(self):
     return mysql.connector.connect(
        host="127.0.0.1",       # 👈 Match Workbench
        user="abhi",
        password="abhi@1289",  # 👈 same as stored in Vault
        port=3306,
        database="face_recognition"
    )


    # ---------- Add ----------
    def add_data(self):
        if self.var_std_name.get() == "" or self.var_std_id.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
            return
        try:
            conn = self.connect_db()
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO student (dep, course, year, sem, student_id, name, roll, gender, dob, email, phone, address)
                VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
            """, (
                self.var_dep.get(), self.var_course.get(), self.var_year.get(),
                self.var_sem.get(), self.var_std_id.get(), self.var_std_name.get(),
                self.var_roll.get(), self.var_gender.get(), self.var_dob.get(),
                self.var_email.get(), self.var_phone.get(), self.var_address.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Student details added successfully", parent=self.root)
        except Error as e:
            messagebox.showerror("Error", f"Database error: {e}", parent=self.root)

    # ---------- Fetch ----------
    def fetch_data(self):
        try:
            conn = self.connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM student")
            data = cursor.fetchall()
            if len(data) != 0:
                self.student_table.delete(*self.student_table.get_children())
                for row in data:
                    self.student_table.insert("", END, values=row)
            conn.close()
        except Error as e:
            messagebox.showerror("Error", f"Database fetch error: {e}", parent=self.root)

    # ---------- Get Cursor ----------
    def get_cursor(self, event=""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]
        if data:
            self.var_dep.set(data[0])
            self.var_course.set(data[1])
            self.var_year.set(data[2])
            self.var_sem.set(data[3])
            self.var_std_id.set(data[4])
            self.var_std_name.set(data[5])
            self.var_roll.set(data[6])
            self.var_gender.set(data[7])
            self.var_dob.set(data[8])
            self.var_email.set(data[9])
            self.var_phone.set(data[10])
            self.var_address.set(data[11])

    # ---------- Update ----------
    def update_data(self):
        try:
            conn = self.connect_db()
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE student
                SET dep=%s, course=%s, year=%s, sem=%s, name=%s, roll=%s, gender=%s, dob=%s, email=%s, phone=%s, address=%s
                WHERE student_id=%s
            """, (
                self.var_dep.get(), self.var_course.get(), self.var_year.get(), self.var_sem.get(),
                self.var_std_name.get(), self.var_roll.get(), self.var_gender.get(), self.var_dob.get(),
                self.var_email.get(), self.var_phone.get(), self.var_address.get(), self.var_std_id.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Student details updated successfully", parent=self.root)
        except Error as e:
            messagebox.showerror("Error", f"Database update error: {e}", parent=self.root)

    # ---------- Delete ----------
    def delete_data(self):
        try:
            if self.var_std_id.get() == "":
                messagebox.showerror("Error", "Student ID required", parent=self.root)
                return
            conn = self.connect_db()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM student WHERE student_id=%s", (self.var_std_id.get(),))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Deleted", "Record deleted successfully", parent=self.root)
        except Error as e:
            messagebox.showerror("Error", f"Delete error: {e}", parent=self.root)

    # ---------- Reset ----------
    def reset_data(self):
        for var in [self.var_dep, self.var_course, self.var_year, self.var_sem,
                    self.var_std_id, self.var_std_name, self.var_roll, self.var_gender,
                    self.var_dob, self.var_email, self.var_phone, self.var_address]:
            var.set("")
        self.fetch_data()
