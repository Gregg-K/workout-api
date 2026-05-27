from app import ma
from models import Exercise, Workout, WorkoutExercise

class ExerciseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Exercise


class WorkoutSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Workout


class WorkoutExerciseSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = WorkoutExercise