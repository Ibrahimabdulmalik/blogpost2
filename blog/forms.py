from django import forms
from .models import Blogpost

class BlogPostForms(forms.Form):
    title = forms.CharField()
    slug = forms.SlugField()
    content = forms.CharField(widget=forms.Textarea)


class BlogPostModelForm(forms.ModelForm):
    class Meta:
        model = Blogpost
        fields = ['title' ,'image','slug' ,'content','published_date']
    

    def cleaned_title(self,*args,**kwargs):
        instance = self.instance
        print(instance)
        title = self.cleaned_data.get('title')
        qs = Blogpost.objects.filter(title__iexact=title )
        if instance is not None:
            qs = qs.exclude(pk=instance.pk)
        if qs.exists():
            raise forms.ValidationError("title already exist ")
        return title

 