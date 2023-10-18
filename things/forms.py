"""Forms of the project."""

from django import forms
from .forms import ThingForm
# Create your forms here.

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ["name", "description", "quantity"]
        widgets = {"description": forms.TextArea(),
                    "quantity": forms.NumberInput()}

