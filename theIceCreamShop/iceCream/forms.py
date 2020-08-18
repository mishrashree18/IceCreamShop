from django import forms
from .models import icecream, Type

# class icecreamForm(forms.Form):
#     flavour1 = forms.CharField(label='Flavour', max_length=100)
#     additionals = forms.CharField(label='additionals', max_length=100)
#     type = forms.ChoiceField(label='Type', choices=[('Bar','Bar'),('Cone','Cone'),('Cup','Cup')])


class icecreamForm(forms.ModelForm):
    type = forms.ModelChoiceField(queryset=Type.objects, empty_label=None, widget=forms.RadioSelect)
    class Meta:
        model = icecream
        fields = ['flavour1','additionals','type']
        labels = {'flavour1':'Flavour 1','Additionals':'additionals'}
        
class MultiplePizzaForm(forms.Form):
    number = forms.IntegerField(min_value=2, max_value=50)