from django import forms
from app.models import URLModel

class URLForm(forms.ModelForm):
    url = forms.URLField(widget=forms.TextInput(attrs={'placeholder': 'Enter URL', 'size':'12', 'class': "form-control"}),label='URL')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['url'].required = True
        
    class Meta:
        verbose_name = 'url'
        model = URLModel
        fields = ['url']

