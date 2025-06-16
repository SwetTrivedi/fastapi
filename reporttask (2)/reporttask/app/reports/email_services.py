# email_service.py

def send_email_with_link(email: str, filename: str):
    download_url = f"http://localhost:9000/reports/{filename}"
    print(f"Sending email to {email} with report link: {download_url}")
    # In real app: integrate with SMTP or services like SendGrid/Mailgun