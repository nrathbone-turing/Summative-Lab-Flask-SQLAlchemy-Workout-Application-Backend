# Workout Application Backend (Flask + SQLAlchemy)

> Summative assessment project implementing a REST API with database persistence, validations, and schema-based serialization.

## Overview
- A workout tracking backend with:
- Flask REST API for CRUD management of workouts and exercises
- Join table (`WorkoutExercise`) to capture sets, reps, and duration
- Marshmallow schemas for serialization and validation
- Unit tests for models, routes, and integration

## Features
- **Workouts**
    - Create, list, retrieve, delete
    - Stretch: cascade deletes and include linked exercises
- **Exercises**
    - Create, list, retrieve, delete
    - Stretch: cascade deletes and include linked workouts
- **WorkoutExercises**
    - Link workouts and exercises with reps/sets/duration
    - Delete and retrieve links

## Tech Stack
- **Backend**: Flask + Flask-Migrate + SQLAlchemy
- **Validation/Serialization**: Marshmallow
- **Database**: SQLite (default), configurable for Postgres
- **Testing**: pytest + Flask test client

## Installation & Setup
### 1. Clone & create virtual environment
```
git clone git@github.com:nrathbone-turing/Summative-Lab-Flask-SQLAlchemy-Workout-Application-Backend.git
cd Summative-Lab-Flask-SQLAlchemy-Workout-Application-Backend

pipenv install --dev
pipenv shell
```

### 2. Configure environment
Create a `.flaskenv` file (already scaffolded):
```
FLASK_APP=server.app
FLASK_RUN_PORT=5555
FLASK_DEBUG=1
```

Optional: `.env` with DB overrides:
```
DATABASE_URI=sqlite:///app.db
```

### 3. Initialize DB & migrations
```
flask db init
flask db migrate -m "initial tables"
flask db upgrade head
```

### 4. Seed sample data
```
python -m server.seed
```

### 5. Run server
```
flask run
# -> http://127.0.0.1:5555
```

## Data Model
```
Exercise
- id               int, PK
- name             string, required, unique (name+category)
- category         string, required
- equipment_needed bool, default False

Workout
- id               int, PK
- date             date, required
- duration_minutes int, >=0, default 0
- notes            text

WorkoutExercise
- id               int, PK
- workout_id       FK --> Workouts
- exercise_id      FK --> Exercises
- reps             int, >=0
- sets             int, >=0
- duration_seconds int, >=0
```

## API Endpoints

### Workouts
- `GET /workouts` — list all workouts
- `GET /workouts/<id>` — show single workout (+ stretch: include join data)
- `POST /workouts` — create
- `DELETE /workouts/<id>` — delete (+ stretch: cascade join rows)

### Exercises
- `GET /exercises` — list all
- `GET /exercises/<id>` — show (+ associated workouts)
- `POST /exercises` — create
- `DELETE /exercises/<id>` — delete (+ stretch: cascade join rows)

### WorkoutExercises
- `POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` — add exercise to workout with reps/sets/duration
- `GET /workout_exercises/<id>` — fetch a single join row (WorkoutExercise) by id, including reps/sets/duration data  
- `DELETE /workout_exercises/<id>` — remove a join row (WorkoutExercise) by id; returns 404 if not found

## Example REST Calls
```
# Create an exercise
curl -X POST http://127.0.0.1:5555/exercises/ \
  -H "Content-Type: application/json" \
  -d '{"name":"Push-ups","category":"Strength"}'
```

```
# Create a workout
curl -X POST http://127.0.0.1:5555/workouts/ \
  -H "Content-Type: application/json" \
  -d '{"date":"2025-08-23","duration_minutes":30}'
```

```
# Link exercise to workout
curl -X POST http://127.0.0.1:5555/workouts/1/exercises/1/workout_exercises \
  -H "Content-Type: application/json" \
  -d '{"reps":15,"sets":3}'
```

## Running Tests
```
pytest -v
```
Covers:
- Model validations & constraints
- Route behavior (200, 201, 400, 404, 204 cases)
- Integration of join table

## Project Structure
```
Summative-Lab-Flask-SQLAlchemy-Workout-Application-Backend/
├─ README.md
├─ Pipfile / Pipfile.lock       # Python dependencies
├─ migrations/                  # Flask-Migrate versions
├─ server/
│  ├─ app.py                    # Flask app + config
│  ├─ models.py                 # SQLAlchemy models + constraints
│  ├─ schemas.py                # Marshmallow schemas + validations
│  ├─ seed.py                   # sample seed data
│  └─ routes/                   # API routes (Blueprints)
│     ├─ workouts.py
│     ├─ exercises.py
│     └─ workout_exercises.py
└─ tests/                       # pytest suite
   ├─ conftest.py               # shared fixtures (db, client, app_context)
   ├─ test_models_exercises.py
   ├─ test_models_workouts.py
   ├─ test_models_workout_exercise.py
   ├─ test_routes_app.py        # healthcheck
   ├─ test_routes_workouts.py
   ├─ test_routes_exercises.py
   ├─ test_routes_workout_exercises.py
   └─ test_schemas.py           # schema validation tests
```

## About This Repo
**Author:** Nick Rathbone | [GitHub Profile](https://github.com/nrathbone-turing)

This project is part of the Flatiron Relational Databases course summative assessment.

**License**: MIT — feel free to use or remix!