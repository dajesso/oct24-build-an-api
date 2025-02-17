from flask import Blueprint
from models.student import Student

from init import db

db_bp = Blueprint('db', __name__)

@db_bp.cli.command('init')
def create_tables():
    db.drop_all()
    db.create_all()
    print('Tables created')

@db_bp.cli.command('seed')

def seed_tables():
    students = [
        Student(
            name='Felicis Losose',
            email='felicis@gmail.com',
            address='Sydney'
        ),
        Student(
            name="Jessica Amy",
            email="jessica@amy.com"
        )
    ]

    db.session.add_all(students)
    db.session.commit()
    print('Table Seeded')

