from app.extensions.db import db

class Students(db.Model):
    __tablename__ = "students"

    id = db.Column(db.Integer, primary_key=True)

    full_name = db.Column(db.String(150), nullable=False)
    slug = db.Column(db.String(200), unique=True, nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)
    mobile_no = db.Column(db.String(15), nullable=False)
    start_year = db.Column(db.Integer, nullable=False) 
    end_year = db.Column(db.Integer, nullable=False)
    field = db.Column(db.String(100), nullable=False)
    specialization = db.Column(db.String(120))
    objective = db.Column(db.Text)
    password = db.Column(db.String(16), nullable=False)
    college_id = db.Column(db.Integer, nullable=False)
    github = db.Column(db.String(200))
    linkedin = db.Column(db.String(200))
    portfolio = db.Column(db.String(255))
    
    resume_file = db.Column(db.String(255))
    video_resume = db.Column(db.String(255))

    # New fields for semester and CGPA
    sem = db.Column(db.Integer)  # Current/Last semester
    cgpa = db.Column(db.Float)    # CGPA

    is_public = db.Column(db.Boolean, default=True)

    created_at = db.Column(db.DateTime, server_default=db.func.now())

    projects = db.relationship(
        "Projects",
        back_populates="student",
        cascade="all, delete-orphan"
    )
    skills = db.relationship(
    "Skills",
    back_populates="student",
    cascade="all, delete-orphan"
)

    
    certificate = db.relationship("certificate", backref="student", lazy=True)

    

    def __repr__(self):
        return f"<Student {self.full_name}>"
