from django.core.exceptions import ValidationError

def validate_phone(self):
	if len(self) < 10:
		raise ValidationError('Phone number is correct!')
	else:
		return self
	