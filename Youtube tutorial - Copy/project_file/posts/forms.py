from django import forms
from.models import postspage

class postform(forms.ModelForm):
    class Meta:
        model=postspage
        fields=["title","image","content",]