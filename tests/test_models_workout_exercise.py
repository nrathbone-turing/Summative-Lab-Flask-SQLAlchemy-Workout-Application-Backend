# test/test_models_workout_exercise.py
import pytest
from datetime import date
from sqlalchemy.exc import IntegrityError
from server.models import db, Workout, Exercise, WorkoutExercise


def test_create_workout_exercise_minimal(app_context):
    """
    Expected behavior:
    - a WorkoutExercise row links one Workout and one Exercise together
    - optional fields (reps, sets, duration_seconds) can be None
    """
    # first create a new Workout and a new Exercise
    workout = Workout(date=date(2025, 1, 1))
    exercise = Exercise(name="Lunges", category="Strength", equipment_needed=False)
    db.session.add_all([workout, exercise])
    db.session.commit()

    # then link them through a WorkoutExercise join row
    link = WorkoutExercise(workout_id=workout.id, exercise_id=exercise.id)
    db.session.add(link)
    db.session.commit()

    # assertions to test the ids and linkage and that the join row saved correctly
    assert link.id is not None
    assert link.workout_id == workout.id
    assert link.exercise_id == exercise.id


def test_workout_exercise_requires_foreign_keys(app_context):
    """
    Constraint path:
    - workout_id and exercise_id must be valid foreign keys
    - null or invalid foreign key values should raise IntegrityError
    """
    # attempt to create an invalid join (missing primary keys, so no values for `workout_id` or `exercise_id`)
    bad_link = WorkoutExercise(workout_id=None, exercise_id=None)
    db.session.add(bad_link)

    # expect IntegrityError when committing to db
    with pytest.raises(IntegrityError):
        db.session.commit()
    
    # roll back failed transaction so other tests don't break
    db.session.rollback()

def test_workout_exercise_relationships(app_context):
    """
    Relationship path:
    - a WorkoutExercise belongs to only unique pairing of one Workout and one Exercise
    - table relationships allow navigation both directions:
      * workout.exercises should include exercise
      * exercise.workouts should include workout
    """
    # create the base records for test
    workout = Workout(date=date(2025, 2, 1))
    pushups = Exercise(name="Pushups", category="Bodyweight", equipment_needed=False)
    db.session.add_all([workout, pushups])
    db.session.commit()

    # then create a join row linking the records with reps/sets
    link = WorkoutExercise(workout=workout, exercise=pushups, reps=10, sets=3)
    db.session.add(link)
    db.session.commit()

    # relationship assertions
    # the join row points back to its parent objects
    assert link.workout == workout
    assert link.exercise == pushups

    # each parent has the join row in its list of workout_exercises
    assert link in workout.workout_exercises
    assert link in pushups.workout_exercises

    # still able to reach across tables by iterating the join rows to follow the link manually
    assert pushups in [we.exercise for we in workout.workout_exercises]
    assert workout in [we.workout for we in pushups.workout_exercises]

def test_workout_exercise_nonnegative_validations(app_context):
    """
    Validation path:
    - reps, sets, and duration_seconds must be >= 0
    - negative values should raise ValueError from @validates
    """
    # create valid parent records for test
    workout = Workout(date=date(2025, 3, 1))
    exercise = Exercise(name="Running", category="Cardio", equipment_needed=False)
    db.session.add_all([workout, exercise])
    db.session.commit()

    # try to assign a negative reps count --> expect validation error
    with pytest.raises(ValueError, match="must be >= 0"):
        WorkoutExercise(workout=workout, exercise=exercise, reps=-5)