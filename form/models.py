from django.db import models

class Form(models.Model):
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    telephone = models.CharField(max_length=120)
    completed = models.BooleanField(default=False)

    def _str_(self):
        return self.firstName
