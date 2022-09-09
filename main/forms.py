from django import forms

class ContactForm(forms.Form):
    
    name = forms.CharField(max_length=50)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data['name']
        email = cleaned_data['email']

        if name == '' and email == '':
            #raise forms.ValidationError("Email or Phone 1 should be field", code='invalid')
            self.add_error("name", "Name or Email 1 should be field")