from django import forms
from .models import UserProfile, Post, Comment, ThreadModel, MessageModel

class PostForm(forms.ModelForm):
    body=forms.CharField(
        max_length=200,
        label='',
        widget=forms.Textarea(attrs={
            'rows':'3',
            'placeholder':'Say Something...'
        })
    )

    post_image = forms.ImageField(required=False)
    class Meta:
        model=Post
        fields=['body','post_image']

class CommentForm(forms.ModelForm):
    comment=forms.CharField(
        max_length=200,
        label='',
        widget=forms.Textarea(attrs={
            'rows':'2',
            'placeholder':'Compose Comment...'
        })
    )
    class Meta:
        model=Comment
        fields=['comment']

class UserprofileForm(forms.ModelForm):

    class Meta:
        model=UserProfile
        fields=('name','bio','location','birth_date','education','work', 'place_of_work','skill','hobby','religion','status', 'profile_picture')
    def __init__(self,*args,**kwargs,): 
        super(UserprofileForm,self).__init__(*args,**kwargs)
        self.fields['work'].empty_label='select'
    
class ShareForm(forms.Form):
    body=forms.CharField(
        label='',
        widget=forms.Textarea(attrs={
            'rows':'3',
            'placeholder':'Say Something...'
            }))
    post_image = forms.ImageField(required=False)
    class Meta:
        model=Post
        fields=['body','post_image']

class ThreadForm(forms.Form):
    username = forms.CharField(label='', max_length=100)
     

class MessageForm(forms.ModelForm):
    body = forms.CharField(
        label='', max_length=1000)
    
    image = forms.ImageField(required=False)
    class Meta:
        model = MessageModel
        fields=['body', 'image']
