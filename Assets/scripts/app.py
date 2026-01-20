import tkinter as tk
from tkinter import messagebox
import email_management
import os

def validation_ui():
    root = tk.Tk()
    root.title("Email Validation")
    root.geometry("380x220")
    root.resizable(False, False)
    root.configure(bg="#1e1e1e")

    icon_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "icons",
        "atlas.png"
    )

    icon = tk.PhotoImage(file=icon_path)
    root.iconphoto(True,icon)

    email_var = tk.StringVar()

    title = tk.Label(
        root,
        text="ClassHub Email Verification",
        bg="#1e1e1e",
        fg="#ffffff",
        font=("Segoe UI", 14, "bold")
    )
    title.pack(pady=(20, 10))

    # ---------- Email Entry ----------
    email_entry = tk.Entry(
        root,
        textvariable=email_var,
        width=30,
        bg="#2b2b2b",
        fg="#ffffff",
        insertbackground="#ffffff",
        relief="flat",
        font=("Segoe UI", 10)
    )
    email_entry.pack(pady=10)
    email_entry.focus()

    def submit():
        email = email_var.get().strip()
        if not email:
            messagebox.showerror("Error", "Please enter an email.")
            return

        root.destroy()
        global user_email
        user_email = email

    validate_btn = tk.Button(
        root,
        text="Send Verification",
        command=submit,
        bg="#3a7afe",
        fg="#ffffff",
        activebackground="#2f5fd1",
        activeforeground="#ffffff",
        relief="flat",
        font=("Segoe UI", 10, "bold"),
        padx=10,
        pady=5
    )
    validate_btn.pack(pady=15)

    root.mainloop()


user_email = None
validation_ui()

if user_email:
    result = email_management.send_validation_email(user_email, False)
