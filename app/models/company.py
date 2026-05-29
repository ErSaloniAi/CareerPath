from app.extensions import db
from werkzeug.security import generate_password_hash, check_password_hash

# ================= COMPANY MODEL =================
class Company(db.Model):
    __tablename__ = "companies" 
    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(200), nullable=False)
    hr_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile_no = db.Column(db.String(10), nullable=False)
    industry_type = db.Column(db.String(100), nullable=False)
    website = db.Column(db.String(200))
    password = db.Column(db.String(200), nullable=False)
    is_verified = db.Column(db.Boolean, default=False)