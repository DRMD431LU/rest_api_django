from django import forms

from .models import Status
import pdb

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]

    def clean_content(self, *args, **kwargs):
        content = self.cleaned_data.get('content')
        content = content.encode(encoding='UTF-8',errors='strict')
        if len(content) > 240:
            raise forms.ValidationError('content too lung')
        return content

    def clean(self, *args, **kwargs):
        data = self.cleaned_data
        content = data.get('content', None)
        if content == "":
            content = None
        image = data.get("image", None)
        print(content)
        if content is None and image is None:
            raise forms.ValidationError('Content or image is required')
        return super().clean(*args, **kwargs)
