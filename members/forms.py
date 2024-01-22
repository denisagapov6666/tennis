from django import forms
from .models import FileUpload

class FileUploadModelForm(forms.ModelForm):
    class Meta:
        model = FileUpload
        fields = []