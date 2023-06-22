from time import sleep
from django.core.mail import send_mail
from celery import shared_task
from celerytut.settings import EMAIL_HOST_USER

@shared_task()
def send_feedback_email_task(email_address, message):
    sleep(10)
    send_mail(
        "Your Feedback",
        f"\t{message}\n\nThank you!",
        EMAIL_HOST_USER,
        [email_address],
        fail_silently=False,
    )

