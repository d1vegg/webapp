from django.db import models

class Order(models.Model):
    title = models.CharField('Название', max_length=50),
    description = models.CharField('Описание', max_length=250)
    datetime = models.DateTimeField('Дата и время')
    nickname = models.CharField('Никнейм',max_length=25)
    type = models
    # currency_crypto: = ""
    # currency_fiat: = ""
    # amount_crypto: = ""
    # amount_fiat: = ""
    # status: = ""
    # goal: = ""

def __str__(self):
    return self.title