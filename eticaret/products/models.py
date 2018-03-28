from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Cateogory(models.Model):
    slug = models.SlugField(max_length=80, null=True, blank=True,help_text=u"Link otomatik alinir, Lutfen Degistirmeyiniz!")
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='BlogResimleri/%Y/%m/%d', default='BlogResimleri/blog.png')
    create_time = models.DateTimeField(auto_now_add=True)
    enable = models.BooleanField(default=True)
    def __unicode__(self):
        return '{}'.format(self.title)

class SubCateogory(models.Model):
    cateogory = models.ForeignKey(Cateogory,on_delete=models.CASCADE,related_name='cateogory')
    slug = models.SlugField(max_length=80, null=True, blank=True,help_text=u"Link otomatik alinir, Lutfen Degistirmeyiniz!")
    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='BlogResimleri/%Y/%m/%d', default='BlogResimleri/blog.png')
    create_time = models.DateTimeField(auto_now_add=True)
    enable = models.BooleanField(default=True)
    def __unicode__(self):
        return '{}'.format(self.title)

class Products(models.Model):


    sub_cateogory = models.ForeignKey(SubCateogory)
    slug = models.SlugField(max_length=80, null=True, blank=True,help_text=u"Link otomatik alinir, Lutfen Degistirmeyiniz!")
    title = models.CharField(max_length=255, null=True, blank=True)
    price = models.IntegerField(help_text='Bu Alan Bos Birakilamaz!')
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='BlogResimleri/%Y/%m/%d', default='BlogResimleri/blog.png')
    video = models.FileField(upload_to='Videos/%Y/%m/%d', blank=True)
    link = models.URLField(blank=True)
    enable = models.BooleanField(default=True)
    readingCounter = models.IntegerField(default=0, editable=False)
    def __unicode__(self):
        return '{}'.format(self.title)