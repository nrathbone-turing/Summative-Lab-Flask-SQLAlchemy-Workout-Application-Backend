"""
PSEUDOCODE SEED SCRIPT:
- Clears tables (respect FK constraints)
- Inserts small sample data for Exercises and Workouts
- Creates WorkoutExercise rows linking them
- Wrap in app.app_context()
"""
# from .app import app
# from .models import db
#
# with app.app_context():
# # PSEUDOCODE: db.drop_all() then db.create_all()
# # Create sample Exercises, Workouts, WorkoutExercises
# # db.session.add_all([...])
# # db.session.commit()
# pass

#!/usr/bin/env python3

from app import app
from models import *

with app.app_context():
    # reset data and add new example data, committing to db