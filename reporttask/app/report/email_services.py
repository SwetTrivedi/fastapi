# email_service.py

# def send_email_with_link(email: str, filename: str):
#     download_url = f"http://localhost:8000/reports/{filename}"
#     print(f"Sending email to {email} with report link: {download_url}")
#     # In real app: integrate with SMTP or services like SendGrid/Mailgun


import aiosmtplib
from email.message import EmailMessage
from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD

async def send_email_async(email: str, subject: str, body: str):
    msg = EmailMessage()
    msg["From"] = SMTP_USER
    msg["To"] = email
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        await aiosmtplib.send(
            msg,
            hostname=SMTP_HOST,
            port=SMTP_PORT,
            start_tls=True,
            username=SMTP_USER,
            password=SMTP_PASSWORD,
        )
        print("Email sent successfully.")
    except Exception as e:
        print("Error sending email:", e)