from django import forms
from django.core import validators

class ZinvtdForm(forms.Form):

    material = forms.CharField(
        max_length = 18,
        min_length = 7,
        required = False,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Número de artículo SAP',
                'class': 'material_number_form', 
            }
        ),
        label = 'N° Artículo',
        validators = [
            validators.MinLengthValidator(7, 'Número de artículo demasiado corto'),
            validators.MaxLengthValidator(18, 'Número de artículo demasiado largo'),
            validators.RegexValidator('^[0-9]*$', 'Solo es posible introducir caracteres númericos', 'bad_article'),
        ]
    )

    article_group = forms.CharField(
        max_length = 10,
        required = False,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Código de grupo de artículos SAP',
                'class': 'article_group_form', 
            }
        ),
        label = 'Grupo de artículos',
        validators = [
            validators.MinLengthValidator(7, 'Número de artículo demasiado corto'),
            validators.MaxLengthValidator(18, 'Número de artículo demasiado largo'),
            validators.RegexValidator('^[A-Za-z0-9]*$', 'No es posible introducir caracteres especiales', 'bad_article_group'),
        ]
    )
