from django.db import models
from django.core.mail import send_mail
import telebot

token = '1040941161:AAGRKhQAsHaPsXVQH6nfuaE_Sap-9qnN878'

from telebot import types

bot= telebot.TeleBot(token)
bot.config['api_key'] = token;
class Form(models.Model):
    firstName = models.CharField(max_length=120)
    lastName = models.CharField(max_length=120)
    telephone = models.CharField(max_length=120)
    completed = models.BooleanField(default=False)
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        #send_mail('New Client', f'Телефон: {self.telephone}\n Имя: {self.firstName}\n Фамилия: {self.lastName}\n', 'alquilar.cochee@gmail.com', ['alquilar.cochee@gmail.com'])
        str = "Новый клиент.\nИмя: {} {}\nТелефон: {}".format(self.firstName, self.lastName, self.telephone)
        bot.send_message(chat_id='270129913', text=str)
        bot.send_message(chat_id='251780463', text=str)
        bot.send_message(chat_id='309350089', text=str)
        bot.send_message(chat_id='-368201757', text=str)
    def _str_(self):
        return self.firstName
