from django.db import models

# Create your models here.


class ToDo(models.Model):

    toDo_text = models.CharField(max_length=160)
    due_date = models.DateTimeField()
    progress = models.IntegerField(default=0)

    def __str__(self):
        return self.toDo_text
