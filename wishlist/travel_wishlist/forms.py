from django import forms
from .models import Place


class NewPlaceForm(forms.ModelForm):
	class Meta:
		model = Place
		fields = ('name',)

class PlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        fields = ('visited_date', 'note')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Does not show time since time uses midnight as default
        self.fields['visited_date'].widget = forms.DateInput()
        self.fields['note'].widget = forms.Textarea()