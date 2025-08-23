"""
tMODELS:
- Exercise(id, name, category, equipment_needed)
- Workout(id, date, duration_minutes, notes)
- WorkoutExercise(id, workout_id, exercise_id, reps, sets, duration_seconds)


RELATIONSHIPS:
- WorkoutExercise belongs to Workout
- WorkoutExercise belongs to Exercise
- Workout has many WorkoutExercises
- Exercise has many WorkoutExercises
- Workout has many Exercises through WorkoutExercises
- Exercise has many Workouts through WorkoutExercises


VALIDATIONS (examples to consider later):
- name non-empty, category in allowed set
- duration_minutes >= 0
- reps/sets/duration_seconds >= 0


TABLE CONSTRAINTS (examples to consider later):
- Unique constraint on Exercise(name, category) to avoid dupes?
- Check constraints for non-negative integers
- Foreign keys with cascade or ON DELETE behavior (stretch)
"""
# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.orm import validates
# from sqlalchemy import CheckConstraint, UniqueConstraint
#
# db = SQLAlchemy()
#
# class Exercise(db.Model):
# # PSEUDOCODE: define columns, constraints, relationships to WorkoutExercise
# pass
#
# class Workout(db.Model):
# # PSEUDOCODE: define columns, constraints, relationships to WorkoutExercise
# pass
#
# class WorkoutExercise(db.Model):
# # PSEUDOCODE: define columns, FKs to Workout/Exercise, constraints
# # Relationship backrefs to Workout and Exercise
# pass

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates
db = SQLAlchemy()

# Define Models here