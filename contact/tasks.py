from celery import shared_task
from django.core.mail import send_mail
from django.conf import settings

@shared_task
def send_contact_email(name, email, message):
    subject = 'New Contact Message'
    body = f"You have received a new message from {name} ({email}):\n\n{message}"
    send_mail(
        subject,
        body,
        settings.DEFAULT_FROM_EMAIL,
        ['fahrultech@gmail.com'],  # Replace with your email
        fail_silently=False,
    )