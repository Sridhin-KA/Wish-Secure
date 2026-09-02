from django import forms

from .models import SpecialDate


class SpecialDateForm(forms.ModelForm):

    class Meta:

        model = SpecialDate

        exclude = [
            "created_by",
            "created_at",
            "updated_at",
        ]

        widgets = {

            "date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder":
                        "Why is this date special?"
                }
            ),

            "icon": forms.TextInput(
                attrs={
                    "placeholder": "❤️"
                }
            ),
        }