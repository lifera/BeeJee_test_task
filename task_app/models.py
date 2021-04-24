from django.db import models


class Task(models.Model):
    username = models.CharField(max_length=200)
    email = models.EmailField()
    text = models.CharField(max_length=200)
    status = models.BooleanField(default=0)
    changed_by_admin = models.BooleanField(default=0)

    __original_text = None

    def __init__(self, *args, **kwargs):
        super(Task, self).__init__(*args, **kwargs)
        self.__original_text = self.text

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if self.text != self.__original_text and self.pk is not None:
            self.changed_by_admin = 1

        super(Task, self).save(force_insert, force_update, *args, **kwargs)
        self.__original_text = self.text

    def __str__(self):
        return self.text
