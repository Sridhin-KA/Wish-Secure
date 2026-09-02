from django import forms

from .models import Gift


class GiftForm(forms.ModelForm):

    class Meta:

        model = Gift

        exclude = [
            "added_by",
            "created_at",
            "updated_at",
        ]

        widgets = {

            "gift_date": forms.DateInput(
                attrs={
                    "type": "date"
                }
            ),

            "description": forms.Textarea(
                attrs={
                    "rows": 5,
                    "placeholder": "What makes this gift special?"
                }
            ),

            "price": forms.NumberInput(
                attrs={
                    "step": "0.01",
                    "placeholder": "Optional"
                }
            ),

            "link": forms.URLInput(
                attrs={
                    "placeholder": "https://..."
                }
            ),

        }   