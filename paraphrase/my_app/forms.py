from .models import MyText
from django.forms import ModelForm, Textarea


class MyTextForm(ModelForm):
    class Meta:
        model = MyText
        fields = ['tree', 'limit']
        
        widgets = {
            'tree': Textarea(attrs={
                'placeholder': 'Input your text'
                }),
            
        }