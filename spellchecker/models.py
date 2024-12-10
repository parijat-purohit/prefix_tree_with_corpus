from django.db import models


class Prefix(models.Model):
    word = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Prefix'
        verbose_name_plural = 'Prefixes'
