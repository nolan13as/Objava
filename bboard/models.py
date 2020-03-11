from django.db import models


class Bb(models.Model):
        title = models.CharField(max_length=50, verbose_name='Товар')
        content = models.TextField(null =True, blank=True, verbose_name='Описание')
        price = models.FloatField(null=True, blank=True,verbose_name='Цена')
        published = models.DateTimeField(auto_now_add=True, db_index=True,verbose_name='Опубликовано')
        rubric = models.ForeignKey('Rubric', null = True, on_delete=models.PROTECT, verbose_name='Рубрика')
        img = models.ImageField(upload_to='', null=True, blank=True, verbose_name='Изображение')

        class Meta:
            verbose_name_plural = 'Объявления'
            verbose_name = 'Объявление'
            ordering = ['-published']

        def image_img(self):
            if self.img:
                from django.utils.safestring import mark_safe
                return mark_safe(
                    u'<a href="{0}" target="_blank"><img src="{0}" width="100"/></a>'.format(self.img.url))
            else:
                return '(Нет изображения)'

        image_img.short_description = 'Картинка'
        image_img.allow_tags = True

class Rubric(models.Model):
    name = models.CharField(max_length = 20,db_index=True, verbose_name ='Название')

    def __str__(self):
        return  self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']
# Create your models here.
