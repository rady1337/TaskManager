from django.db import models


class Tasks(models.Model):
    title = models.CharField('Title', max_length=200)
    text = models.TextField('Task')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

