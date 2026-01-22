import tkinter as tk
from tkinter import messagebox
import email_management
import ui_storage
import os
import json
import pyrebase
from dotenv import load_dotenv
load_dotenv()

# Load Firebase config from environment variables
config = {
    "apiKey": os.environ.get('FIREBASE_API_KEY'),
    "authDomain": os.environ.get('FIREBASE_AUTH_DOMAIN'),
    "databaseURL": os.environ.get('FIREBASE_DATABASE_URL'),
    "storageBucket": os.environ.get('FIREBASE_STORAGE_BUCKET')
}

# Validate that all required environment variables are set
required_vars = ['FIREBASE_API_KEY', 'FIREBASE_AUTH_DOMAIN', 'FIREBASE_DATABASE_URL', 'FIREBASE_STORAGE_BUCKET']
missing_vars = [var for var in required_vars if not os.environ.get(var)]

if missing_vars:
    messagebox.showerror(
        "Configuration Error",
        f"Missing environment variables: {', '.join(missing_vars)}\n\n"
        "Please set them before running the application."
    )
    os._exit(0)

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db = firebase.database()

def quit_script(msg: str):
    messagebox.showerror("Error", msg)
    os._exit(0)

def reopen_auth(msg: str):
    messagebox.showinfo("Invalid", msg)
    ui_storage.auth_ui()

auth_data = ui_storage.auth_ui()
if not auth_data:
    quit_script("Authentication Canceled.")

email = auth_data["email"]
password = auth_data["password"]
action = auth_data["action"]
name = auth_data.get("name", "")

"""
if action == "signup":
    try:
        users = db.child("users").get()
        if users.val():
            for user_id, user_data in users.val().items():
                if user_data.get("email") == email:
                    reopen_auth("This email is already registered. Please sign in instead.")
    except Exception as e:
        print(f"Database check error: {e}")

try:
    #result = email_management.send_validation_email(email, action == "signup")
    if not result:
        messagebox.showwarning(
            "Too Many Requests", 
            "Please wait before requesting another verification code.\n\n"
            "You can request a new code in 60 seconds."
        )
        quit_script("Rate limited. Please try again later.")

    entered_code = ui_storage.verification_code_ui()
    if not entered_code:
        quit_script("Verification cancelled.")

    if not email_management.verify_code(email, entered_code):
        quit_script("Invalid or expired verification code!")

    if action == "signup":
        user = auth.create_user_with_email_and_password(email, password)
        user_id = user['localId']
        
        db.child("users").child(user_id).set({
            "name": name,
            "email": email,
            "role": "student",
            "created_at": str(db.generate_key())
        })
        
        messagebox.showinfo("Success", f"Account created for {name}!")
        print(f"New user created: {user_id}")
        
    elif action == "signin":
        user = auth.sign_in_with_email_and_password(email, password)
        user_id = user['localId']
        
        messagebox.showinfo("Success", "Signed in successfully!")
        print(f"User signed in: {user_id}")

except Exception as e:
    try:
        error_json = json.loads(e.args[1])
        error_message = error_json["error"]["message"]

        if error_message == "EMAIL_EXISTS":
            quit_script("Email already exists. Please sign in instead.")
        elif error_message == "INVALID_EMAIL":
            quit_script("Invalid email format.")
        elif error_message == "WEAK_PASSWORD":
            quit_script("Password should be at least 6 characters.")
        elif error_message == "EMAIL_NOT_FOUND":
            quit_script("No account found with this email. Please sign up first.")
        elif error_message == "INVALID_PASSWORD":
            quit_script("Incorrect password. Please try again.")
        else:
            quit_script(f"Firebase error: {error_message}")

    except Exception:
        quit_script(f"Authentication failed: {str(e)}")
"""

main_ui = ui_storage.main_ui()
main_ui.root.mainloop()