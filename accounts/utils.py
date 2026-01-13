import random
from django.core.mail import send_mail
from django.conf import settings

def generate_otp():
    """Generate 6-digit OTP"""
    return str(random.randint(100000, 999999))

def send_otp_email(email, otp):
    """Send OTP to user's email"""
    subject = 'Password Reset OTP - Study Platform'
    message = f'''
    Hello,
    
    Your OTP for password reset is: {otp}
    
    This OTP is valid for 2 minutes only.
    
    If you didn't request this, please ignore this email.
    
    Thanks,
    Study Platform Team
    '''
    
    try:
        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [email],
            fail_silently=False,
        )
        return True
    except Exception as e:
        print(f"Email sending failed: {str(e)}")
        return False