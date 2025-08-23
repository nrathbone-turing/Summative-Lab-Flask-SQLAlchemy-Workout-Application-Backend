"""
PSEUDOCODE EXERCISE ROUTES:
- GET /exercises --> list all exercises
- GET /exercises/<id> --> show exercise + associated workouts
- POST /exercises --> create a new exercise
- DELETE /exercises/<id> --> delete an exercise (stretch: also delete related joins)
- POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises → add join row
"""
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint, UniqueConstraint, ForeignKey
from sqlalchemy.orm import validates, relationship
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()

class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)           # validate non-empty
    category = db.Column(db.String, nullable=False)       # validate non-empty
    equipment_needed = db.Column(db.Boolean, nullable=False, default=False)

    # prevent obvious duplicates
    __table_args__ = (
        UniqueConstraint("name", "category", name="uq_exercise_name_category"),
    )
     
    workout_exercises = relationship(
        "WorkoutExercise",
        back_populates="exercise",
        cascade="all, delete-orphan"
    )
    workouts = association_proxy("workout_exercises", "workout")

    @validates("name", "category")
    def validate_non_empty(self, key, value):
        # model validation #1
        if not value or not str(value).strip():
            raise ValueError(f"{key} must be non-empty")
        return value

    def __repr__(self):
        return f"<Exercise id={self.id} name={self.name!r} category={self.category!r}>"

#
# @exercises_bp.get("/exercises")
# def list_exercises():
# # PSEUDOCODE: query all exercises; return serialized list
# pass
#
# @exercises_bp.get("/exercises/<int:exercise_id>")
# def get_exercise(exercise_id):
# # PSEUDOCODE: fetch one by id; include associated workouts
# pass
#
# @exercises_bp.post("/exercises")
# def create_exercise():
# # PSEUDOCODE: validate via ExerciseSchema; insert; return created
# pass
#
# @exercises_bp.delete("/exercises/<int:exercise_id>")
# def delete_exercise(exercise_id):
# # PSEUDOCODE: delete exercise
# pass
#
# @exercises_bp.post("/workouts/<int:workout_id>/exercises/<int:exercise_id>/workout_exercises")
# def add_workout_exercise(workout_id, exercise_id):
# # PSEUDOCODE: create WorkoutExercise with reps/sets/duration from JSON
# pass