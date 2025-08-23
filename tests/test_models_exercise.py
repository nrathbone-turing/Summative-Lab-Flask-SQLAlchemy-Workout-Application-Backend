import pytest
from server.models import db, Exercise

def test_create_exercise_minimal():
    ex = Exercise(name="Squat", category="Strength", equipment_needed=True)
    db.session.add(ex)
    db.session.commit()
    assert ex.id is not None
    assert ex.name == "Squat"
    assert ex.category == "Strength"
    assert ex.equipment_needed is True

def test_exercise_name_and_category_required_validation():
    bad = Exercise(name="   ", category="   ", equipment_needed=False)
    db.session.add(bad)
    with pytest.raises(Exception):
        db.session.commit()   # Expect @validates to raise (ValueError => flush fail)

def test_exercise_unique_name_category_constraint():
    a = Exercise(name="Push-Up", category="Bodyweight", equipment_needed=False)
    b = Exercise(name="Push-Up", category="Bodyweight", equipment_needed=False)
    db.session.add_all([a, b])
    with pytest.raises(Exception):
        db.session.commit()   # Expect UniqueConstraint to fail