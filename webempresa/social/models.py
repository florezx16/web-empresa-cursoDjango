from django.db import models

# Create your models here.
class Link(models.Model):
    key = models.SlugField(verbose_name='Key name',max_length=100,unique=True)
    name = models.CharField(verbose_name='Social network',max_length=50)
    url = models.URLField(verbose_name='Link', max_length=200,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True,verbose_name='Created time')
    updated = models.DateField(auto_now=True,verbose_name='Updated time')

    class Meta:
        verbose_name = 'Link'
        verbose_name_plural = 'Links'
        ordering = ['name']
    
    def __str__(self) -> str:
        return self.name