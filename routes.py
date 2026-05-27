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