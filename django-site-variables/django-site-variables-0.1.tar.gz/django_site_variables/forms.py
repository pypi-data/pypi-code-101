from django import forms


class SiteVariableForm(forms.ModelForm):
    pass


class SiteVariableNumberForm(forms.ModelForm):
    class Meta:
        widgets = {
            'content': forms.NumberInput()
        }


class SiteVariableBooleanForm(forms.ModelForm):
    class Meta:
        widgets = {
            'content': forms.CheckboxInput()
        }
