from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

# Create your models here.
class Page(models.Model):
    title = models.CharField(verbose_name='Title',max_length=100)
    content = CKEditor5Field('text',config_name='extends')
    order = models.SmallIntegerField(verbose_name='Order',default=0)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Created time')
    updated = models.DateField(auto_now=True,verbose_name='Updated time')

    class Meta:
        verbose_name = 'Page'
        verbose_name_plural = 'Pages'
        ordering = ['order','title']
    
    def __str__(self) -> str:
        return self.title