from django.contrib import admin
from django.db import models
from django.utils.html import format_html
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()




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
    updated_at = models.DateTimeField('Обновленно', auto_now = True)
    user = models.ForeignKey(User, verbose_name = 'Пользователь', on_delete = models.CASCADE)
    image = models.ImageField('Изображение', upload_to = 'advertisements/')
    @admin.display(description = 'дата создания')
    def datefilt(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color:green; font-weight: bold;"> Сегодня в {}</span>', created_time
            )
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')
    
    @admin.display(description = 'дата обновления')
    def dateupfilt(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            update_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style = "color:red; font-weight: bold;"> Сегодня в {}</span>', update_time
            )
        return self.updated_at.strftime('%d.%m.%Y в %H:%M:%S')
        
    @admin.display(description = 'фото')
    def image_tag(self):
        if self.image:
            return format_html('<a href="{0}" target="_blank"><img src="{0}" width = "100";" /></a>',self.image.url)
    def __str__(self):
        return f'Advertisement_2(id = {self.id}, title = {self.title}, price = {self.price})'
    class Meta:
        db_table = 'advertisements'