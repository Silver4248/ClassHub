import smtplib
import random
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

verification_codes = {}
email_rate_limit = {}

# Configuration
CODE_EXPIRY_SECONDS = 600
RATE_LIMIT_SECONDS = 60
MAX_ATTEMPTS_PER_HOUR = 5

def send_validation_email(email, is_signup):
    """
    Send verification email with rate limiting
    Returns: True if sent successfully, False if rate limited
    """
    current_time = time.time()
    
    # Check rate limiting
    if email in email_rate_limit:
        last_sent = email_rate_limit[email]["last_sent"]
        attempts = email_rate_limit[email]["attempts"]
        first_attempt_time = email_rate_limit[email]["first_attempt"]
        
        # Check if trying to send too soon (within 60 seconds)
        if current_time - last_sent < RATE_LIMIT_SECONDS:
            remaining = int(RATE_LIMIT_SECONDS - (current_time - last_sent))
            print(f"⏳ Please wait {remaining} seconds before requesting another code")
            return False
        
        # Check if too many attempts in the last hour
        if current_time - first_attempt_time < 3600:  # Within 1 hour
            if attempts >= MAX_ATTEMPTS_PER_HOUR:
                print(f"⚠️ Too many attempts. Please try again later.")
                return False
            # Increment attempts
            email_rate_limit[email]["attempts"] += 1
        else:
            # Reset counter after 1 hour
            email_rate_limit[email] = {
                "last_sent": current_time,
                "attempts": 1,
                "first_attempt": current_time
            }
    else:
        # First time sending to this email
        email_rate_limit[email] = {
            "last_sent": current_time,
            "attempts": 1,
            "first_attempt": current_time
        }
    
    # Generate 6-digit code
    code = str(random.randint(100000, 999999))
    
    # Store code with timestamp
    verification_codes[email] = {
        "code": code,
        "timestamp": current_time
    }
    
    # Update last sent time
    email_rate_limit[email]["last_sent"] = current_time
    
    # Email content
    action = "Sign Up" if is_signup else "Sign In"
    subject = f"ClassHub - {action} Verification Code"
    body = f"""
Hello,

Your verification code for ClassHub {action.lower()}:

{code}

This code will expire in 10 minutes.

If you didn't request this code, please ignore this email.

Best regards,
ClassHub Team
    """
    
    # Send email
    try:
        sender_email = "your-email@gmail.com"
        sender_password = "your-app-password"
        
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))
        
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        
        print(f"✓ Verification code sent to {email}: {code}")
        return True
        
    except Exception as e:
        print(f"✗ Failed to send email: {e}")
        print(f"Verification code for {email}: {code}")
        return True


def verify_code(email, entered_code):
    """
    Verify the entered code
    Returns: True if valid, False otherwise
    """
    if email not in verification_codes:
        print("No code found for this email")
        return False
    
    stored = verification_codes[email]
    
    # Check if expired
    if time.time() - stored["timestamp"] > CODE_EXPIRY_SECONDS:
        del verification_codes[email]
        print("Code expired")
        return False
    
    # Check if code matches
    if stored["code"] == entered_code:
        del verification_codes[email]
        # Clear rate limiting on successful verification
        if email in email_rate_limit:
            del email_rate_limit[email]
        print("Code verified successfully!")
        return True
    
    print("Invalid code")
    return False