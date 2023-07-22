from django.db import models
from django.utils.safestring import mark_safe
#import validators if need be
#import machine learning library
#import module extension where model was saved e.g joblib
import tensorflow as hub
import joblib

# Create your models here.
class Data(models.Model):
    file = models.ImageField(null=True, blank=True, upload_to='media/')
    rating = models.CharField(max_length=100, blank=True)
    date = models.DateTimeField(auto_now_add=True)

    # def save(self, *args, **kwargs):
    #     #load model in variable e.g:
    #     # ml_model = joblib.load('ML_Model/...*.joblib')
    #     # self.rating = ml_model.predict([[self.file]])
        
    #     return super().save(*args, *kwargs)
    
    def logo_image(self):
        return mark_safe('<img src="{}" width="100" />'.format(self.file))
    logo_image.short_description = 'Logo'
    logo_image.allow_tags = True

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.rating