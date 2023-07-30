from django.db import models

# Create your models here.
class Advertisement(models.Model):
    public_text = models.TextField('public_text')
    price = models.DecimalField('Price', max_digits= 10, decimal_places= 2)
    model_product = models.CharField(max_length=128)
    auction = models.BooleanField('Torg',help_text='Yes and not')
    created_at = models.DateTimeField('Date', auto_now_add = True)
    updated_at = models.DateTimeField(auto_now=True)

class Advertisement_2(models.Model):
    title = models.CharField('Заголовок', max_length = 128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена', max_digits = 10, decimal_places = 2)
    auction = models.BooleanField('Торг', help_text = 'укажите, если торг уместен(да  или нет)')
    created_at = models.DateTimeField('Дата', auto_now_add = True)
    updated_at = models.DateTimeField('Jбновленно', auto_now = True)
    def __str__(self):
        return self.title, self.price
    class Meta:
        db_table = 'advertisements'