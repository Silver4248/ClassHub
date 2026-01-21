import tkinter as tk
from tkinter import messagebox
import os
import json
import sys

styles_data = None
try:
    with open(os.path.join(os.path.dirname(__file__), "styles.json"), "r") as file:
        styles_data = json.load(file)
except (FileNotFoundError, ValueError):
    sys.exit("File styles.json wasn't found, exiting.")


def validation_ui():
    user_email = None  # Local variable to store email
    
    root = tk.Tk()
    root.title("Email Validation")
    root.geometry("380x220")
    root.resizable(False, False)
    root.configure(bg=styles_data["BG_DARK"])
    root.attributes('-topmost', True)  # ← Keeps window on top

    icon_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "icons",
        "atlas.png"
    )

    try:
        icon = tk.PhotoImage(file=icon_path)
        root.iconphoto(True, icon)
    except:
        pass

    email_var = tk.StringVar()

    title = tk.Label(
        root,
        text="ClassHub Email Verification",
        bg=styles_data["BG_DARK"],
        fg=styles_data["TEXT_PRIMARY"],
        font=("Segoe UI", 14, "bold")
    )
    title.pack(pady=(20, 10))

    email_entry = tk.Entry(
        root,
        textvariable=email_var,
        width=30,
        bg=styles_data["BG_MEDIUM"],
        fg=styles_data["TEXT_PRIMARY"],
        insertbackground=styles_data["TEXT_PRIMARY"],
        relief="flat",
        font=("Segoe UI", 10)
    )
    email_entry.pack(pady=10)
    email_entry.focus()

    def submit():
        nonlocal user_email  # Access the local variable from outer function
        email = email_var.get().strip()
        if not email:
            messagebox.showerror("Error", "Please enter an email.")
            return

        user_email = email
        root.destroy()

    validate_btn = tk.Button(
        root,
        text="Send Verification",
        command=submit,
        bg=styles_data["ACCENT"],
        fg=styles_data["TEXT_PRIMARY"],
        activebackground=styles_data.get("ACCENT_DARK", "#2f5fd1"),
        activeforeground=styles_data["TEXT_PRIMARY"],
        relief="flat",
        font=("Segoe UI", 10, "bold"),
        padx=10,
        pady=5
    )
    validate_btn.pack(pady=15)

    root.mainloop()
    
    return user_email

def auth_ui():
    """
    Shows sign in/sign up UI and returns user data
    Returns: dict with keys 'action' (signin/signup), 'email', 'password', and 'name' (for signup only)
             or None if cancelled
    """
    user_data = None
    
    root = tk.Tk()
    root.title("ClassHub - Authentication")
    root.geometry("450x600")
    root.resizable(False, False)
    root.configure(bg=styles_data["BG_DARK"])
    root.attributes('-topmost', True)

    icon_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "icons",
        "atlas.png"
    )

    try:
        icon = tk.PhotoImage(file=icon_path)
        root.iconphoto(True, icon)
    except:
        pass

    # Variables
    signin_email_var = tk.StringVar()
    signin_password_var = tk.StringVar()
    
    signup_name_var = tk.StringVar()
    signup_email_var = tk.StringVar()
    signup_password_var = tk.StringVar()
    signup_confirm_var = tk.StringVar()

    # Main container
    container = tk.Frame(root, bg=styles_data["BG_DARK"])
    container.pack(expand=True, fill='both')

    def clear_container():
        for widget in container.winfo_children():
            widget.destroy()

    # ---------- SIGN IN SCREEN ----------
    def show_signin():
        nonlocal user_data
        clear_container()
        
        # Header
        header = tk.Label(
            container,
            text="🎓 ClassHub",
            bg=styles_data["BG_DARK"],
            fg=styles_data["ACCENT"],
            font=("Segoe UI", 32, "bold")
        )
        header.pack(pady=(40, 5))
        
        subtitle = tk.Label(
            container,
            text="Welcome Back!",
            bg=styles_data["BG_DARK"],
            fg=styles_data["TEXT_SECONDARY"],
            font=("Segoe UI", 14)
        )
        subtitle.pack(pady=(0, 30))
        
        # Email
        email_label = tk.Label(
            container,
            text="Email Address",
            bg=styles_data["BG_DARK"],
            fg=styles_data["TEXT_PRIMARY"],
            font=("Segoe UI", 10, "bold"),
            anchor='w'
        )
        email_label.pack(padx=50, fill='x', pady=(0, 5))
        
        email_entry = tk.Entry(
            container,
            textvariable=signin_email_var,
            bg=styles_data["BG_MEDIUM"],
            fg=styles_data["TEXT_PRIMARY"],
            insertbackground=styles_data["TEXT_PRIMARY"],
            relief="flat",
            font=("Segoe UI", 11),
            highlightthickness=1,
            highlightcolor=styles_data["ACCENT"],
            highlightbackground="#3a3a3a"
        )
        email_entry.pack(padx=50, fill='x', ipady=8, pady=(0, 15))
        
        # Password
        password_label = tk.Label(
            container,
            text="Password",
            bg=styles_data["BG_DARK"],
            fg=styles_data["TEXT_PRIMARY"],
            font=("Segoe UI", 10, "bold"),
            anchor='w'
        )
        password_label.pack(padx=50, fill='x', pady=(0, 5))
        
        password_entry = tk.Entry(
            container,
            textvariable=signin_password_var,
            bg=styles_data["BG_MEDIUM"],
            fg=styles_data["TEXT_PRIMARY"],
            insertbackground=styles_data["TEXT_PRIMARY"],
            relief="flat",
            show="●",
            font=("Segoe UI", 11),
            highlightthickness=1,
            highlightcolor=styles_data["ACCENT"],
            highlightbackground="#3a3a3a"
        )
        password_entry.pack(padx=50, fill='x', ipady=8, pady=(0, 25))
        
        # Sign In Button
        def handle_signin():
            nonlocal user_data
            email = signin_email_var.get().strip()
            password = signin_password_var.get().strip()
            
            if not email or not password:
                messagebox.showerror("Error", "Please fill in all fields.")
                return
            
            if not email.endswith("@sch.gr"):
                messagebox.showerror("Email must be from school web (@sch.gr)")

            user_data = {
                "action": "signin",
                "email": email,
                "password": password
            }
            root.destroy()
        
        signin_btn = tk.Button(
            container,
            text="Sign In",
            command=handle_signin,
            bg=styles_data["ACCENT"],
            fg=styles_data["TEXT_PRIMARY"],
            activebackground=styles_data.get("ACCENT_DARK", "#2f5fd1"),
            activeforeground=styles_data["TEXT_PRIMARY"],
            relief="flat",
            font=("Segoe UI", 12, "bold"),
            cursor="hand2"
        )
        signin_btn.pack(padx=50, fill='x', ipady=10, pady=(0, 20))
        
        # Divider
        divider_frame = tk.Frame(container, bg=styles_data["BG_DARK"])
        divider_frame.pack(fill='x', padx=50, pady=(0, 20))
        
        tk.Frame(divider_frame, bg="#3a3a3a", height=1).pack(side='left', fill='x', expand=True, padx=(0, 10))
        tk.Label(divider_frame, text="OR", font=("Segoe UI", 9), fg="#7a7a7a", bg=styles_data["BG_DARK"]).pack(side='left')
        tk.Frame(divider_frame, bg="#3a3a3a", height=1).pack(side='left', fill='x', expand=True, padx=(10, 0))
        
        # Sign Up Link
        signup_text = tk.Label(
            container,
            text="Don't have an account?",
            bg=styles_data["BG_DARK"],
            fg=styles_data["TEXT_SECONDARY"],
            font=("Segoe UI", 10)
        )
        signup_text.pack()
        
        signup_link = tk.Label(
            container,
            text="Sign Up",
            bg=styles_data["BG_DARK"],
            fg=styles_data["ACCENT"],
            font=("Segoe UI", 11, "bold"),
            cursor="hand2"
        )
        signup_link.pack(pady=(5, 0))
        signup_link.bind("<Button-1>", lambda e: show_signup())

    # ---------- SIGN UP SCREEN ----------
    def show_signup():
        nonlocal user_data
        clear_container()
        
        # Header
        header = tk.Label(
            container,
            text="🎓 ClassHub",
            bg=styles_data["BG_DARK"],
            fg=styles_data["ACCENT"],
            font=("Segoe UI", 32, "bold")
        )
        header.pack(pady=(30, 5))
        
        subtitle = tk.Label(
            container,
            text="Create Account",
            bg=styles_data["BG_DARK"],
            fg=styles_data["TEXT_SECONDARY"],
            font=("Segoe UI", 14)
        )
        subtitle.pack(pady=(0, 20))
        
        # Full Name
        name_label = tk.Label(
            container,
            text="Full Name",
            bg=styles_data["BG_DARK"],
            fg=styles_data["TEXT_PRIMARY"],
            font=("Segoe UI", 10, "bold"),
            anchor='w'
        )
        name_label.pack(padx=50, fill='x', pady=(0, 5))
        
        name_entry = tk.Entry(
            container,
            textvariable=signup_name_var,
            bg=styles_data["BG_MEDIUM"],
            fg=styles_data["TEXT_PRIMARY"],
            insertbackground=styles_data["TEXT_PRIMARY"],
            relief="flat",
            font=("Segoe UI", 11),
            highlightthickness=1,
            highlightcolor=styles_data["ACCENT"],
            highlightbackground="#3a3a3a"
        )
        name_entry.pack(padx=50, fill='x', ipady=8, pady=(0, 12))
        
        # Email
        email_label = tk.Label(
            container,
            text="Email Address (@sch.gr)",
            bg=styles_data["BG_DARK"],
            fg=styles_data["TEXT_PRIMARY"],
            font=("Segoe UI", 10, "bold"),
            anchor='w'
        )
        email_label.pack(padx=50, fill='x', pady=(0, 5))
        
        email_entry = tk.Entry(
            container,
            textvariable=signup_email_var,
            bg=styles_data["BG_MEDIUM"],
            fg=styles_data["TEXT_PRIMARY"],
            insertbackground=styles_data["TEXT_PRIMARY"],
            relief="flat",
            font=("Segoe UI", 11),
            highlightthickness=1,
            highlightcolor=styles_data["ACCENT"],
            highlightbackground="#3a3a3a"
        )
        email_entry.pack(padx=50, fill='x', ipady=8, pady=(0, 12))
        
        # Password
        password_label = tk.Label(
            container,
            text="Password",
            bg=styles_data["BG_DARK"],
            fg=styles_data["TEXT_PRIMARY"],
            font=("Segoe UI", 10, "bold"),
            anchor='w'
        )
        password_label.pack(padx=50, fill='x', pady=(0, 5))
        
        password_entry = tk.Entry(
            container,
            textvariable=signup_password_var,
            bg=styles_data["BG_MEDIUM"],
            fg=styles_data["TEXT_PRIMARY"],
            insertbackground=styles_data["TEXT_PRIMARY"],
            relief="flat",
            show="●",
            font=("Segoe UI", 11),
            highlightthickness=1,
            highlightcolor=styles_data["ACCENT"],
            highlightbackground="#3a3a3a"
        )
        password_entry.pack(padx=50, fill='x', ipady=8, pady=(0, 12))
        
        # Confirm Password
        confirm_label = tk.Label(
            container,
            text="Confirm Password",
            bg=styles_data["BG_DARK"],
            fg=styles_data["TEXT_PRIMARY"],
            font=("Segoe UI", 10, "bold"),
            anchor='w'
        )
        confirm_label.pack(padx=50, fill='x', pady=(0, 5))
        
        confirm_entry = tk.Entry(
            container,
            textvariable=signup_confirm_var,
            bg=styles_data["BG_MEDIUM"],
            fg=styles_data["TEXT_PRIMARY"],
            insertbackground=styles_data["TEXT_PRIMARY"],
            relief="flat",
            show="●",
            font=("Segoe UI", 11),
            highlightthickness=1,
            highlightcolor=styles_data["ACCENT"],
            highlightbackground="#3a3a3a"
        )
        confirm_entry.pack(padx=50, fill='x', ipady=8, pady=(0, 20))
        
        # Sign Up Button
        def handle_signup():
            nonlocal user_data
            name = signup_name_var.get().strip()
            email = signup_email_var.get().strip()
            password = signup_password_var.get().strip()
            confirm = signup_confirm_var.get().strip()
            
            if not name or not email or not password or not confirm:
                messagebox.showerror("Error", "Please fill in all fields.")
                return
            
            if password != confirm:
                messagebox.showerror("Error", "Passwords don't match!")
                return
            
            if not email.endswith("@sch.gr"):
                messagebox.showerror("Error", "Email must end with @sch.gr")
                return
            
            user_data = {
                "action": "signup",
                "name": name,
                "email": email,
                "password": password
            }
            root.destroy()
        
        signup_btn = tk.Button(
            container,
            text="Sign Up",
            command=handle_signup,
            bg=styles_data["ACCENT"],
            fg=styles_data["TEXT_PRIMARY"],
            activebackground=styles_data.get("ACCENT_DARK", "#2f5fd1"),
            activeforeground=styles_data["TEXT_PRIMARY"],
            relief="flat",
            font=("Segoe UI", 12, "bold"),
            cursor="hand2"
        )
        signup_btn.pack(padx=50, fill='x', ipady=10, pady=(0, 15))
        
        signin_text = tk.Label(
            container,
            text="Already have an account?",
            bg=styles_data["BG_DARK"],
            fg=styles_data["TEXT_SECONDARY"],
            font=("Segoe UI", 10)
        )
        signin_text.pack()
        
        signin_link = tk.Label(
            container,
            text="Sign In",
            bg=styles_data["BG_DARK"],
            fg=styles_data["ACCENT"],
            font=("Segoe UI", 11, "bold"),
            cursor="hand2"
        )
        signin_link.pack(pady=(5, 0))
        signin_link.bind("<Button-1>", lambda e: show_signin())

    show_signin()
    
    root.mainloop()
    
    return user_data