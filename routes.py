from flask import request, jsonify
from app import app, db
from models import Exercise, Workout, WorkoutExercise
from schemas import ExerciseSchema, WorkoutSchema, WorkoutExerciseSchema

exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

wx_schema = WorkoutExerciseSchema()
wx_many_schema = WorkoutExerciseSchema(many=True)

@app.route("/exercises", methods=["POST"])
def create_exercise():
    data = request.json
    ex = Exercise(**data)

    db.session.add(ex)
    db.session.commit()

    return exercise_schema.jsonify(ex)


@app.route("/exercises", methods=["GET"])
def get_exercises():
    return exercises_schema.jsonify(Exercise.query.all())

@app.route("/workouts", methods=["POST"])
def create_workout():
    data = request.json
    w = Workout(**data)

    db.session.add(w)
    db.session.commit()

    return workout_schema.jsonify(w)


@app.route("/workouts", methods=["GET"])
def get_workouts():
    return workouts_schema.jsonify(Workout.query.all())

@app.route("/workout-exercises", methods=["POST"])
def add_exercise():
    data = request.json

    wx = WorkoutExercise(
        workout_id=data["workout_id"],
        exercise_id=data["exercise_id"],
        sets=data.get("sets"),
        reps=data.get("reps"),
        duration=data.get("duration")
    )

    db.session.add(wx)
    db.session.commit()

    return wx_schema.jsonify(wx)