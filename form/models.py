from django.db import models
import smtplib, ssl

class Form(models.Model):
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    telephone = models.CharField(max_length=120)
    completed = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        port = 465  # For SSL
        smtp_server = "smtp.gmail.com"
        sender_email = "test4sendingresults@gmail.com"  # Enter your address
        receiver_email = "test4sendingresults@gmail.com"  # Enter receiver address
        password = '9250087828'
        message = """\
        Subject: Hi there

        This message is sent from Python."""

        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message)
    def _str_(self):
        return self.firstName
