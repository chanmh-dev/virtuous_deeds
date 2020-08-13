from django import forms
from vdeed_app.models import deeds1, deeds2, deeds3
            

class deeds1Form(forms.ModelForm):
    class Meta:
        model = deeds1
        fields = ['deed', 'name']
        labels = {
            'name': 'Enter your name here (姓名)',
            'deed': 'OMAK (观功念恩)'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'True', 'blank': 'False'}), 
            'deed': forms.Textarea(attrs={'rows': "4", 'maxlength': '250', 'class': 'form-control', 'required': 'True', 'blank': 'False'})
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
        super(deeds1Form, self).__init__(*args, **kwargs)
        if hide_condition:
            self.fields['deed'].widget = HiddenInput()
            self.fields['name'].widget = HiddenInput()
            # or alternately:  del self.fields['fieldname']  to remove it from the form altogether. 
  

class deeds2Form(forms.ModelForm):
    class Meta:
        model = deeds2
        fields = ['deed', 'name']
        labels = {
            'name': 'Enter your name here (姓名)',
            'deed': 'Remembering Kindness (修信念恩)'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'True', 'blank': 'False'}), 
            'deed': forms.Textarea(attrs={'rows': "4", 'maxlength': '250', 'class': 'form-control', 'required': 'True', 'blank': 'False'})
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
        super(deeds2Form, self).__init__(*args, **kwargs)
        if hide_condition:
            self.fields['deed'].widget = HiddenInput()
            self.fields['name'].widget = HiddenInput()
            # or alternately:  del self.fields['fieldname']  to remove it from the form altogether. 
  

class deeds3Form(forms.ModelForm):
    class Meta:
        model = deeds3
        fields = ['deed', 'name']
        labels = {
            'name': 'Enter your name here (姓名)',
            'deed': 'Virtuous deeds (善行点滴)'
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'required': 'True', 'blank': 'False'}), 
            'deed': forms.Textarea(attrs={'rows': "4", 'maxlength': '250', 'class': 'form-control', 'required': 'True', 'blank': 'False'})
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
        super(deeds3Form, self).__init__(*args, **kwargs)
        if hide_condition:
            self.fields['deed'].widget = HiddenInput()
            self.fields['name'].widget = HiddenInput()
            # or alternately:  del self.fields['fieldname']  to remove it from the form altogether. 