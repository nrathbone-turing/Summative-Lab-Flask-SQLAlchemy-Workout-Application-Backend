import pytest
from datetime import date
from sqlalchemy.exc import IntegrityError
from sqlalchemy import text
from server.models import db, Workout


def test_create_workout_minimal_defaults():
    """
   Expected behavior:
    - a Workout created with only a date should still save successfully since the other parameters are optional
    - duration_minutes should default to 0
    """
    w = Workout(date=date(2025, 1, 2))  # only required field

    db.session.add(w)
    db.session.commit()

    assert w.id is not None
    assert w.date == date(2025, 1, 2)
    assert w.duration_minutes == 0  # default value
    assert w.notes is None


def test_workout_duration_nonnegative_validation():
    """
    Validation path:
    - Workout.duration_minutes must be >= 0
    - negative values should raise a ValueError from @validates
    """
    with pytest.raises(ValueError, match="duration_minutes must be >= 0"):
        Workout(date=date(2025, 1, 3), duration_minutes=-10)


def test_workout_duration_check_constraint():
    """
    Constraint path:
    - database-level CheckConstraint enforces duration_minutes >= 0
    - trying to commit a negative value should raise an IntegrityError
    """
    bad = Workout(date=date(2025, 1, 4), duration_minutes=-1)
    db.session.add(bad)

    with pytest.raises(IntegrityError):
        db.session.commit()

def test_workout_duration_check_constraint():
    """
    Constraint path:
    - bypass model validation by issuing raw SQL
    - CheckConstraint should enforce duration_minutes >= 0 at the DB level
    """
    # Insert directly into DB without ORM validation
    insert_sql = text("INSERT INTO workouts (date, duration_minutes) VALUES (:date, :dur)")
    
    with pytest.raises(IntegrityError):
        db.session.execute(insert_sql, {"date": "2025-01-04", "dur": -1})
        db.session.commit()