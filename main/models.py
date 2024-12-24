from datetime import date
from django.db import models
from django.contrib.auth.models import User

class Interest(models.Model):
    title = models.CharField('Название', max_length=50)
    icon = models.FileField('Иконка', upload_to='images/')

    class Meta:
        verbose_name = 'Интерес'
        verbose_name_plural = 'Интересы'

    def __str__(self):
        return self.title

class DatingProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='dating_profile')
    name = models.CharField('Название', max_length=30)
    bio = models.TextField('Описание анкеты')
    image = models.ImageField('Фотография', upload_to='images/')
    date_birth = models.DateField('Дата рождения')
    interests = models.ManyToManyField(Interest, related_name='profile')

    class Meta:
        verbose_name = 'Анкета'
        verbose_name_plural = 'Анкеты'

    def __str__(self):
        return f"{self.name}'s Profile"

    def age(self):
        today = date.today()
        return today.year - self.date_birth.year - ((today.month, today.day) < (self.date_birth.month, self.date_birth.day))
