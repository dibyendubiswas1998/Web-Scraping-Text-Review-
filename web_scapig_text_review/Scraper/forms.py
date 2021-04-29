from django import forms
from .models import Input, Review_Details


class InputForm(forms.ModelForm):
    class Meta:
        model = Input
        fields = ['input', 'category']
        widgets = {
            'input': forms.TextInput(attrs={'class': 'my_class', 'placeholder': 'Enter Link Here'}),
        }

    def __init__(self, *args, **kwargs):
        super(InputForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select The Domain"


class Review_Details_Form(forms.ModelForm):
    class Meta:
        model = Review_Details
        fields = "__all__"
