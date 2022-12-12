from django import forms

# creating a form
class loginForm(forms.Form):

    user = forms.CharField(max_length = 8)
    password = forms.CharField(max_length=8)
    
class projectForm(forms.Form):


    photo = forms.CharField(max_length=1000)
    title= forms.CharField(max_length=50)
    tags= forms.CharField(max_length=50)
    description= forms.CharField(max_length=1000)
    git= forms.CharField(max_length=50)