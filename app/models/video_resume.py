from app.extensions.db import db

from datetime import datetime


class VideoResume(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=False)
    video_filename = db.Column(db.String(255), nullable=False)
    visibility = db.Column(db.String(20), default="after_apply")  
    uploaded_at = db.Column(db.DateTime, default=datetime.utcnow)
