# Workout Application Backend (Flask + SQLAlchemy)

> Summative lab scaffold with **pseudocode** to start

## Quickstart Checklist (Dev)
- Python version: 3.x
- Create virtualenv (pipenv or venv)
- Install deps from Pipfile or requirements.txt
- Create `.flaskenv` and `.env` as needed
- Initialize DB and migrations:
```
flask db init
flask db migrate -m "initial tables"
flask db upgrade head
```

### Seed data:

```
python -m server.seed
```

### Run server:

```
s
```

## Entities (from spec)

- Exercise(id, name, category, equipment_needed)
- Workout(id, date, duration_minutes, notes)
- WorkoutExercise(id, workout_id, exercise_id, reps, sets, duration_seconds)

## Endpoints (from spec)

- `GET /workouts` — list all workouts
- `GET /workouts/<id>` — show single workout (+ stretch: include join data)
- `POST /workouts` — create
- `DELETE /workouts/<id>` — delete (+ stretch: cascade join rows)
- `GET /exercises` — list all
- `GET /exercises/<id>` — show (+ associated workouts)
- `POST /exercises` — create
- `DELETE /exercises/<id>` — delete (+ stretch: cascade join rows)
- `POST /workouts/<workout_id>/exercises/<exercise_id>/workout_exercises` — add exercise to workout with reps/sets/duration

## Implementation Steps (from spec for reference)

1. Setup application structure & deps
2. Define models
3. Set up relationships
4. Add table constraints & model validations
5. Initialize DB & migrations
6. Seed and verify
7. Create endpoints (scaffold first then wire up the schemas)
8. Setup Marshmallow schemas
9. Add schema validations
10. Edit endpoints to use schemas for serialization/deserialization