from django import forms
from django.forms import ModelForm
from django.utils.translation import gettext_lazy as _

from .models import Case, DataFile


class UploadFileForm(forms.Form):
    title = forms.HiddenInput()
    file = forms.FileField()
    
class UploadDataFile(ModelForm):
    
    class Meta:
        model = DataFile
        fields = ['zipfile']


class CaseSearchForm(ModelForm):

    class Meta:
        model = Case
        fields = ['defendant_name']
        labels = {
            'defendant_name': _(""),
        }
        help_texts = {
            'defendant_name': _(""),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['defendant_name'].widget.attrs.update(
            {'class': 'input is-medium'})
