import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import random
import time
from dotenv import load_dotenv
load_dotenv()

verification_codes = {}

def send_validation_email(email, is_signup):
    code = str(random.randint(100000, 999999))
    
    verification_codes[email] = {
        "code": code,
        "timestamp": time.time()
    }
    
    action = "Sign Up" if is_signup else "Sign In"
    
    # Create message
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f'ClassHub - {action} Verification Code'
    msg['From'] = 'noreply@classhub.app'
    msg['To'] = email
    
    # HTML content
    html = f'''
    <div style="font-family: Arial, sans-serif; padding: 20px;">
        <h2>🎓 ClassHub Verification</h2>
        <p>Your verification code is:</p>
        <h1 style="color: #3a7afe; letter-spacing: 5px;">{code}</h1>
        <p>This code expires in 10 minutes.</p>
        <p style="color: #999; font-size: 12px;">If you didn't request this, ignore this email.</p>
    </div>
    '''
    
    # Attach HTML content
    html_part = MIMEText(html, 'html')
    msg.attach(html_part)
    
    try:
        # Send via localhost SMTP server
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login(os.environ.get('EMAIL_USER'), os.environ.get('EMAIL_PASSWORD'))
        s.send_message(msg)
        s.quit()
        print(f"✓ Email sent to {email}")
        return True
    except Exception as e:
        print(f"✗ SMTP error: {e}")
        return False

def verify_code(email, entered_code):
    if email not in verification_codes:
        return False
    
    stored_data = verification_codes[email]
    
    # Check if code expired (10 minutes = 600 seconds)
    if time.time() - stored_data["timestamp"] > 600:
        del verification_codes[email]
        return False
    
    # Check if code matches
    if stored_data["code"] == entered_code:
        del verification_codes[email]  # Remove after successful verification
        return True
    
    return False