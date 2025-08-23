"""
PSEUDOCODE MARSHMALLOW SCHEMAS:
- ExerciseSchema
- WorkoutSchema
- WorkoutExerciseSchema

SCHEMA VALIDATIONS:
- validate length for name/category
- validate ranges for duration/reps/sets
- nested relationships for includes
"""
# from marshmallow import Schema, fields, validates, ValidationError
# from marshmallow_sqlalchemy import SQLAlchemyAutoSchema, auto_field
#
# class ExerciseSchema(SQLAlchemyAutoSchema):
# # PSEUDOCODE: Meta binds to Exercise model, include relationships as needed
# pass
#
# class WorkoutExerciseSchema(SQLAlchemyAutoSchema):
# # PSEUDOCODE: includes reps/sets/duration_seconds
# pass
#
# class WorkoutSchema(SQLAlchemyAutoSchema):
# # PSEUDOCODE: include nested WorkoutExercises for stretch
# pass