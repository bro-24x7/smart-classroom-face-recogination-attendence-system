import cv2
import os
import numpy as np
from PIL import Image
from tkinter import *
from tkinter import messagebox

class Train:
    def __init__(self, root):
        self.root = root
        self.root.title("Train Dataset")
        self.root.geometry("600x400")

        Label(self.root, text="Training Faces...", font=("times new roman", 20, "bold")).pack(pady=20)
        Button(self.root, text="Start Training", command=self.train_classifier, bg="green", fg="white", font=("arial", 15, "bold")).pack(pady=10)

    def train_classifier(self):
        data_dir = "data"
        if not os.path.exists(data_dir):
            messagebox.showerror("Error", f"'{data_dir}' folder not found.")
            return

        faces = []
        ids = []
        for file in os.listdir(data_dir):
            path = os.path.join(data_dir, file)
            img = Image.open(path).convert("L")  # grayscale
            imageNp = np.array(img, "uint8")
            id = int(os.path.split(path)[1].split(".")[1])
            faces.append(imageNp)
            ids.append(id)

        ids = np.array(ids)

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.train(faces, ids)
        recognizer.save("classifier.xml")

        messagebox.showinfo("Result", "Training dataset completed successfully!")
