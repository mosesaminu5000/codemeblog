from django.db import models


class core(models.Model):
    tittle = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models. TextField()
    body = models. TextField()
    created_at = models.DateTimeField(auto_now_add=True)