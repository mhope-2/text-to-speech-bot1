from django.db import models

# Create your models here.
class URLModel(models.Model):
    id = models.IntegerField(primary_key=True)
    url = models.URLField()

    def __str__(self):
        return str(self.url)

    class Meta:
        verbose_name = "url"
        verbose_name_plural = "urls"
