from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=100,verbose_name='Title',blank=False,null=False)
    subtitle = models.CharField(max_length=100,verbose_name='Subtitle')
    content = models.TextField(verbose_name='Content')
    image = models.ImageField(upload_to='services',verbose_name='Image')
    created = models.DateTimeField(auto_now_add=True,verbose_name='Created time')
    updated = models.DateField(auto_now=True,verbose_name='Updated time')

    class Meta():
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
        ordering = ['-created']

    def __str__(self):
        return self.title
    