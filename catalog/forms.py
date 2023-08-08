from django import forms
from catalog.models.products import Product
from catalog.models.version import Version

banned_words = ('казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар')


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields =('name', 'description', 'image', 'category', 'purchase_price')

    def clean_name(self):
        cleaned_data = self.cleaned_data['name']
        for word in banned_words:
            if word in cleaned_data.lower():
                raise forms.ValidationError('Недопустимые темы в литературе')
        return cleaned_data

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'


class VersionForm(forms.ModelForm):
    class Meta:
        model = Version
        fields = '__all__'

    def __int__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
