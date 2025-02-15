from django import forms


class TemplateForm(forms.Form):
    # choices в ChoiceField нужен только для отображения в HTML форме
    name = forms.CharField()
    # widget тоже нужен только для отображения в HTML
    email = forms.EmailField()