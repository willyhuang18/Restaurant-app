# Import the necessary modules
from django import forms
from .models import Review

# Define a form for the Review model
class ReviewForm(forms.ModelForm):
    class Meta:
        # Specify the model and fields to use
        model = Review
        fields = ['rating', 'comment']