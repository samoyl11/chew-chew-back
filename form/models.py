from django.db import models
from django.core.mail import send_mail

class Form(models.Model):
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    telephone = models.CharField(max_length=120)
    completed = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        send_mail('hello', 'wazap', 'test4sendingresults@gmail.com', ['test4sendingresults@gmail.com'])

    def _str_(self):
        return self.firstName
