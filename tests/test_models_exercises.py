# test/test_models_exercises.py
import pytest
from sqlalchemy.exc import IntegrityError
from server.models import db, Exercise


def test_create_exercise_minimal():
    """
    Expected behavior: Creating a valid Exercise with all required fields should save successfully and assign an id
    """
    ex = Exercise(name="Squat", category="Strength", equipment_needed=True)

    # Add to the session and commit to persist in db
    db.session.add(ex)
    db.session.commit()

    # After commit, id is auto-assigned and fields remain intact
    assert ex.id is not None
    assert ex.name == "Squat"
    assert ex.category == "Strength"
    assert ex.equipment_needed is True


def test_exercise_name_and_category_required_validation():
    """
    validation path: 
    - the @validates decorator on Exercise requires 'name' and 'category' to be non-empty strings
    - attempting to construct an Exercise with blank values should raise a ValueError immediately
    """
    with pytest.raises(ValueError, match="must be non-empty"):
        Exercise(name="   ", category="   ", equipment_needed=False)


def test_exercise_unique_name_category_constraint():
    """
    constraint path:
    - the table has a UNIQUE constraint on (name, category)
    - attempting to insert two Exercises with the same name+category pair should raise an IntegrityError when committing to the db
    """
    a = Exercise(name="Push-Up", category="Bodyweight", equipment_needed=False)
    b = Exercise(name="Push-Up", category="Bodyweight", equipment_needed=False)

    db.session.add_all([a, b])

    # Expect IntegrityError from the database on commit
    with pytest.raises(IntegrityError):
        db.session.commit()