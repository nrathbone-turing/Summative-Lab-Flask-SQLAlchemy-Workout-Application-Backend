import pytest
from datetime import date
from sqlalchemy.exc import IntegrityError
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