import cv2
import numpy as np
from PIL import Image
from tkinter import *
from tkinter import messagebox
import os
import csv
from datetime import datetime

class face_recognitation:
    def __init__(self, root):
        self.root = root
        self.root.title("Face Recognition")
        self.root.geometry("700x500")

        Label(self.root, text="Face Recognition", font=("times new roman", 20, "bold")).pack(pady=20)
        Button(self.root, text="Start Recognition", command=self.recognize_face, bg="#4CAF50", fg="white").pack(pady=10)

    def mark_attendance(self, i, n):
        file = "Attendancesheet.csv"
        now = datetime.now()
        date = now.strftime("%Y-%m-%d")
        time = now.strftime("%H:%M:%S")
        with open(file, "a", newline="") as f:
            writer = csv.writer(f)
            writer.writerow([i, n, time, date, "Present"])

    def recognize_face(self):
        classifier_path = "classifier.xml"
        if not os.path.exists(classifier_path):
            messagebox.showerror("Error", "Classifier not trained yet!")
            return

        recognizer = cv2.face.LBPHFaceRecognizer_create()
        recognizer.read(classifier_path)
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

        cam = cv2.VideoCapture(0)
        while True:
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = faceCascade.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
                confidence = int(100 * (1 - confidence / 300))
                if confidence > 77:
                    cv2.putText(img, f"ID: {id}", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)
                    self.mark_attendance(id, f"Student_{id}")
                else:
                    cv2.putText(img, "Unknown", (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,0,255), 2)
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 255, 0), 2)

            cv2.imshow("Face Recognition", img)
            if cv2.waitKey(1) == 13:  # Enter key
                break
        cam.release()
        cv2.destroyAllWindows()
