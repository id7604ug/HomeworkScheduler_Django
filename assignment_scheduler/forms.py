from django import forms
from .models import ScheduleItem

class AddAssignmentForm(forms.ModelForm):
    class Meta:
        model = ScheduleItem
        # todo Figure out how to get a date time picker for due_date
        fields = ('class_name', 'name', 'complete', 'description', 'due_date')
