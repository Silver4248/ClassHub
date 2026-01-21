import tkinter as tk
from tkinter import messagebox
import email_management
import ui_storage
import os
import json
import sys
import pyrebase

config = {
    "apiKey": "AIzaSyBz0a6HXlY0Fl27PrNiOa1bEMkzWSb6ZVs",
    "authDomain": "eduhub-16ced.firebaseapp.com",
    "databaseURL": "https://eduhub-16ced-default-rtdb.europe-west1.firebasedatabase.app",
    "storageBucket": "eduhub-16ced.firebasestorage.app"
}

firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

styles_data = None
with open(os.path.join(os.path.dirname(__file__), "styles.json"), "r") as file:
    styles_data = json.load(file)

auth_data = ui_storage.auth_ui()
if not auth_data:
    sys.exit("Authentication cancelled.")

secret_code = email_management.send_validation_email(auth_data["email"], auth_data["action"] == "signup")

if not secret_code:
    messagebox.showerror("Error", "Failed to send verification email.")
    sys.exit("Email sending failed.")

# Step 3: Show verification code UI
entered_code = ui_storage.verification_code_ui()
if not entered_code:
    sys.exit("Verification cancelled.")

# Step 4: Verify the code (you need to implement this in email_management)
if not entered_code == secret_code:
    sys.exit("Code isn't correct.")


# Step 5: Create/Sign in user in Firebase
try:
    if auth_data["action"] == "signup":
        # Create new user
        user = auth.create_user_with_email_and_password(auth_data["email"], auth_data["password"])
        messagebox.showinfo("Success", f"Account created for {auth_data['name']}!")
        print(f"User signed up: {user['localId']}")
        
    elif auth_data["action"] == "signin":
        # Sign in existing user
        user = auth.sign_in_with_email_and_password(auth_data["email"], auth_data["password"])
        messagebox.showinfo("Success", "Signed in successfully!")
        print(f"User signed in: {user['localId']}")
        
except Exception as e:
    messagebox.showerror("Firebase Error", f"Authentication failed: {str(e)}")
    sys.exit("Firebase auth failed.")

# Continue with your app...
print("Authentication successful! Starting main app...")