from django.db import models
from django.core.mail import send_mail

class Form(models.Model):
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    telephone = models.CharField(max_length=120)
    completed = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        send_mail('New Client', f'Телефон: {self.telephone}\ Имя: {self.firstName}\n Фамилия: {self.lastName}\n', 'alquilar.cochee@gmail.com', ['alquilar.cochee@gmail.com'])

    def _str_(self):
        return self.firstName
