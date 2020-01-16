from django.core.exceptions import ValidationError

CATEGORY=['Mexican','Gujrati','Punjabi','Italian','South','Family']
 
def validate_category(value):
	cat=value.capitalize()
	if not value in CATEGORY and not cat in CATEGORY:
		raise ValidationError(value+" not a valid category")
