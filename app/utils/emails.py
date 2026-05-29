from flask_mail import Message
from flask import render_template
from app.extensions import mail


def send_approval_email(student, job):

    msg = Message(
        subject=f"Congratulations! You're Selected for {job.title}",
        recipients=[student.email]
    )

    msg.html = render_template(
        "emails/application_approved.html",
        student=student,
        job=job
    )

    mail.send(msg)

def send_rejection_email(student, job):

    msg = Message(
        subject=f"Update on Your Application for {job.title}",
        recipients=[student.email]
    )

    msg.html = render_template(
        "emails/application_rejected.html",
        student=student,
        job=job
    )

    mail.send(msg)