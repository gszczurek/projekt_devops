import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import csv
import json
import logging
from datetime import datetime
from db import db
from models import User
from flask import Flask


logging.basicConfig(
    filename='seed.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:root123@localhost:5432/app_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

sample_users = [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Charlie", "email": "charlie@example.com"},
    {"name": "David", "email": "david@example.com"},
    {"name": "Eve", "email": "eve@example.com"},
]

def seed():
    with app.app_context():
        for u in sample_users:
            user = User(name=u["name"], email=u["email"])
            db.session.add(user)
        db.session.commit()
        logging.info(f"Inserted {len(sample_users)} users into database.")

        with open('users.csv', 'w', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=["name", "email"])
            writer.writeheader()
            for u in sample_users:
                writer.writerow(u)
        logging.info("Saved users.csv")

        with open('users.json', 'w') as jsonfile:
            json.dump(sample_users, jsonfile, indent=4)
        logging.info("Saved users.json")

if __name__ == "__main__":
    seed()
    print("Seeding done. Files: users.csv, users.json, seed.log")
