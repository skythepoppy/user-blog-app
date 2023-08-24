from django import forms as f
from .models import Post

class PostForm(f.ModelForm):

    class Meta:
        model = Post
        fields = '__all__'

        widgets = {
            'title': f.TextInput(attrs={'class':'form-control'}),
            'slug': f.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter any tags related to your post'
                                                                              ' separated by dashes (-)'}),
            'author': f.Select(attrs={'class': 'form-control'}),
            'content': f.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write Away!'}),
            'status': f.Select(attrs={'class': 'form-control'}),
        }