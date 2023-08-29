from django import forms as f
from .models import Post

class PostForm(f.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'content', 'status', 'header_image')

        widgets = {
            'title': f.TextInput(attrs={'class':'form-control', 'placeholder': 'Blog Post Title'}),
            'slug': f.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter any tags related to your post'
                                                                              ' separated by dashes (-)'}),
            'author': f.TextInput(attrs={'class': 'form-control', 'value':'', 'id':'author', 'type':'hidden'}),
            'content': f.Textarea(attrs={'class': 'form-control', 'placeholder': 'Write Away!'}),
            'status': f.Select(attrs={'class': 'form-control'}),

        }