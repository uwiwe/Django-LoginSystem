# from django.core.exceptions import ValidationError

# def validate_uppercase(value):
#     """Valida que la contraseña contenga al menos una letra mayúscula."""
#     if not any(char.isupper() for char in value):
#         raise ValidationError('La contraseña debe contener al menos una letra mayúscula.')

# def validate_lowercase(value):
#     """Valida que la contraseña contenga al menos una letra minúscula."""
#     if not any(char.islower() for char in value):
#         raise ValidationError('La contraseña debe contener al menos una letra minúscula.')

# def validate_number(value):
#     """Valida que la contraseña contenga al menos un número."""
#     if not any(char.isdigit() for char in value):
#         raise ValidationError('La contraseña debe contener al menos un número.')

# def validate_special_character(value):
#     """Valida que la contraseña contenga al menos un carácter especial."""
#     special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>?/~"
#     if not any(char in special_characters for char in value):
#         raise ValidationError('La contraseña debe contener al menos un carácter especial.')

# def validate_common_words(value):
#     """Evita contraseñas con palabras comunes."""
#     common_words = ["password", "qwerty", "123456", "admin", "welcome"]
#     if any(word in value for word in common_words):
#         raise ValidationError('La contraseña contiene una palabra común y es fácil de adivinar.')

# def validate_minimum_length(value):
#     """Valida que la contraseña tenga una longitud mínima."""
#     min_length = 8  # Puedes ajustar este valor según tus necesidades.
#     if len(value) < min_length:
#         raise ValidationError(f'La contraseña debe tener al menos {min_length} caracteres.')