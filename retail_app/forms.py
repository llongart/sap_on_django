from tabnanny import verbose
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
            validators.RegexValidator('^[0-9]*$', 'Solo es posible introducir caracteres númericos', 'bad_article'),
        ]
    )

    article_group = forms.CharField(
        max_length = 10,
        min_length = 5,
        required = False,
        widget = forms.TextInput(
            attrs = {
                'placeholder': 'Código de grupo de artículos SAP',
                'class': 'article_group_form', 
            }
        ),
        label = 'Grupo de artículos',
        validators = [
            validators.RegexValidator('^[A-Za-z0-9]*$', 'No es posible introducir caracteres especiales', 'bad_article_group'),
        ]
    )

class MatchCodeForm(forms.Form):

    material = forms.CharField(
        required=False,
        widget = forms.Textarea(),        
        validators=[
            validators.MaxLengthValidator(20, 'Contenido demasiado largo')
        ],
        label="Artículos"
    )

    material.widget.attrs.update({
        'class': 'articles_matchcode_form',
        'placeholder': 'Artículos'
    })