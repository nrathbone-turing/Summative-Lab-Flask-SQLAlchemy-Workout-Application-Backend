
# server/models.py
"""
MODELS:
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
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint, UniqueConstraint
from sqlalchemy.orm import validates
db = SQLAlchemy()

# Define Models here

class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)        # validated non-empty
    category = db.Column(db.String, nullable=False)    # validated non-empty
    equipment_needed = db.Column(db.Boolean, nullable=False, default=False)

    __table_args__ = (
        # avoid obvious duplicates by (name, category)
        UniqueConstraint("name", "category", name="uq_exercise_name_category"),
    )

    @validates("name", "category")
    def validate_non_empty(self, key, value):
        if not value or not str(value).strip():
            raise ValueError(f"{key} must be non-empty")
        return value

    def __repr__(self):
        return f"<Exercise id={self.id} name={self.name!r} category={self.category!r}>"
    

class Workout(db.Model):
    __tablename__ = "workouts"

    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False, default=0)
    notes = db.Column(db.Text)

    __table_args__ = (
        CheckConstraint("duration_minutes >= 0", name="ck_workout_duration_nonneg"),
    )

    @validates("duration_minutes")
    def validate_duration(self, key, value):
        if value is None or int(value) < 0:
            raise ValueError("duration_minutes must be >= 0")
        return int(value)

    def __repr__(self):
        return f"<Workout id={self.id} date={self.date} duration={self.duration_minutes}m>"

# class WorkoutExercise(db.Model):
# # PSEUDOCODE: define columns, FKs to Workout/Exercise, constraints
# # Relationship backrefs to Workout and Exercise
# pass