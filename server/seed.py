#!/usr/bin/env python3
"""
PSEUDOCODE SEED SCRIPT:
- Clears tables (respect FK constraints)
- Inserts small sample data for Exercises and Workouts
- Creates WorkoutExercise rows linking them
- Wrap in app.app_context()
"""
#!/usr/bin/env python3

from server.app import app
from server.models import db, Exercise, Workout

with app.app_context():
    # Clear out old data
    db.drop_all()
    db.create_all()

    # Create sample Exercises data
    pushups = Exercise(name="Push-ups", category="Strength")
    squats = Exercise(name="Squats", category="Strength")
    running = Exercise(name="Running", category="Cardio")

    # Create sample Workouts data
    workout1 = Workout(date="2025-08-23", duration_minutes=30)
    workout2 = Workout(date="2025-08-24", duration_minutes=45)

    # Add to session and commit
    db.session.add_all([pushups, squats, running, workout1, workout2])
    db.session.commit()

    print("Database seeded with example data!")