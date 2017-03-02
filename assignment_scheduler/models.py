from django.db import models
from django.utils import timezone

# Create your models here.
class ScheduleItem(models.Model):

    class_name = models.CharField(max_length=200)
    name = models.CharField(max_length=100)
    complete = models.BooleanField()
    description = models.TextField()
    due_date = models.DateTimeField(blank=True, null=True)

    def __repr__(self):
        return "ID: {}; Name: {}; IsComplete: {}; Description: {}; DueDate: {}".format(self.id, self.name, self.complete, self.description, self.due_date)
