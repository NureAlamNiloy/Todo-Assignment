from django import forms
from . import models

class taskForm(forms.ModelForm):
    class Meta:
        model = models.taskModel
        fields = ['taskNo', 'taskTitle', 'taskDescription','is_completed']