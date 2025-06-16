import aiosmtplib
from email.message import EmailMessage
from config import SMTP_HOST, SMTP_PORT, SMTP_USER, SMTP_PASSWORD

async def send_email_async(to_email: str, subject: str, body: str):
    msg = EmailMessage()
    msg["From"] = SMTP_USER
    msg["To"] = to_email
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
