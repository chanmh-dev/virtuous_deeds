from django import forms
from vdeed_app.models import  deeds
            

class deedsForm(forms.ModelForm):
    class Meta:
        model = deeds
        fields = ['deed', 'name']
        labels = {
            'name': 'Enter your name here (姓名)',
            'deed': 'Write your virtuous deeds here (请写下您的善行)'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'True', 'blank': 'False', 'label': 'Enter your name here (姓名)'},), 
            'deed': forms.Textarea(attrs={'rows': "4", 'maxlength': '250', 'class': 'form-control', 'required': 'True', 'blank': 'False',
            'label':'Write your virtuous deeds here (请写下您的善行)'})
        }

    def clean(self):
        cleaned_data = self.cleaned_data
        begin = '<p>'
        end = '</p> <br>'
        cleaned_data['deed'] = begin + cleaned_data['deed'] + ' (' + cleaned_data['name'] + ')' + end
        print (cleaned_data)
        return cleaned_data

    
    def __init__(self, *args, **kwargs):
        from django.forms.widgets import HiddenInput
        hide_condition = kwargs.pop('hide_condition',None)
        super(deedsForm, self).__init__(*args, **kwargs)
        if hide_condition:
            self.fields['deed'].widget = HiddenInput()
            self.fields['name'].widget = HiddenInput()
            # or alternately:  del self.fields['fieldname']  to remove it from the form altogether. 
  

