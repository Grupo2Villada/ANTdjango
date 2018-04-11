from django.forms import ModelForm
from .models import *

class FormGrade(ModelForm):
    class Meta:
        model = Grade
        fields = ['value', 'subject', 'student']
