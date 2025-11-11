import os
import subprocess
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from Student import student
from Face_Recognitation import face_recognitation
from train import Train
from attendance import Attendace

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1500x790+0+0")
        self.root.title("Face Recognition System")

        # --- Helper: safely load images ---
        def load_image(filename, size):
            path = os.path.join("Software Image", filename)
            if not os.path.exists(path):
                # Create placeholder if missing
                img = Image.new("RGB", size, color=(200, 200, 200))
            else:
                img = Image.open(path).resize(size, Image.Resampling.LANCZOS)
            return ImageTk.PhotoImage(img)

        # --- Top header images ---
        self.photoimg = load_image("B-1.png", (500, 130))
        Label(self.root, image=self.photoimg).place(x=0, y=0, width=500, height=130)

        self.photoimg1 = load_image("M-1.png", (500, 130))
        Label(self.root, image=self.photoimg1).place(x=500, y=0, width=500, height=130)

        self.photoimg2 = load_image("B-1.png", (500, 130))
        Label(self.root, image=self.photoimg2).place(x=1000, y=0, width=500, height=130)

        # --- Background image ---
        self.photoimg3 = load_image("Background.png", (1530, 710))
        bg_image = Label(self.root, image=self.photoimg3)
        bg_image.place(x=0, y=130, width=1530, height=710)

        title_lbl = Label(
            bg_image,
            text="DASHBOARD",
            font=("times new roman", 35, "bold"),
            bg="#B1E0B8",
            fg="#001C57",
        )
        title_lbl.place(x=0, y=0, width=1530, height=45)

        # --- Dashboard buttons ---
        buttons = [
            ("Btn-1.png", (200, 100), "STUDENTS DETAILS", self.student_details_btn),
            ("Btn-2.png", (500, 100), "FACE DETECTOR", self.face_data),
            ("Btn-3.png", (800, 100), "ATTENDANCE", self.attendance_date_btn),
            ("Btn-4.png", (1100, 100), "SUPPORT", None),
            ("Btn-5.png", (200, 380), "TRAIN DATA", self.train_date_btn),
            ("Btn-6.png", (500, 380), "PHOTOS", self.open_image_btn),
            ("Btn-7.png", (800, 380), "DEVELOPER", None),
            ("Btn-9.png", (1100, 380), "EXIT", self.root.quit),
        ]

        for btn_img, (x, y), caption, command in buttons:
            img = load_image(btn_img, (220, 220))
            Button(bg_image, image=img, cursor="hand2", command=command).place(
                x=x, y=y, width=220, height=220
            )
            Button(
                bg_image,
                text=caption,
                cursor="hand2",
                command=command,
                font=("times new roman", 18, "bold"),
                bg="#FAF9F6",
                fg="#571945",
            ).place(x=x, y=y + 220, width=220, height=40)
            # Keep a reference so Python doesn't garbage-collect the image
            setattr(self, f"photo_{btn_img}", img)

    # --- Function buttons ---
    def student_details_btn(self):
        self.new_window = Toplevel(self.root)
        self.app = student(self.new_window)

    def train_date_btn(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)

    def open_image_btn(self):
        folder_path = os.path.join(os.getcwd(), "data")
        if os.path.exists(folder_path):
            try:
                if os.name == "nt":  # Windows
                    os.startfile(folder_path)
                elif os.name == "posix":  # macOS/Linux
                    subprocess.Popen(["open", folder_path])
            except Exception as e:
                print("Error opening folder:", e)
        else:
            print("Data folder not found:", folder_path)

    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = face_recognitation(self.new_window)

    def attendance_date_btn(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendace(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
