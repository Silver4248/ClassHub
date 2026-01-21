import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import random
import time

verification_codes = {}

def send_validation_email(email, is_signup):
    code = str(random.randint(100000, 999999))
    
    verification_codes[email] = {
        "code": code,
        "timestamp": time.time()
    }
    
    action = "Sign Up" if is_signup else "Sign In"
    
    message = Mail(
        from_email='noreply@classhub.app',  # Can be any email
        to_emails=email,
        subject=f'ClassHub - {action} Verification Code',
        html_content=f'''
        <div style="font-family: Arial, sans-serif; padding: 20px;">
            <h2>🎓 ClassHub Verification</h2>
            <p>Your verification code is:</p>
            <h1 style="color: #3a7afe; letter-spacing: 5px;">{code}</h1>
            <p>This code expires in 10 minutes.</p>
            <p style="color: #999; font-size: 12px;">If you didn't request this, ignore this email.</p>
        </div>
        '''
    )
    
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))  # Store in env variable
        response = sg.send(message)
        print(f"✓ Email sent! Status: {response.status_code}")
        return True
    except Exception as e:
        print(f"✗ SendGrid error: {e}")
        return False