from django import forms
from pagedown.widgets import PagedownWidget

from .models import Post

CATEGORIES = (
    ('PROGRAMMING', 'Programming'),
    ('DESIGN', 'Design'),
    ('TECHNOLOGY', 'Technology'),
    ('SECURITY', 'Security'),
    )

class PostForm(forms.ModelForm):
    content = forms.CharField(widget=PagedownWidget(show_preview=False))
    publish = forms.DateField(widget=forms.SelectDateWidget)
    category = forms.ChoiceField(choices=CATEGORIES, required=True)
    class Meta:
        model = Post
        fields = [
        "title",
        "category",
        "content",
        "image",
        "draft",
        "publish",
]

