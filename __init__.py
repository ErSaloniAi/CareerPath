from flask import Flask
from app.config.settings import Config
from app.extensions.db import db, mail   # ✅ use ONLY this db

def create_app():
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object(Config)
    app.config['SECRET_KEY'] = 'dev-key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///campusxhire.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # ✅ Initialize extensions
    db.init_app(app)
    mail.init_app(app)

    # ✅ Register blueprints
    from app.routes.auth import auth_bp
    from app.routes.home import home_bp
    from app.routes.company import company_bp
    from app.routes.student import student_bp
    from app.routes.resume import resume_bp
    from app.routes.video_resume import video_resume_bp
    from app.routes.portfolio import portfolio_bp
    from app.routes.job import job_bp

    app.register_blueprint(portfolio_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(home_bp)
    app.register_blueprint(student_bp)
    app.register_blueprint(company_bp)
    app.register_blueprint(resume_bp)
    app.register_blueprint(video_resume_bp)
    app.register_blueprint(job_bp)

    # ✅ Create tables
    with app.app_context():
        db.create_all()

    return app
