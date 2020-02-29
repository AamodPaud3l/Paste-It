from django import forms
from .models import Todo

class todoForm(forms.ModelForm):
    class Meta:
        model=Todo

        fields=('text','title','link_code','lang', 'date_time')
        labels={'text':'New Paste','title':'Paste Title','link_code':'Paste Code','lang': 'Syntax Highlighting', 'date_time': 'Deadline'}
        #widgets={'lang': forms}
        