from django import forms
from .models import Wish


class WishForm(forms.ModelForm):

    class Meta:

        model = Wish

        exclude = [
            'created_by',
            'created_at',
            'updated_at'
        ]

        widgets = {

            'description':forms.Textarea(
                attrs={
                    'rows':5
                }
            )

        }