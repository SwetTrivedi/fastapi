# background_tasks.py
import csv
import os
from datetime import datetime
from database import get_db
from models import Report, User
from sqlalchemy.orm import Session
from reports.weather_services import get_weather_data
from reports.email_services import send_email_with_link

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

    # Send email
    # email_services.py
from reports.report_utils import send_email_async  # wherever you keep async function

async def send_email_with_link(email: str, filename: str):
    download_url = f"http://localhost:9000/reports/{filename}"
    subject = "Your Weather Report is Ready"
    body = f"Hi,\n\nYour report is ready. You can download it from the link below:\n{download_url}\n\nRegards,\nTeam"
    await send_email_async(email, subject, body)

