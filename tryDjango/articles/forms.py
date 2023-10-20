from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content']
        
        
    def clean(self):
        data= self.cleaned_data
        title = data.get('title')
        qs = Article.objects.filter(title__icontains =title)
        if qs.exists:
            self.add_error('title', f"{title} is already existes, please enter other title")
            
        return data
        
        

        
        
        
class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()
    
    # def clean_title(self):
    #     cleaned_data = self.cleaned_data # dictionary
    #     print("cleaned_data:", cleaned_data)
    #     title = cleaned_data.get('title') 
    #     if title.lower().strip() == "the office":
    #         raise forms.ValidationError("this title is given")
    #     print("title :", title)
    #     return title
    
    def clean(self):
        cleaned_data = self.cleaned_data # dictionary
        print("cleaned_data:", cleaned_data)
        title = cleaned_data.get('title') 
        print("title :", title)
         
        if title.lower().strip() == "the office":
            self.add_error('title', "this title is given")
            # raise forms.ValidationError("this title is given")
        
        content = cleaned_data.get('content') 
        if "office" in content or "office" in title.lower():
            self.add_error('content', 'office cannot be in content')
            raise forms.ValidationError('content is not allowed')
        
        return cleaned_data