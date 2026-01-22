import tkinter as tk
from tkinter import messagebox
import os
import json
import sys

styles_data = None
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    if hasattr(sys, '_MEIPASS'):
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    else:
        base_path = os.path.abspath(".")
    
    return os.path.join(base_path, relative_path)

try:
    with open(os.path.join(os.path.dirname(__file__), "styles.json"), "r") as file:
        styles_data = json.load(file)
    """
    This for the .exe

    with open(resource_path("styles.json"), "r") as file:
        styles_data = json.load(file)
    """
except (FileNotFoundError, ValueError):
    messagebox.showerror("File styles.json wasn't found, exiting.")
    os._exit(0)


def auth_ui():
    user_data = None
    
    root = tk.Tk()
    root.title("ClassHub - Authentication")
    root.geometry("450x600")
    root.resizable(False, False)
    root.configure(bg=styles_data["BG_DARK"])

    icon_path = resource_path(os.path.join("icons", "atlas.png"))

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

    container = tk.Frame(root, bg=styles_data["BG_DARK"])
    container.pack(expand=True, fill='both')

    def clear_container():
        for widget in container.winfo_children():
            widget.destroy()

    # ---------- SIGN IN SCREEN ----------
    def show_signin():
        nonlocal user_data
        clear_container()
        
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
        
        def handle_signin():
            nonlocal user_data
            email = signin_email_var.get().strip()
            password = signin_password_var.get().strip()
            
            if not email or not password:
                messagebox.showerror("Error", "Please fill in all fields.")
                return
            
            if not email.endswith("@sch.gr"):
                messagebox.showerror("Error", "Email must end with @sch.gr")
                return
            
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
            text="Nickname",
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
            
            if len(password) < 6:
                messagebox.showerror("Error", "Password must be at least 6 characters!")
                return
            if " " in password:
                messagebox.showerror("Error", "Password can't contain spaces")
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
        signup_btn.pack(padx=50, fill='x', ipady=10, pady=(0, 0))
        
        # Sign In Link
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


def verification_code_ui():
    """
    Shows verification code input UI
    Returns: the entered code or None if cancelled
    """
    code = None
    
    root = tk.Tk()
    root.title("Email Verification")
    root.geometry("400x250")
    root.resizable(False, False)
    root.configure(bg=styles_data["BG_DARK"])

    icon_path = resource_path(os.path.join("icons", "atlas.png"))

    try:
        icon = tk.PhotoImage(file=icon_path)
        root.iconphoto(True, icon)
    except:
        pass

    code_var = tk.StringVar()

    title = tk.Label(
        root,
        text="📧 Email Verification",
        bg=styles_data["BG_DARK"],
        fg=styles_data["TEXT_PRIMARY"],
        font=("Segoe UI", 16, "bold")
    )
    title.pack(pady=(30, 10))

    subtitle = tk.Label(
        root,
        text="Enter the verification code sent to your email",
        bg=styles_data["BG_DARK"],
        fg=styles_data["TEXT_SECONDARY"],
        font=("Segoe UI", 10)
    )
    subtitle.pack(pady=(0, 20))

    code_entry = tk.Entry(
        root,
        textvariable=code_var,
        width=20,
        bg=styles_data["BG_MEDIUM"],
        fg=styles_data["TEXT_PRIMARY"],
        insertbackground=styles_data["TEXT_PRIMARY"],
        relief="flat",
        font=("Segoe UI", 14, "bold"),
        justify='center',
        highlightthickness=1,
        highlightcolor=styles_data["ACCENT"],
        highlightbackground="#3a3a3a"
    )
    code_entry.pack(pady=10, ipady=10)
    code_entry.focus()

    def submit():
        nonlocal code
        entered_code = code_var.get().strip()
        if not entered_code:
            messagebox.showerror("Error", "Please enter the verification code.")
            return

        code = entered_code
        root.destroy()

    verify_btn = tk.Button(
        root,
        text="Verify Code",
        command=submit,
        bg=styles_data["ACCENT"],
        fg=styles_data["TEXT_PRIMARY"],
        activebackground=styles_data.get("ACCENT_DARK", "#2f5fd1"),
        activeforeground=styles_data["TEXT_PRIMARY"],
        relief="flat",
        font=("Segoe UI", 11, "bold"),
        padx=20,
        pady=10,
        cursor="hand2"
    )
    verify_btn.pack(pady=15)

    root.mainloop()
    
    return code

class main_ui():
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ClassHub")
        self.root.resizable(True, True)
        self.root.configure(bg=styles_data["BG_DARK"])
        self.root.state("zoomed")
        self.root.resizable(True, True)

        icon_path = resource_path(os.path.join("icons", "atlas.png"))

        try:
            icon = tk.PhotoImage(file=icon_path)
            self.root.iconphoto(True, icon)
        except:
            pass