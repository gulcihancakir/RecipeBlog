from django import forms
from .models import Post, Ingredient


class PostForm(forms.ModelForm):
  
    class Meta:
        model=Post
        fields=('recipe_name','image','description','level', 'ingredients',)
        
        # ingredient = forms.ModelMultipleChoiceField(Ingredient.objects.all())