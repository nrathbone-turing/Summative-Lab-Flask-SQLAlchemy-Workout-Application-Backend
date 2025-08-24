
# server/models.py
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import CheckConstraint, UniqueConstraint, ForeignKey
from sqlalchemy.orm import validates, relationship
db = SQLAlchemy()

class Exercise(db.Model):
    __tablename__ = "exercises"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)        # validated non-empty
    category = db.Column(db.String, nullable=False)    # validated non-empty
    equipment_needed = db.Column(db.Boolean, nullable=False, default=False)

    # backref to joins
    workout_exercises = relationship(
        "WorkoutExercise",
        back_populates="exercise",
        cascade="all, delete-orphan",
    )
    
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

    # backref to joins
    workout_exercises = relationship(
        "WorkoutExercise",
        back_populates="workout",
        cascade="all, delete-orphan",
    )

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

class WorkoutExercise(db.Model):
    __tablename__ = "workout_exercises"

    id = db.Column(db.Integer, primary_key=True)

    workout_id = db.Column(
        db.Integer,
        ForeignKey("workouts.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    exercise_id = db.Column(
        db.Integer,
        ForeignKey("exercises.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    # optional parameter validations
    reps = db.Column(db.Integer)
    sets = db.Column(db.Integer)
    duration_seconds = db.Column(db.Integer)

    # relationships back to parents
    workout = relationship("Workout", back_populates="workout_exercises")
    exercise = relationship("Exercise", back_populates="workout_exercises")

    __table_args__ = (
        # prevent duplicate (workout, exercise) pairs
        UniqueConstraint("workout_id", "exercise_id", name="uq_workout_exercise_pair"),
        # nonnegative checks (NULL allowed; when provided, must be >= 0)
        CheckConstraint("reps IS NULL OR reps >= 0", name="ck_we_reps_nonneg"),
        CheckConstraint("sets IS NULL OR sets >= 0", name="ck_we_sets_nonneg"),
        CheckConstraint(
            "duration_seconds IS NULL OR duration_seconds >= 0",
            name="ck_we_duration_secs_nonneg",
        ),
    )

    @validates("reps", "sets", "duration_seconds")
    def validate_nonneg(self, key, value):
        if value is None:
            return None
        try:
            iv = int(value)
        except (TypeError, ValueError):
            raise ValueError(f"{key} must be an integer >= 0")
        if iv < 0:
            raise ValueError(f"{key} must be >= 0")
        return iv