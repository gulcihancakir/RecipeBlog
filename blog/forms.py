from django import forms
from .models import Post, Ingredient

OPTIONS = (('Tomato', 'Tomato'),
                          ('Eggplant', 'Eggplant'),
                          ('Celery', 'Celery'),
                          ('Egg', 'Egg'),
                          ('Milk', 'Milk'),
                          ('Fish', 'Fish'),
                          ('Chicken', 'Chicken'),
                          ('Oil', 'Oil')
                          )
class PostForm(forms.ModelForm):
    """ Bu class gonderi kaydetmeye yarar. eger birsey donduruyorsa falan onu da int dondurur gibi asagiki gibi belirt. tam bilemedim. docs_string yaz google a python ile guzel dokumantasyon olusturabilirsin otomatik. bu sekilde yazarsan.
    return: int """

    class Meta:
        model=Post
        fields=('recipe_name','image','description','level', 'ingredients')
    #@TODO: yorumlar eger ise yaramiyorsa sil. ama fonksiyonun ne yaptigini acikliyorsa docs_string seklinde yaz. mesela bu class ne ise yariyor yazıyorum.
    #ingredient = forms.ModelMultipleChoiceField(Ingredient.objects.all())