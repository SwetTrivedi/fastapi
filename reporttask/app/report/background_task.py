# background_tasks.py
import csv
import os
from datetime import datetime
from database import get_db
from models import Report, User
from sqlalchemy.orm import Session
from report.weather_services import get_weather_data
from report.email_services import send_email_async #send_email_with_link

REPORT_DIR = "reports"


def generate_report_task(report_id: int, user_id: int):
    db: Session = next(get_db())

    report = db.query(Report).filter(Report.id == report_id).first()
    user = db.query(User).filter(User.id == user_id).first()
    if not report or not user:
        return

    filename = f"report_{report_id}_{datetime.utcnow().strftime('%Y%m%d%H%M%S')}.csv"
    filepath = os.path.join(REPORT_DIR, filename)

    # Get weather data
    weather_data = get_weather_data()

    # Generate CSV
    with open(filepath, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Report ID", "User", "Status", "Weather", "Created At"])
        writer.writerow([
            report.id,
            user.username,
            "Completed",
            weather_data,
            datetime.utcnow().isoformat()
        ])

    # Update DB
    report.status = "Completed"
    report.file_path = filename
    db.commit()



    # send_email_async(user.email, filename)
    # async def send_email_async(subject: str, recipient: str, body: str):
from report.email_services import send_email_async  # ya jo relative path ho

async def generate_report_task(user, data):
        # ... report file bana rahe ho yahan
    filename = f"report_{user.id}_20250611.csv"
        
        # Email bhejna after file ready
    await send_email_async(
        recipient=user.email,
        subject="Your Report is Ready",
        # body=f"Hi {user.username},\n\nYour report '{filename}' is ready.\nPlease check your dashboard.\n\nRegards,\nTeam"
        )



