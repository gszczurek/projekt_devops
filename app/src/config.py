import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        "postgresql://postgres:root123@localhost:5432/app_db"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
