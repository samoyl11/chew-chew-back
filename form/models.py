from django.db import models

class Form(models.Model):
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    telephone = models.CharField(max_length=120)

    def _str_(self):
        return self.telephone
