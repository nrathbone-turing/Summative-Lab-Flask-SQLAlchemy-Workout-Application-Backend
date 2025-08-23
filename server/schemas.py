from marshmallow import Schema, fields

class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Bool()

class ExerciseCreateSchema(Schema):
    name = fields.Str(required=True)
    category = fields.Str(required=True)
    equipment_needed = fields.Bool(load_default=False)

class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    reps = fields.Int(allow_none=True)
    sets = fields.Int(allow_none=True)
    duration_seconds = fields.Int(allow_none=True)

class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int()
    notes = fields.Str(allow_none=True)
    # read-only nested join rows for stretch
    workout_exercises = fields.List(fields.Nested(WorkoutExerciseSchema), dump_only=True)

class WorkoutCreateSchema(Schema):
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True)
    notes = fields.Str(load_default=None)

class WorkoutExerciseCreateSchema(Schema):
    # workout_id/exercise_id come from the URL &
    # reps/sets/duration are optional, non-negative ints
    reps = fields.Int(allow_none=True)
    sets = fields.Int(allow_none=True)
    duration_seconds = fields.Int(allow_none=True)