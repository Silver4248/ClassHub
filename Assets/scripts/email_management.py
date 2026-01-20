import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import secrets

def send_validation_email(recipient_email: str, debug: bool):
    # Generate a random validation code
    validation_code = secrets.token_urlsafe(32)
    
    # Gmail credentials
    sender_email = "vibezman123@gmail.com"
    sender_password = "tdwb xcpj rlof fiwj"
    
    # Create message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = "Email Validation"
    
    body = f"""
    Hello,
    
    Please validate your email by entering the code at the app.

    Enter this code: {validation_code}
    
    Thanks!
    """
    
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        # Connect to Gmail SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.send_message(msg)
        server.quit()
        
        if debug == True:
            print(f"Validation email sent to {recipient_email}")
        return validation_code
    except Exception as e:
        if debug == True:
            print(f"Error sending email: {e}")
        return None