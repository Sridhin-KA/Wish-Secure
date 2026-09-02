from django import forms

from .models import Promise


class PromiseForm(forms.ModelForm):

    class Meta:

        model = Promise

        exclude = [
            "made_by",
            "kept_at",
            "created_at",
            "updated_at",
        ]

        widgets = {

            "promise_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 6,
                    "placeholder": "Write the promise you want to remember..."
                }
            ),

        }