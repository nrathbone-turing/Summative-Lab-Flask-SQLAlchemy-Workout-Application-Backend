from marshmallow import Schema, fields, validates_schema, ValidationError, validate

ALLOWED_CATEGORIES = ("Strength", "Cardio", "Core", "Bodyweight", "HIIT")

class ExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    category = fields.Str(required=True, validate=validate.OneOf(ALLOWED_CATEGORIES))
    equipment_needed = fields.Bool()

class ExerciseCreateSchema(Schema):
    name = fields.Str(required=True)
    category = fields.Str(
        required=True,
        validate=validate.OneOf(ALLOWED_CATEGORIES, error="category must be one of: " + ", ".join(ALLOWED_CATEGORIES)),
    )
    equipment_needed = fields.Bool(load_default=False)

class WorkoutExerciseSchema(Schema):
    id = fields.Int(dump_only=True)
    workout_id = fields.Int(required=True)
    exercise_id = fields.Int(required=True)
    reps = fields.Int(allow_none=True, validate=validate.Range(min=0, error="reps must be >= 0"))
    sets = fields.Int(allow_none=True, validate=validate.Range(min=0, error="sets must be >= 0"))
    duration_seconds = fields.Int(allow_none=True, validate=validate.Range(min=0, error="duration_seconds must be >= 0"))

class WorkoutSchema(Schema):
    id = fields.Int(dump_only=True)
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True, validate=validate.Range(min=0, error="duration_minutes must be >= 0"))
    notes = fields.Str(allow_none=True)
    # read-only nested join rows for stretch
    workout_exercises = fields.List(fields.Nested(WorkoutExerciseSchema), dump_only=True)

class WorkoutCreateSchema(Schema):
    date = fields.Date(required=True)
    duration_minutes = fields.Int(required=True, validate=validate.Range(min=0, error="duration_minutes must be >= 0"))
    notes = fields.Str(load_default=None, validate=validate.Length(max=500))

class WorkoutExerciseCreateSchema(Schema):
    reps = fields.Int(allow_none=True, validate=validate.Range(min=0, error="reps must be >= 0"))
    sets = fields.Int(allow_none=True, validate=validate.Range(min=0, error="sets must be >= 0"))
    duration_seconds = fields.Int(allow_none=True, validate=validate.Range(min=0, error="duration_seconds must be >= 0"))

    @validates_schema
    def at_least_one_value(self, data, **kwargs):
        # require at least one of reps/sets/duration_seconds to be provided
        if all(data.get(k) in (None, "") for k in ("reps", "sets", "duration_seconds")):
            raise ValidationError("Provide at least one of: reps, sets, duration_seconds.")