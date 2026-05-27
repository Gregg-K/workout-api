from app import app, db
from models import Exercise, Workout

with app.app_context():
    db.drop_all()
    db.create_all()

    db.session.add_all([
        Exercise(name="Push Ups", muscle_group="Chest"),
        Exercise(name="Squats", muscle_group="Legs"),
        Workout(title="Monday Workout")
    ])

    db.session.commit()