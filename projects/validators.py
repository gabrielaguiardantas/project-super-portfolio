from django.core.exceptions import ValidationError


# editar amanhã
def validate_fields(value):
    value_without_spaces = value.replace(" ", "")  # remove espaços
    if not 1 <= len(value_without_spaces) <= 500:
        raise ValidationError(
            "As propriedades da Model não devem conter informações vazias"
            + " ou maiores que 500 caracteres."
        )
