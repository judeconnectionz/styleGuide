from django.db import models

# Create your models here.
class StyleGuide(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=500)
    name = models.CharField(max_length=500)
    body_font_family = models.CharField(max_length=20)
    h1_font_size = models.CharField(max_length=20)
    h2_font_size = models.CharField(max_length=20)
    h3_font_size = models.CharField(max_length=20)
    h4_font_size = models.CharField(max_length=20)
    h5_font_size = models.CharField(max_length=20)
    h6_font_size = models.CharField(max_length=20)
    h6_font_weight = models.CharField(max_length=20)
    paragraph_font_size = models.CharField(max_length=20)
    span_float =  models.CharField(max_length=20)
    span_margin_right =  models.CharField(max_length=20)
    span_width =  models.CharField(max_length=20)
    span_height =  models.CharField(max_length=20)
    colour1 = models.CharField(max_length=20)
    colour2 = models.CharField(max_length=20)
    colour3 = models.CharField(max_length=20)
    colour4 = models.CharField(max_length=20)
    colour5 = models.CharField(max_length=20)
