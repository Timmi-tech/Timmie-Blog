from django.conf import settings
from django.core.mail import send_mail

def send_account_activation_email(email, email_token):
    subject = f"Your account needs to be verified"
    message = f"Hi, click on the link to activate your accounthttp://127.0.0.1:8000/activate/{email_token}"
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list )
    return True