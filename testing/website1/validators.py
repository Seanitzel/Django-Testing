from django.core.exceptions import ValidationError

WORKOUT = ['Legs', 'Chest', 'Abs', 'General']

def validate_workout(value):
	cat = value.capitalize()
	if not value in WORKOUT and not cat in WORKOUT:
		raise ValidationError(f"{value} not a valid workout")