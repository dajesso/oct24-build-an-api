from flask import Blueprint
from init import db
from models.student import Student
student_bp = Blueprint('students', __name__)

# Read all -GET /students

@student_bp.route('/students')
def get_all_students():
    stmt = db.session(Student)
    students = db.session.scalar(stmt)
    return students.dump(stmt)


# Read one - get /students/<int:id>
# Create - post /students
# Update -  post /students/<int:id>
# Delete - delete /students/<int:id>
# possible extra routes
# Unenrol - DELETE /students/<int:student_id>/<int:course_id>
# Enrol - POST /students/<int:student_id><int:course_id>