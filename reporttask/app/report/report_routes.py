# report_routes.py
from fastapi import APIRouter, Depends, BackgroundTasks, HTTPException, Query
from sqlalchemy.orm import Session
from database import get_db
from models import Report, User
from schemas import ReportOut
from auth.auth_handler import get_current_user# get_current_active_admin
from report.background_task import generate_report_task
from typing import List
import os

router = APIRouter()

REPORT_DIR = "reports"
os.makedirs(REPORT_DIR, exist_ok=True)

@router.post("/reports/request")
def request_report(background_tasks: BackgroundTasks, current_user: User = Depends(get_current_user), db: Session = Depends(get_db)):
    new_report = Report(user_id=current_user.id, status="Pending")
    db.add(new_report)
    db.commit()
    db.refresh(new_report)

    background_tasks.add_task(generate_report_task, new_report.id, current_user.id)

    return {"msg": "Report generation started", "report_id": new_report.id}

@router.get("/reports", response_model=List[ReportOut])
def list_reports(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
    skip: int = 0,
    limit: int = Query(10, le=50)
):
    if current_user.role == "admin":
        reports = db.query(Report).offset(skip).limit(limit).all()
    else:
        reports = db.query(Report).filter(Report.user_id == current_user.id).offset(skip).limit(limit).all()
    return reports

@router.get("/reports/download/{report_id}")
def download_report(report_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    report = db.query(Report).filter(Report.id == report_id).first()
    if not report:
        raise HTTPException(status_code=404, detail="Report not found")

    if report.user_id != current_user.id and current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Access denied")

    if report.status != "Completed" or not report.file_path:
        raise HTTPException(status_code=400, detail="Report is not ready")

    file_path = os.path.join(REPORT_DIR, report.file_path)
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    return {"download_url": f"/static/reports/{report.file_path}"}


