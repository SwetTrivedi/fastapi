from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from auth.auth_routes import router as auth_router
from reports.report_routes import router as report_router
import os

app = FastAPI()

# Create static reports directory if not exists
os.makedirs("reports", exist_ok=True)
app.mount("/static/reports", StaticFiles(directory="reports"), name="reports")

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(report_router, tags=["Reports"])
