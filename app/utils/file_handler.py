import os
import uuid
from werkzeug.utils import secure_filename
from flask import current_app

ALLOWED_RESUME_EXT = {"pdf"}
ALLOWED_VIDEO_EXT = {"mp4", "webm", "mov"}

def save_file(file, folder):
    """
    Saves file in static/uploads/<folder>/
    Returns relative path for DB storage
    """

    if not file:
        return None

    filename = secure_filename(file.filename)
    ext = filename.rsplit(".", 1)[1].lower()

    # ---------------- VALIDATION ----------------
    if folder == "resumes" and ext not in ALLOWED_RESUME_EXT:
        raise ValueError("Only PDF resumes are allowed")

    if folder == "videos" and ext not in ALLOWED_VIDEO_EXT:
        raise ValueError("Only MP4 / WEBM / MOV videos are allowed")

    # ---------------- UNIQUE NAME ----------------
    unique_name = f"{uuid.uuid4().hex}.{ext}"

    upload_path = os.path.join(
        current_app.root_path,
        "static",
        "uploads",
        folder
    )

    os.makedirs(upload_path, exist_ok=True)

    file_path = os.path.join(upload_path, unique_name)
    file.save(file_path)

    # ---------------- DB PATH ----------------
    return f"uploads/{folder}/{unique_name}"
