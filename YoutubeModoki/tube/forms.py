from django import forms
from .models import Video

class VideoCreateForm(forms.ModelForm):

    class Meta:
        model = Video
        fields = ('title', 'description', 'thumbnail', 'upload')

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),#<input type="text" class="form-control" 
            'discription': forms.Textarea(attrs={'class':'from-control'}),
            'thumbnail': forms.ClearableFileInput(attrs={'class':'form-control-file'}),
            'upload': forms.ClearableFileInput(attrs={'class':'form-control-file'}),
        }